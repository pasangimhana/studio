# Studio

## Pip

`pip/index.html` shows Pip, an armoured two-legged walker, and its three companion drones walking forever across an endless white floor. The 3D camera follows it like the Fly demo's chase camera. It is only visuals; there is no brain behind it.

Serve the folder with any static server and open the page:

```
python3 -m http.server 8000
# then open http://127.0.0.1:8000/pip/
```

The page is a single file. It loads three.js r170 from jsDelivr and fonts from Google Fonts, so it needs internet access.

### What you see

- **The studio**: the floor and the background are the same white, so there is no horizon and the floor never ends. The only marks are soft shadows and footprints, which fade after about 20 seconds.
- **Survey grid**: toward the edges and corners of the view a grid shows through the floor: fine lines every 0.5 m, bold lines every 2.5 m with a cross on each bold corner, and faint contour lines of an imaginary terrain. It is fixed to the world, so it scrolls past as Pip walks, while the middle of the view stays clean white.
- **The walker**:
  - An egg-shaped white hull with panel seams and screws, and a navy crest.
  - A navy face frame around a hexagonal socket holding one glowing blue eye, with a vented chin plate and blue light strips on the cheeks.
  - Sensor pods on both sides and big hip drums under white shells.
  - Legs with white shin armour and navy knee plates, and wheeled boots.
  - The eye barrel turns to look at things. The iris blinks, turns into "^" when Pip says hi, and dims when it powers down.
- **The drones**: three round white scouts with navy caps, one blue eye each, and a slow two-bladed rotor on each side.
  - They escort Pip in a loose ring, banking as they move.
  - Now and then one flies out to scan a patch of floor while Pip watches it.
  - One flies ahead and hovers over any spot you click.
  - They flank Pip and do barrel rolls when it says hi, and land around it when it powers down.

### Controls

| Control | Action |
|---|---|
| Click or tap the floor | send Pip there (it says hi when it arrives) |
| Play / Pause, `P` or `Space` | start or stop the walk |
| Auto / Follow / Front / Side, `C` | camera (Auto cycles through the shots and turns to the front for hi and naps) |
| Mouse wheel | move the camera closer or further |
| Say hi, `W` | Pip turns to the camera and bounces; the drones roll |
| `H` | hide the controls (for screen recording) |

### How the walk works

- **Footsteps**: the feet are stepped in world space. A planted boot stays put, and the next foot swings to where the body will be when it lands, so turns and stops never slide.
- **Legs**: two-bone IK with the knees forward.
- **Body**: bobs and sways toward the standing foot, and settles at each footfall.
- **Face plates**: flat 2D shapes bent onto the curved hull along its surface normal, and shaded with the hull's own normal.
- **Drones**: spring-damped toward a target that depends on what Pip is doing, and they keep clear of each other.
- **Behaviour**: a small state machine: patrol, scan around, say hi, power down, or go to a clicked spot. Nothing is learned.
