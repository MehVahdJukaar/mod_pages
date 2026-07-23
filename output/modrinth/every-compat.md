<p style="text-align:center"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/separators/lilac.png" alt="separator" width="1688" height="42"></p>

<h2 style="text-align:center">📖 About 📖</h2>

Tired of incomplete wood sets? Every mod adds its own woods, every other mod adds its own wooden blocks, and none of them know about each other. You end up with cherry planks but no cherry bookshelf, walnut logs but no walnut chair.

Every Compat fixes that automatically. It looks at the wood types and the wooden block types you have installed, then registers the missing combinations, textures and all. Install Quark and Twilight Forest and you get Twilight Forest vertical slabs. Install Macaw's Furniture and Regions Unexplored and you get every Macaw's block in every Regions Unexplored wood.

No per-mod compat addons to hunt down, no config to fill in. One mod, everything filled in.

<p style="text-align:center"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/separators/lilac.png" alt="separator" width="1688" height="42"></p>

<h2 style="text-align:center">✨ What It Does ✨</h2>

- Adds **every supported block type in every installed wood type**, automatically
- Generates textures, models, recipes, loot tables and tags at runtime
- Detects other compat addons and skips anything they already register, so nothing is duplicated
- Converts blocks from compat mods you have since removed into their Every Compat equivalents, so worlds don't lose their builds
- Ships an API so mod authors can register a whole block definition in about ten lines

Installed on its own it does nothing at all: it only registers blocks when there is a gap to fill.

<p style="text-align:center"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/separators/lilac.png" alt="separator" width="1688" height="42"></p>

<h2 style="text-align:center">🪑 Supported Mods 🪑</h2>

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

<p style="text-align:center"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/separators/lilac.png" alt="separator" width="1688" height="42"></p>

<h2 style="text-align:center">📦 Addons 📦</h2>

- [**Gems Realm**](https://www.curseforge.com/minecraft/mc-mods/gems-realm): the same treatment for gems, metals, crystals and redstone

<p style="text-align:center"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/separators/lilac.png" alt="separator" width="1688" height="42"></p>

<h2 style="text-align:center">❓ F.A.Q. ❓</h2>

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

<p style="text-align:center"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/separators/lilac.png" alt="separator" width="1688" height="42"></p>

Modding takes a lot of my time. If you like what I do and want to support me, you'll receive a custom **Globe** and/or **Statue** just for you - this also applies if you buy a server from Akliz using the code below.

<p style="text-align:center"><a href="https://ko-fi.com/mehvahdjukaar"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/badges/kofi.png" alt="Ko-Fi"></a></p>

Need a server? **Akliz** offers top-tier servers built for modded Minecraft, with a great community and support team.  
Use code **"supplementaries"** to get **20% off** and support me at the same time!

<p style="text-align:center"><a href="https://www.akliz.net/supplementaries"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/badges/akliz.png" alt="Akliz Server Hosting" width="640" height="150"></a></p>

<p style="text-align:center"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/separators/lilac.png" alt="separator" width="1688" height="42"></p>

<p style="text-align:center">
<a href="https://modrinth.com/mod/supplementaries"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/supplementaries.gif" alt="Supplementaries" width="125" height="125"></a>
<a href="https://modrinth.com/mod/amendments"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/amendments.gif" alt="Amendments" width="125" height="125"></a>
<a href="https://modrinth.com/mod/supplementaries-squared"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/supp-squared.webp" alt="Supplementaries Squared" width="125" height="125"></a>
<a href="https://modrinth.com/mod/map-atlases"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/map-atlases.png" alt="Map Atlases" width="125" height="125"></a>
<a href="https://modrinth.com/mod/universal-sawmill"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/sawmill.webp" alt="Universal Sawmill" width="125" height="125"></a>
<a href="https://modrinth.com/mod/polytone"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/polytone.png" alt="Polytone" width="125" height="125"></a>
<a href="https://modrinth.com/mod/snowy-spirit"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/snowy-spirit.webp" alt="Snowy Spirit" width="125" height="125"></a>
<a href="https://modrinth.com/mod/haunted-harvest"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/haunted-harvest.webp" alt="Haunted Harvest" width="125" height="125"></a>
<a href="https://modrinth.com/mod/sleep-tight"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/sleep-tight.png" alt="Sleep Tight" width="125" height="125"></a>
<a href="https://modrinth.com/mod/smarter-farmers-farmers-replant"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/smarter-farmers.webp" alt="Smarter Farmers" width="125" height="125"></a>
<a href="https://modrinth.com/mod/mystical-oak-tree"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/mystical-oak-tree.webp" alt="Mystical Oak Tree" width="125" height="125"></a>
<a href="https://modrinth.com/mod/labels"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/labels.webp" alt="Storage Labels" width="125" height="125"></a>
<a href="https://modrinth.com/mod/goated"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/goated.webp" alt="Goated" width="125" height="125"></a>
<a href="https://modrinth.com/mod/a-good-place"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/a-good-place.webp" alt="A Good Place" width="125" height="125"></a>
<a href="https://modrinth.com/mod/vista"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/vista.gif" alt="Vista" width="125" height="125"></a>
<a href="https://modrinth.com/mod/heartstone"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/heartstone.webp" alt="Heartstone" width="125" height="125"></a>
<a href="https://modrinth.com/mod/fast-paintings"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/fast-paintings.png" alt="Fast Paintings" width="125" height="125"></a>
<a href="https://modrinth.com/mod/mmmmmmmmmmmm"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/mmmmmmmmmmmm.png" alt="MmmMmmMmmMmm" width="125" height="125"></a>
<a href="https://modrinth.com/mod/just-enough-effect-descriptions-jeed"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/jeed.webp" alt="JEED" width="125" height="125"></a>
<a href="https://modrinth.com/mod/advancement-frames"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/advancement-frames.png" alt="Advancement Frames" width="125" height="125"></a>
<a href="https://modrinth.com/mod/randomium-ore"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/randomium.webp" alt="Randomium" width="125" height="125"></a>
<a href="https://modrinth.com/mod/moyai"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/moyai.webp" alt="Moyai" width="125" height="125"></a>
</p>
