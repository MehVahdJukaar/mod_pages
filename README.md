# mod_pages

Image assets for the CurseForge and Modrinth pages of my mods, plus `moonlight_mods.json`.

Everything here is served straight over `raw.githubusercontent.com`, so the paths are part of
what's already published. Don't rename or move files: the live mod pages link to them by URL.

```
assets/
  badges/       Discord, Patreon, Twitter, YouTube, Ko-Fi, Akliz badges
  separators/   per-mod divider bars
  mod_icons/    mod icons, used in the "Our Mods" grid
  banners/      page header images
  media/        screenshots used on the pages
moonlight_mods.json
```

## moonlight_mods.json

The mod catalog behind Moonlight's in-game "discover mods" screen. Moonlight fetches it from this
repo at runtime, from a URL hardcoded in `OurModsList.java`, so it has to stay at the repo root
under this exact name. Editing it changes what players see in game.
