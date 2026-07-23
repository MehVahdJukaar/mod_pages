<p style="text-align:center"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/separators/vista.png" alt="separator" width="1688" height="42"></p>

<h2 style="text-align:center">📖 About 📖</h2>

Vista adds working screens to Minecraft. Televisions play Cassettes, and can be linked to a Viewfinder placed anywhere in the world to show a live camera feed of it. TVs can be tiled into screens of any size.

Screens render through a CRT filter with scanlines, vignette and a turn-on animation. The mod also adds reflective Mirrors, Picture Tapes for displaying maps and photos, and a Wave Gate that streams media from a URL.

<p style="text-align:center"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/separators/vista.png" alt="separator" width="1688" height="42"></p>

<h2 style="text-align:center">🖼️ Media 🖼️</h2>

**Cinematic trailer:**

<p style="text-align:center"><iframe src="https://www.youtube.com/embed/FvLPfYxOePA?wmode=transparent" width="638" height="358" allowfullscreen="allowfullscreen"></iframe></p>

**Community review:**

<p style="text-align:center"><iframe src="https://www.youtube.com/embed/h_vfz68BfH4?wmode=transparent" width="638" height="358" allowfullscreen="allowfullscreen"></iframe></p>

<p style="text-align:center"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/separators/vista.png" alt="separator" width="1688" height="42"></p>

<h2 style="text-align:center">📺 Features 📺</h2>

### Television

- Needs a redstone signal to turn on
- Adjacent TVs merge into one big screen, up to 8x8 by default, 24x24 max
- Accepts cassettes, picture tapes, or a hollow cassette for a live feed
- Works with hoppers and droppers
- Shift-click to pause
- Optionally consumes Forge energy on NeoForge

### Cassettes

- Each plays a different looping animation. About 20 are included
- Dropped by creepers killed by a pillager
- 3% chance in rare loot chests: woodland mansions, stronghold libraries, jungle temples, igloos, bastions, shipwrecks, nether fortresses, trail ruins, ominous trial chamber rewards
- **Hollow Cassette**: bind it to a Viewfinder, then play it in a TV for the live feed

### Viewfinder

- Right-click opens its screen: lens slot, pitch and yaw controls, view button
- Sneak-click to look through it directly
- Scroll to zoom, click to lock the view
- A glass pane in the lens slot tints the linked TV's output
- View distance controllable with redstone
- Can be aimed by a Supplementaries turntable or a ComputerCraft computer
- Keeps broadcasting from Create contraptions (NeoForge only) and Sable sublevels

### Mirror

- Render a real reflection of the world, not a static texture
- Tile into larger surfaces, like TVs
- Placed flush with the block face or recessed into it, depending on where you click
- Reflect other mirrors recursively, with correct parallax. Depth and quality falloff are configurable
- Work on Sable sublevels
- Made with **Crystalline**, dropped by elder guardians

### Picture Tape

- Holds up to 32 pictures and plays them as a slideshow on any TV
- Right-click to load pictures and set playback speed
- Accepts filled maps and vanilla paintings, plus Exposure photographs and albums and Joy of Painting canvases

### Wave Gate

- Set it to any URL or local file (video, image or GIF) to play it on a linked TV
- Creative-only by default, craftable via config
- Needs FFmpeg, which the mod offers to download on first launch, or the WaterMedia mod
- URL allowlist config for servers
- Exposed as a ComputerCraft peripheral

### Misc

- Looking at an enderman through a TV angers it. Killing an enderman angered this way drops the **Sojourn** music disc
- Playing a cassette on a large screen grants the **Absolute Cinema** advancement

<p style="text-align:center"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/separators/vista.png" alt="separator" width="1688" height="42"></p>

<h2 style="text-align:center">⚙️ Compatibility ⚙️</h2>

| Mod | What you get |
|---|---|
| **Supplementaries** | Mob head shaders in the lens slot, turntable-driven panning |
| **ComputerCraft** | Viewfinder and wave gate peripherals |
| **Create** | Viewfinders broadcasting from moving contraptions (NeoForge only) |
| **Sable** / **Create Aeronautics** | Viewfinders and mirrors on moving sublevels |
| **Exposure** | Photographs and albums on picture tapes |
| **Joy of Painting** | Painted canvases on picture tapes |
| **Vampirism** | Vampires are not rendered in mirrors or camera feeds |
| **Distant Horizons**, **Sodium**, **Entity Culling**, **Flashback**, **Veil** | Feeds render correctly when these are installed |

> **Iris and Oculus:** Vista has visual glitches and degraded performance with Iris installed, even with shader packs off. This can't be fixed from Vista's side.

**WaterMedia 3.0.0+** changed its API incompatibly, so Vista disables that integration automatically. Stay below 3.0.0 if you need it.

<p style="text-align:center"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/separators/vista.png" alt="separator" width="1688" height="42"></p>

