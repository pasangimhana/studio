// Renders index.html frame by frame into an MP4 (deterministic, no dropped frames), then adds the soundtrack.
// usage: node render.mjs [out.mp4] [fps]   |   node render.mjs --still t out.png   |   node render.mjs --sheet out.png t1 t2 ...
import { chromium } from 'playwright';
import { spawn, execFileSync } from 'node:child_process';
import { writeFileSync, rmSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import path from 'node:path';

const dir = path.dirname(fileURLToPath(import.meta.url));
const W = 1920, H = 1080;

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: W, height: H }, deviceScaleFactor: 1 });
page.on('pageerror', e => console.error('PAGE ERROR', e));
page.on('console', m => { if (m.type() === 'error') console.error('CONSOLE', m.text()); });
await page.goto('file://' + path.join(dir, 'index.html') + '#capture');
await page.waitForFunction(() => window.__ready);
const shot = async (t, type = 'png') => { await page.evaluate(t => window.__render(t), t); return page.screenshot({ type, clip: { x: 0, y: 0, width: W, height: H } }); };
const run = (cmd, args) => new Promise((ok, fail) => spawn(cmd, args, { stdio: 'inherit' }).on('close', c => c ? fail(new Error(cmd + ' exited ' + c)) : ok()));

const mode = process.argv[2];
if (mode === '--still') {
  writeFileSync(process.argv[4], await shot(+process.argv[3]));
} else if (mode === '--sheet') {
  // contact sheet: one small frame per requested time, for quick review
  const times = process.argv.slice(4).map(Number), imgs = [];
  for (const t of times) imgs.push('data:image/jpeg;base64,' + (await shot(t, 'jpeg')).toString('base64'));
  const p2 = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
  const cols = 3, rows = Math.ceil(times.length / cols);
  await p2.setViewportSize({ width: 1920, height: rows * 360 });
  await p2.setContent(`<body style="margin:0;background:#000;display:grid;grid-template-columns:repeat(${cols},640px)">${imgs.map((s, i) => `<div style="position:relative"><img src="${s}" style="width:640px;height:360px;display:block"><b style="position:absolute;left:6px;top:4px;color:#ff0;font:16px monospace;background:#000a;padding:2px 5px">${times[i]}s</b></div>`).join('')}</body>`);
  writeFileSync(process.argv[3], await p2.screenshot({ fullPage: true }));
} else {
  const out = mode || path.join(dir, 'from-72-to-722.mp4');
  const fps = +(process.argv[3] || 30);
  const dur = await page.evaluate(() => window.__duration);
  const silent = out.replace(/\.mp4$/, '') + '.video.mp4', wav = path.join(dir, '.soundtrack.wav');
  const ff = spawn('ffmpeg', ['-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', String(fps), '-i', '-', '-c:v', 'libx264', '-preset', 'slow', '-crf', '18', '-pix_fmt', 'yuv420p', silent], { stdio: ['pipe', 'inherit', 'inherit'] });
  const done = new Promise(r => ff.on('close', r));
  const n = Math.round(dur * fps);
  for (let i = 0; i < n; i++) {
    const f = await shot(i / fps);
    if (!ff.stdin.write(f)) await new Promise(r => ff.stdin.once('drain', r));
    if (i % 150 === 0) console.log('frame', i, '/', n);
  }
  ff.stdin.end(); await done;
  execFileSync('python3', [path.join(dir, 'soundtrack.py'), wav], { stdio: 'inherit' });
  await run('ffmpeg', ['-y', '-loglevel', 'error', '-i', silent, '-i', wav, '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-shortest', '-movflags', '+faststart', out]);
  rmSync(silent); rmSync(wav);
  console.log('wrote', out);
}
await browser.close();
