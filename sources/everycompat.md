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

Every mod adds its own wood types, and every other mod adds its own wooden blocks, but none of them know about each other. The result is cherry planks with no cherry bookshelf, and walnut logs with no walnut chair.

Every Compat fills those gaps automatically. It reads the wood types and wooden block types you have installed and registers every missing combination, generating all assets at runtime. Install Macaw's Furniture and Regions Unexplored, and every Macaw's block exists in every Regions Unexplored wood.

Requires **[DEPENDENCY]**.

[SEPARATOR]

## ✨ Features ✨

- Adds every supported block type in every installed wood type, with no configuration
- Generates textures, models, recipes, loot tables and tags at runtime
- Registers nothing at all when installed on its own, so it only costs what it fills in
- Detects other compat addons and skips anything they already register
- Converts blocks from compat mods you have since removed into their Every Compat equivalents, so old builds survive
- Ships an API letting mod authors register a whole block definition in about ten lines

[SEPARATOR]

## 🪑 Supported Mods 🪑

Coverage varies by Minecraft version and loader, and the list keeps growing.

| Category | Mods |
|---|---|
| **Furniture** | Another Furniture, Beautify, Decorative Blocks, Decoration Delight, Furnish, Handcrafted, Hearth and Home, ReDeco, Refurbished Furniture, Unusual Furniture, Valhelsia Furniture, Clutter, Woodster, Workshop for Handsome Adventurer |
| **Macaw's** | Bridges, Doors, Fences, Furniture, Lights, Paths, Roofs, Stairs, Trapdoors, Windows |
| **Building** | Absent by Design, Architect's Palette, Blockus, Builders Addition, Builders Delight, Building But Better, Excessive Building, Infinity Buttons, Mosaic Carpentry, Quark, Stylish Stiles, Timber Frames, Twigs, Variant Vanilla Blocks |
| **Wood and trees** | Boat Load, Missing Wilds, Premium Wood, Regions Unexplored, Wilder Wild, Woodworks, Bark Carpets |
| **Storage and utility** | Functional Storage, More Chest Variants, More Crafting Tables, Storage Drawers, Variant Crafting Tables, Wooden Hoppers, Lightman's Currency, Mighty Mail |
| **Adventure and world** | Bewitchment, Create, Dawn of Time, Friends and Foes, Graveyard, Just a Raft, Pokecube AIO, Productive Bees, Tropicraft, Twilight Forest, Valhelsia Structures, Villagers Plus, Xerca |
| **Farming and food** | Farmer's Delight, Oreberries Replanted, Beautiful Campfires |
| **Other** | Awning, Backpacked, Bibliocraft, Camp Chair, Chipped, Copper Age Backport, Corail Pillar, Curiosities, Dramatic Doors, Lauch's Shutters, Red Bits, Table Top Craft |

The [Every Compat GitHub](https://github.com/MehVahdJukaar/WoodGood) has the current list. If a mod is missing, open a "Suggest a mod" issue.

[SEPARATOR]

## 📦 Addons 📦

- [**Gems Realm**](https://www.curseforge.com/minecraft/mc-mods/gems-realm): the same treatment for gems, metals, crystals and redstone

[SEPARATOR]

## ❓ F.A.Q. ❓

**Q: How does this work?**
**A:** It reads the block definitions of supported mods and registers a copy of each for every wood type it finds, generating all assets at runtime.

**Q: Is this compatible with other compat mods?**
**A:** Yes. Every Compat knows about most popular compat addons and won't register anything they already provide.

**Q: This mod eats too much RAM!**
**A:** Only in proportion to what you ask of it. On its own it registers nothing. Install ten wood mods and ten furniture mods and it registers the hundreds of blocks that combination implies, exactly as if those blocks had shipped in the mods themselves.

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