<h2 style="text-align:center">🛠️ For Pack Makers 🛠️</h2>

- Cassette tapes are a datapack registry, no code needed
- Put JSON definitions in `data/<your_pack>/vista/cassette_tape/` and the matching GIF or PNG in a resource pack
- Definitions support `sound` and `sound_duration`
- See the [mod's own tapes](https://github.com/MehVahdJukaar/cameramod/tree/master/common/src/main/resources/data/vista/vista/cassette_tape) for reference
- Mirrors, picture tapes and the wave gate can each be disabled entirely in the config, along with screen size limits and the rendering pipeline

<p style="text-align:center"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/separators/vista.png" alt="separator" width="1688" height="42"></p>

<h2 style="text-align:center">❤️ Support Me ❤️</h2>

Modding takes a lot of my time. If you like what I do and want to support me, you'll receive a custom **Globe** and/or **Statue** just for you - this also applies if you buy a server from Akliz using the code below.

<p style="text-align:center"><a href="https://ko-fi.com/mehvahdjukaar"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/badges/kofi.png" alt="Ko-Fi"></a></p>

Need a server? **Akliz** offers top-tier servers built for modded Minecraft, with a great community and support team.  
Use code **"supplementaries"** to get **20% off** and support me at the same time!

<p style="text-align:center"><a href="https://www.akliz.net/supplementaries"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/badges/akliz.png" alt="Akliz Server Hosting" width="640" height="150"></a></p>

<p style="text-align:center"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/separators/vista.png" alt="separator" width="1688" height="42"></p>

<h2 style="text-align:center">🦉 Our Mods 🦉</h2>

<p style="text-align:center">
<a href="https://modrinth.com/mod/supplementaries"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/supplementaries.gif" alt="Supplementaries" width="125" height="125"></a>
<a href="https://modrinth.com/mod/amendments"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/amendments.gif" alt="Amendments" width="125" height="125"></a>
<a href="https://modrinth.com/mod/every-compat"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/every-compat.gif" alt="Every Compat (Wood Good)" width="125" height="125"></a>
<a href="https://modrinth.com/mod/supplementaries-squared"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/supp-squared.png" alt="Supplementaries Squared" width="125" height="125"></a>
<a href="https://modrinth.com/mod/map-atlases"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/map-atlases.png" alt="Map Atlases" width="125" height="125"></a>
<a href="https://modrinth.com/mod/universal-sawmill"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/sawmill.png" alt="Universal Sawmill" width="125" height="125"></a>
<a href="https://modrinth.com/mod/polytone"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/polytone.png" alt="Polytone" width="125" height="125"></a>
<a href="https://modrinth.com/mod/pack-editor"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/pack-editor.png" alt="Nautilus Studio" width="125" height="125"></a>
<a href="https://modrinth.com/mod/snowy-spirit"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/snowy-spirit.png" alt="Snowy Spirit" width="125" height="125"></a>
<a href="https://modrinth.com/mod/haunted-harvest"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/haunted-harvest.gif" alt="Haunted Harvest" width="125" height="125"></a>
<a href="https://modrinth.com/mod/sleep-tight"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/sleep-tight.png" alt="Sleep Tight" width="125" height="125"></a>
<a href="https://modrinth.com/mod/smarter-farmers-farmers-replant"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/smarter-farmers.png" alt="Smarter Farmers" width="125" height="125"></a>
<a href="https://modrinth.com/mod/mystical-oak-tree"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/mystical-oak-tree.gif" alt="Mystical Oak Tree" width="125" height="125"></a>
<a href="https://modrinth.com/mod/labels"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/labels.png" alt="Storage Labels" width="125" height="125"></a>
<a href="https://modrinth.com/mod/goated"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/goated.png" alt="Goated" width="125" height="125"></a>
<a href="https://modrinth.com/mod/a-good-place"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/a-good-place.gif" alt="A Good Place" width="125" height="125"></a>
<a href="https://modrinth.com/mod/heartstone"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/heartstone.gif" alt="Heartstone" width="125" height="125"></a>
<a href="https://modrinth.com/mod/fast-paintings"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/fast-paintings.png" alt="Fast Paintings" width="125" height="125"></a>
<a href="https://modrinth.com/mod/mmmmmmmmmmmm"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/mmmmmmmmmmmm.png" alt="MmmMmmMmmMmm" width="125" height="125"></a>
<a href="https://modrinth.com/mod/just-enough-effect-descriptions-jeed"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/jeed.png" alt="JEED" width="125" height="125"></a>
<a href="https://modrinth.com/mod/advancement-frames"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/advancement-frames.png" alt="Advancement Frames" width="125" height="125"></a>
<a href="https://modrinth.com/mod/randomium-ore"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/randomium.png" alt="Randomium" width="125" height="125"></a>
<a href="https://modrinth.com/mod/moyai"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/moyai.png" alt="Moyai" width="125" height="125"></a>
</p>
