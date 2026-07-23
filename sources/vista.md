---
name: "Vista"
slug: vista
separator: "assets/separators/vista.png"
cf_slug: vista
mr_slug: vista
---

[BADGES]
[SEPARATOR]

## 📖 About 📖

Vista adds working screens to Minecraft. Televisions play Cassettes, and can be linked to a Viewfinder placed anywhere in the world to show a live camera feed of it. TVs can be tiled into screens of any size.

Screens render through a CRT filter with scanlines, vignette and a turn-on animation. The mod also adds reflective Mirrors, Picture Tapes for displaying maps and photos, and a Wave Gate that streams media from a URL.

[SEPARATOR]

## 🖼️ Media 🖼️

[YOUTUBE: FvLPfYxOePA | Cinematic trailer]

[YOUTUBE: h_vfz68BfH4 | Community review]

[SEPARATOR]

## 📺 Features 📺

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

[SEPARATOR]

## ⚙️ Compatibility ⚙️

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

[SEPARATOR]

## 🛠️ For Pack Makers 🛠️

- Cassette tapes are a datapack registry, no code needed
- Put JSON definitions in `data/<your_pack>/vista/cassette_tape/` and the matching GIF or PNG in a resource pack
- Definitions support `sound` and `sound_duration`
- See the [mod's own tapes](https://github.com/MehVahdJukaar/cameramod/tree/master/common/src/main/resources/data/vista/vista/cassette_tape) for reference
- Mirrors, picture tapes and the wave gate can each be disabled entirely in the config, along with screen size limits and the rendering pipeline

[SEPARATOR]
[SUPPORT]
[SEPARATOR]
[OUR_MODS]
