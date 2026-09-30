# Studio

## Pip

`pip/index.html` shows Pip, an armoured two-legged walker with three companion drones, patrolling an endless terrain map. The map is drawn in 2.5D from a fixed isometric angle. It is only visuals; there is no brain behind it.

Serve the folder with any static server and open the page:

```
python3 -m http.server 8000
# then open http://127.0.0.1:8000/pip/
```

The page is a single file. It loads three.js r170 from jsDelivr and fonts from Google Fonts, so it needs internet access.

### What you see

- **Terrain**: rolling hills from a fixed Perlin height field, with lakes, sandy shores, contour lines every 0.1 units (a bolder one every 0.5) and slope-shaded colour.
- **Map squares**: a thin boundary line every 2 units, with a cross at every corner. Navy survey stakes sit on some corners. The status card shows which square Pip is in.
- **Props**: low-poly pine and round trees grow in forest patches, with boulders scattered in between. Trees between the camera and Pip turn see-through.
- **The walker**:
  - An egg-shaped white hull with panel seams and screws, and a navy crest.
  - A navy face frame around a hexagonal socket holding one glowing blue eye, with a vented chin plate and blue light strips on the cheeks.
  - Sensor pods on both sides and big hip drums under white shells.
  - Legs with white shin armour and navy knee plates, and wheeled boots.
  - The eye barrel turns to look at things. The iris blinks, squints uphill, turns into "^" when Pip says hi, and dims when it powers down.
- **The drones**: three round white scouts with navy caps, one blue eye each, and a slow two-bladed rotor on each side.
  - They escort Pip in a loose ring, banking as they move.
  - Now and then one flies off to circle a nearby tree or rock.
  - One flies ahead and hovers over any spot you click.
  - They flank Pip and do barrel rolls when it says hi, and land around it when it powers down.

### Controls

| Control | Action |
|---|---|
| Click or tap the terrain | send Pip there (it says hi when it arrives; it won't walk into water) |
| Play / Pause, `P` or `Space` | start or stop the walk |
| Rotate buttons, `Q` / `E` | turn the view 90° |
| − / +, mouse wheel, `-` / `+` | zoom |
| Say hi, `W` | Pip turns to the camera and bounces; the drones roll |
| `H` | hide the controls (for screen recording) |

### How the walk works

- **Footsteps**: the feet are stepped in world space onto the height field. A planted boot stays put and tilts to match the slope. The next foot then swings to where the body will be when it lands, lifting higher when it steps uphill.
- **Legs**: two-bone IK with the knees forward.
- **Body**: bobs and sways toward the standing foot, settles at each footfall, and slows down going uphill.
- **Face plates**: flat 2D shapes bent onto the curved hull along its surface normal.
- **Drones**: spring-damped toward a target that depends on what Pip is doing, and they keep clear of each other.
- **Wandering**: Pip curves gently and slides around trees and rocks. Feelers stop it walking into lakes, and if it gets stuck it turns away.
- **Behaviour**: a small state machine: patrol, scan around, say hi, power down, or go to a clicked spot. Nothing is learned.
- **Streaming world**: the terrain mesh and props are regenerated around the camera as Pip moves, so the walk never ends. A radial haze fades the edges of the map into the paper background.
