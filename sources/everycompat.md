---
name: "Every Compat (Wood Good)"
slug: every-compat
separator: "assets/separators/every-compat.png"
cf_slug: every-compat
mr_slug: every-compat
dependency:
  name: "Moonlight Library"
  cf_slug: selene
  mr_slug: moonlight
---

[BADGES]
[SEPARATOR]

## 📖 About 📖

Tired of incomplete wood sets? Every mod adds its own woods, every other mod adds its own wooden blocks, and none of them know about each other. You end up with cherry planks but no cherry bookshelf, walnut logs but no walnut chair.

Every Compat fixes that automatically. It looks at the wood types and the wooden block types you have installed, then registers the missing combinations, textures and all. Install Quark and Twilight Forest and you get Twilight Forest vertical slabs. Install Macaw's Furniture and Regions Unexplored and you get every Macaw's block in every Regions Unexplored wood.

No per-mod compat addons to hunt down, no config to fill in. One mod, everything filled in.

[SEPARATOR]

## ✨ What It Does ✨

- Adds **every supported block type in every installed wood type**, automatically
- Generates textures, models, recipes, loot tables and tags at runtime
- Detects other compat addons and skips anything they already register, so nothing is duplicated
- Converts blocks from compat mods you have since removed into their Every Compat equivalents, so worlds don't lose their builds
- Ships an API so mod authors can register a whole block definition in about ten lines

Installed on its own it does nothing at all: it only registers blocks when there is a gap to fill.

[SEPARATOR]

## 🪑 Supported Mods 🪑

Every Compat has modules for the wood-adding and furniture-adding mods below. Coverage varies by Minecraft version and loader, and the list keeps growing.

**Furniture & decoration**: Another Furniture, Beautify, Decorative Blocks, Decoration Delight, Furnish, Handcrafted, Hearth and Home, ReDeco, Refurbished Furniture (Crayfish), Unusual Furniture, Valhelsia Furniture, Clutter, Woodster, Workshop for Handsome Adventurer

**Macaw's**: Bridges, Doors, Fences, Furniture, Lights, Paths, Roofs, Stairs, Trapdoors, Windows

**Building & blocks**: Absent by Design, Architect's Palette, Blockus, Builders Addition, Builders Delight, Building But Better, Excessive Building, Infinity Buttons, Mosaic Carpentry, Quark, Stylish Stiles, Timber Frames, Twigs, Variant Vanilla Blocks

**Wood & trees**: Boat Load, Missing Wilds, Premium Wood, Regions Unexplored, Wilder Wild, Woodworks, Bark Carpets

**Storage & utility**: Functional Storage, More Chest Variants, More Crafting Tables, Storage Drawers, Variant Crafting Tables, Wooden Hoppers, Lightman's Currency, Mighty Mail

**Adventure & world**: Bewitchment, Create, Dawn of Time, Friends and Foes, Graveyard, Just a Raft, Pokecube AIO, Productive Bees, Tropicraft, Twilight Forest, Valhelsia Structures, Villagers Plus, Xerca

**Farming & food**: Farmer's Delight, Oreberries Replanted, Beautiful Campfires

**And more**: Awning, Backpacked, Bibliocraft, Camp Chair, Chipped, Copper Age Backport, Corail Pillar, Curiosities, Dramatic Doors, Lauch's Shutters, Red Bits, Table Top Craft

For the current, authoritative list, check the [Every Compat GitHub](https://github.com/MehVahdJukaar/WoodGood). If a mod you want isn't there, open a "Suggest a mod" issue.

[SEPARATOR]

## 📦 Addons 📦

- [**Gems Realm**](https://www.curseforge.com/minecraft/mc-mods/gems-realm): the same treatment for gems, metals, crystals and redstone

[SEPARATOR]

## ❓ F.A.Q. ❓

**Q: How does this work?**
**A:** Magic. (Really: it reads the block definitions of supported mods, then registers copies of them for every wood type it finds, generating all assets at runtime.)

**Q: Is this compatible with other compat mods?**
**A:** Yes. Every Compat knows about most popular compat addons and won't register anything they already provide.

**Q: This mod eats too much RAM!**
**A:** Only if you ask it to. Alone it registers nothing. The moment you install ten wood mods and ten furniture mods, it registers the hundred-odd blocks that combination implies, exactly as if those blocks had shipped in the mods themselves. How much it registers is entirely up to which mods you install.

**Q: How do I retexture a block?**
**A:** With a resource pack, same as any other mod. Every Compat builds its textures at runtime but the game treats them as if they were loaded from a folder. Turn on the debug resources config option and it will dump every generated file to a `/debug` folder in your instance directory so you can see the exact paths.

**Q: A block type isn't supported, can I add it myself?**
**A:** Not from a config, since registration can't be conditional. If you write code, you can make a pull request or call the `EveryCompatAPI` class from your own mod.

**Q: I'm a mod author, can I use this to add support for my blocks?**
**A:** Yes, and please do. The API takes about ten lines per block definition and generates all the assets for you.

**Q: Can I use this in my modpack?**
**A:** Go ahead.

[SEPARATOR]
[SUPPORT]
[SEPARATOR]
[OUR_MODS]
