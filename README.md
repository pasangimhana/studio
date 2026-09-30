# Studio

## Pip

`pip/index.html` shows a small white box robot on two legs, walking forever across an endless terrain map. The map is drawn in 2.5D from a fixed isometric angle. It is only visuals; there is no brain behind it.

Serve the folder with any static server and open the page:

```
python3 -m http.server 8000
# then open http://127.0.0.1:8000/pip/
```

The page is a single file. It loads three.js r170 from jsDelivr and fonts from Google Fonts, so it needs internet access.

### What you see

- **Terrain**: rolling hills from a fixed Perlin height field, with lakes, sandy shores, contour lines every 0.1 units (a bolder one every 0.5) and slope-shaded colour.
- **Map squares**: a thin boundary line every 2 units, with a cross at every corner. Orange survey stakes sit on some corners. The status card shows which square Pip is in.
- **Props**: low-poly pine and round trees grow in forest patches, with boulders scattered in between. Trees between the camera and Pip turn see-through.
- **Pip**: a rounded white box with a glossy face screen and two bird-style legs, with knees that bend backward. The eyes are drawn live: they blink, glance ahead of where Pip is going, squint uphill, turn into "^ ^" when it says hi, and close when it naps. A springy antenna wobbles with every step.

### Controls

| Control | Action |
|---|---|
| Click or tap the terrain | send Pip there (it says hi when it arrives; it won't walk into water) |
| Play / Pause, `P` or `Space` | start or stop the walk |
| Rotate buttons, `Q` / `E` | turn the view 90° |
| − / +, mouse wheel, `-` / `+` | zoom |
| Say hi, `W` | Pip turns to the camera and bounces |
| `H` | hide the controls (for screen recording) |

### How the walk works

- **Footsteps**: the feet are stepped in world space onto the height field. A planted foot stays put and tilts to match the ground. The next foot then swings to where the body will be when it lands, lifting higher when it steps uphill.
- **Legs**: two-bone IK with the knees pointing backward.
- **Body**: bobs and sways toward the standing foot, dips at each footfall, and slows down going uphill.
- **Wandering**: Pip curves gently and slides around trees and rocks. Feelers stop it walking into lakes, and if it gets stuck it turns away.
- **Behaviour**: a small state machine: walk, look around, say hi, nap, or go to a clicked spot. Nothing is learned.
- **Streaming world**: the terrain mesh and props are regenerated around the camera as Pip moves, so the walk never ends. A radial haze fades the edges of the map into the paper background.
