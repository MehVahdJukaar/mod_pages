<p style="text-align:center"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/separators/every-compat.png" alt="separator" width="1688" height="42"></p>

<h2 style="text-align:center">📖 About 📖</h2>

Every mod adds its own wood types, and every other mod adds its own wooden blocks, but none of them know about each other. The result is cherry planks with no cherry bookshelf, and walnut logs with no walnut chair.

Every Compat fills those gaps automatically. It reads the wood types and wooden block types you have installed and registers every missing combination, generating all assets at runtime. Install Macaw's Furniture and Regions Unexplored, and every Macaw's block exists in every Regions Unexplored wood.

Requires **[Moonlight Library](https://modrinth.com/mod/moonlight)**.

<p style="text-align:center"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/separators/every-compat.png" alt="separator" width="1688" height="42"></p>

<h2 style="text-align:center">✨ Features ✨</h2>

- Adds every supported block type in every installed wood type, with no configuration
- Generates textures, models, recipes, loot tables and tags at runtime
- Registers nothing at all when installed on its own, so it only costs what it fills in
- Detects other compat addons and skips anything they already register
- Converts blocks from compat mods you have since removed into their Every Compat equivalents, so old builds survive
- Ships an API letting mod authors register a whole block definition in about ten lines

<p style="text-align:center"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/separators/every-compat.png" alt="separator" width="1688" height="42"></p>

<h2 style="text-align:center">🪑 Supported Mods 🪑</h2>

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

<p style="text-align:center"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/separators/every-compat.png" alt="separator" width="1688" height="42"></p>

<h2 style="text-align:center">📦 Addons 📦</h2>

- [**Gems Realm**](https://www.curseforge.com/minecraft/mc-mods/gems-realm): the same treatment for gems, metals, crystals and redstone

<p style="text-align:center"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/separators/every-compat.png" alt="separator" width="1688" height="42"></p>

<h2 style="text-align:center">❓ F.A.Q. ❓</h2>

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

<p style="text-align:center"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/separators/every-compat.png" alt="separator" width="1688" height="42"></p>

<h2 style="text-align:center">❤️ Support Me ❤️</h2>

Modding takes a lot of my time. If you like what I do and want to support me, you'll receive a custom **Globe** and/or **Statue** just for you - this also applies if you buy a server from Akliz using the code below.

<p style="text-align:center"><a href="https://ko-fi.com/mehvahdjukaar"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/badges/kofi.png" alt="Ko-Fi"></a></p>

Need a server? **Akliz** offers top-tier servers built for modded Minecraft, with a great community and support team.  
Use code **"supplementaries"** to get **20% off** and support me at the same time!

<p style="text-align:center"><a href="https://www.akliz.net/supplementaries"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/badges/akliz.png" alt="Akliz Server Hosting" width="640" height="150"></a></p>

<p style="text-align:center"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/separators/every-compat.png" alt="separator" width="1688" height="42"></p>

<h2 style="text-align:center">🦉 Our Mods 🦉</h2>

<p style="text-align:center">
<a href="https://modrinth.com/mod/supplementaries"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/supplementaries.gif" alt="Supplementaries" width="125" height="125"></a>
<a href="https://modrinth.com/mod/amendments"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/amendments.gif" alt="Amendments" width="125" height="125"></a>
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
<a href="https://modrinth.com/mod/vista"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/vista.gif" alt="Vista" width="125" height="125"></a>
<a href="https://modrinth.com/mod/heartstone"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/heartstone.gif" alt="Heartstone" width="125" height="125"></a>
<a href="https://modrinth.com/mod/fast-paintings"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/fast-paintings.png" alt="Fast Paintings" width="125" height="125"></a>
<a href="https://modrinth.com/mod/mmmmmmmmmmmm"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/mmmmmmmmmmmm.png" alt="MmmMmmMmmMmm" width="125" height="125"></a>
<a href="https://modrinth.com/mod/just-enough-effect-descriptions-jeed"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/jeed.png" alt="JEED" width="125" height="125"></a>
<a href="https://modrinth.com/mod/advancement-frames"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/advancement-frames.png" alt="Advancement Frames" width="125" height="125"></a>
<a href="https://modrinth.com/mod/randomium-ore"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/randomium.png" alt="Randomium" width="125" height="125"></a>
<a href="https://modrinth.com/mod/moyai"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/moyai.png" alt="Moyai" width="125" height="125"></a>
</p>
