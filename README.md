# Studio

## Pip

`pip/index.html` shows a small white two-legged robot wandering an endless studio floor. It uses the same floor, light and camera style as the Fly × Jev demo, but there is no brain behind it, only the visuals.

Serve the folder with any static server and open the page:

```
python3 -m http.server 8000
# then open http://127.0.0.1:8000/pip/
```

The page is a single file. It loads three.js r170 from jsDelivr and fonts from Google Fonts, so it needs internet access.

### What it does

- Pip walks on its own, curving gently and stepping around the balls, blocks, pillars and cones scattered on the floor.
- Every so often it stops to look around, or turns to the camera and waves.
- When it spots a potted plant it walks over, leans in and looks at it for a moment. Each plant is visited once.
- Every footstep leaves a print that fades after about 25 seconds. A faint line traces the longer path.

### Controls

| Control | Action |
|---|---|
| Click or tap the floor | send Pip to that spot (it waves when it gets there) |
| Play / Pause, `P` or `Space` | start or stop the walk |
| Auto / Follow / Front / Side, `C` | camera (Auto cycles through the others and cuts to the front for waves) |
| Say hi, `W` | Pip turns to the camera and waves |
| `H` | hide the controls (for screen recording) |

### How the walk works

- The feet are stepped in world space. A planted foot stays put until it lifts. The next foot then swings to where the body will be when it lands, so turns and stops come out right without sliding.
- The legs are two-bone IK with forward-bending knees. The body bobs, sways and rolls toward the standing foot, and dips a little at each footfall.
- The head and eyes follow springs, so glances overshoot slightly. The eyes lead the head and blink on big glances. The arms swing opposite the legs.
- Behaviour is a small state machine: walk, look around, wave, visit a plant, go to a clicked spot. Nothing is learned.
