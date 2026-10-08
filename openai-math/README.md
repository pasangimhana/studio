# From 72 to 722

A 114-second, math-style hype reel about OpenAI's math milestones, from GSM8K's grade-school word problems in 2021 to the 722 research manuscripts released on October 6, 2026. The title comes from GSM8K's first example problem, whose answer is 72.

`from-72-to-722.mp4` is 1920×1080, 30 fps, H.264 + AAC.

| Time | Section |
| --- | --- |
| 0:00 | §0 · 2021: the Natalia word problem, worked out to 72 |
| 0:09 | 72 → 722 |
| 0:15 | Title |
| 0:19 | §1 · The climb: GSM8K, GPT-4, o1, o3, IMO gold, Erdős #728 |
| 0:41 | §2 · May 20, 2026: Erdős's unit distance conjecture disproved |
| 0:51 | §3 · Aug 2026: Astra, ten open problems with Lean certificates |
| 0:59 | §4 · Sep 8, 2026: Navier–Stokes finite-time blow-up |
| 1:11 | §5 · Sep 21, 2026: 100+ problems claimed |
| 1:15 | §6 · Oct 6, 2026: 722 manuscripts, ζ(s), Hodge, and more |
| 1:33 | §7 · How far we've come |
| 1:48 | ∎ |

## How it's built

- `index.html` draws every frame. Geometry goes on a canvas and text is set with KaTeX. `window.__render(t)` is a pure function of time, so frames render deterministically. Open the page in a browser to preview it: click pauses, ←/→ seek 2 s, and 0–9 jump to tenths. `index.html#42` starts playback at 42 s.
- `soundtrack.py` synthesises the music and sound effects with numpy (kick, snare, hats, bass, pads, plucks, risers, impacts, typing clicks, reverb). It reads the `CUES` line in `index.html`, so beats and hits stay in sync with the picture.
- `render.mjs` screenshots every frame with Playwright, encodes the frames with ffmpeg, generates the soundtrack, and muxes the two.
- `vendor/` holds KaTeX (MIT) plus Inter and JetBrains Mono (OFL), so rendering needs no network.

```
node render.mjs from-72-to-722.mp4 30          # full render (~13 min)
node render.mjs --still 85 frame.png           # one frame at t = 85 s
node render.mjs --sheet sheet.png 20 45.5 66   # contact sheet of several frames
python3 soundtrack.py out.wav                  # audio only
```

Needs Node with Playwright (link or install it into `node_modules/`), ffmpeg on `PATH`, and Python 3 with numpy.

## Accuracy notes

- The 2026 results are presented as OpenAI announced them. Independent verification of the Navier–Stokes proof, the 100+ problem claim and the October 6 manuscripts was still in progress at release. The video says so on screen, and the end card says so again.
- The vertical axis of the climb chart is qualitative: milestones are placed on a smooth exponential, not plotted against a measured score.
- The unit-distance and ζ(s) visuals are schematic. The lattice is a projection of the cyclotomic integers ℤ[ζ₅] in the spirit of the construction, not the construction itself. σ₀ is left unlabelled because reports disagree on the claimed bound.
- The o1 AIME figure (83%) is consensus over 64 samples; single-sample accuracy was 74%.

Sources are listed in [SOURCES.md](SOURCES.md).
