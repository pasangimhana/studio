// Renders index.html frame-by-frame into an MP4 (deterministic, no dropped frames).
// usage: node render.mjs [out.mp4] [fps] [loops]   |   node render.mjs --still t out.png
import { chromium } from 'playwright';
import { spawn, execSync } from 'node:child_process';
import { readFileSync, writeFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import path from 'node:path';

const dir = path.dirname(fileURLToPath(import.meta.url));
const wrapped = path.join(dir, '.capture.html');
writeFileSync(wrapped, '<!doctype html><html><head><meta charset="utf-8"></head><body>' + readFileSync(path.join(dir, 'index.html'), 'utf8') + '</body></html>');

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1440, height: 1080 }, deviceScaleFactor: 1 });
page.on('pageerror', e => console.error('PAGE ERROR', e));
await page.goto('file://' + wrapped + '#capture');
await page.waitForFunction(() => window.__ready);
const shot = async t => { await page.evaluate(t => window.__render(t), t); return page.screenshot({ type: 'png', clip: { x: 0, y: 0, width: 1440, height: 1080 } }); };

if (process.argv[2] === '--still') {
  writeFileSync(process.argv[4], await shot(+process.argv[3]));
} else {
  const out = process.argv[2] || path.join(dir, 'twelve-dragons.mp4');
  const fps = +(process.argv[3] || 30), loops = +(process.argv[4] || 2);
  const ff = execSync('python3 -c "import imageio_ffmpeg as f;print(f.get_ffmpeg_exe())"').toString().trim();
  const p = spawn(ff, ['-y', '-f', 'image2pipe', '-framerate', String(fps), '-i', '-', '-c:v', 'libx264', '-preset', 'slow', '-crf', '16', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', out], { stdio: ['pipe', 'inherit', 'inherit'] });
  const n = 8 * fps;
  const frames = [];
  for (let i = 0; i < n; i++) { frames.push(await shot(i / fps)); if (i % 30 === 0) console.log('frame', i, '/', n); }
  for (let l = 0; l < loops; l++) for (const f of frames) if (!p.stdin.write(f)) await new Promise(r => p.stdin.once('drain', r));
  p.stdin.end(); await new Promise(r => p.on('close', r));
  console.log('wrote', out);
}
await browser.close();
