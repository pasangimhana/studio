# 12 Ways to Draw a Dragon

`index.html` is a 1440×1080 (4:3) animated grid. All 12 panels loop every 8 seconds, so the video loops cleanly.

Render the video frame by frame, with no dropped frames:

```
node render.mjs twelve-dragons.mp4 30 2   # output, fps, number of loops
node render.mjs --still 4.5 frame.png     # one frame at t = 4.5s
```

Needs Playwright plus `imageio-ffmpeg` (`pip install imageio-ffmpeg`) for the ffmpeg binary.
