<p style="text-align:center"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/separators/blue.png" alt="separator" width="1688" height="42"></p>

<h2 style="text-align:center">📖 About 📖</h2>

Formerly known as Selene Library, **Moonlight Lib** is a collection of utilities and shared code used across all of MehVahdJukaar's mods.

**If you're a player:** You don't need to do anything special - Moonlight is automatically pulled in as a dependency when you install any mod that requires it. Just install it and forget about it.

**If you're a developer:** This library gives you a solid multiloader foundation with a focus on simplicity over boilerplate. Full documentation is available in the [Java Docs](https://github.com/MehVahdJukaar/Moonlight/tree/1.20/common/src/main/java/net/mehvahdjukaar/moonlight/api) and [example package](https://github.com/MehVahdJukaar/Moonlight/tree/1.20/common/src/example/java) on GitHub.

<p style="text-align:center"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/separators/blue.png" alt="separator" width="1688" height="42"></p>

<h2 style="text-align:center">🛠️ Features 🛠️</h2>

### 🎨 Dynamic Assets

Generate any asset dynamically for datapacks and resource packs. Includes an extensive API for generating dynamic textures: palette extraction, cropping, reshaping, automatic recoloring, and more.

<details>
<summary>Dynamic resource generation example</summary>

![Dynamic Resources](https://i.imgur.com/RipgGvz.png)

</details>

<details>
<summary>Texture recoloring example</summary>

![Texture Recoloring](https://i.imgur.com/8X9USvL.png)

</details>

<details>
<summary>Palette manipulation example</summary>

![Palette Manipulation](https://i.imgur.com/2Yiu8C5.png)

</details>

### 🌍 Multiloader Utilities

Simple static helper functions that emulate Forge behavior on Fabric. Four main API classes: `PlatHelper`, `ClientHelper`, `RegHelper`, `ForgeHelper`. Plus `ConfigBuilder` (Codec support, early loading, auto client-sync) and `ChannelHandler` for networking.

<details>
<summary>PlatHelper example</summary>

![PlatHelper](https://i.imgur.com/J09BP39.png)

</details>

<details>
<summary>RegHelper example</summary>

![RegHelper](https://i.imgur.com/EcNchXA.png)

</details>

<details>
<summary>ConfigBuilder example</summary>

![ConfigBuilder](https://i.imgur.com/XRxW9nv.png)

</details>

<details>
<summary>ChannelHandler example</summary>

![ChannelHandler](https://i.imgur.com/rE22Fcm.png)

</details>

### 📒 Dynamic Registration (BlockSetAPI)

Detect "block sets" right after all blocks are registered and dynamically register new entries that depend on them. Built-in `WoodTypeRegistry` and `LeavesTypeRegistry` automatically populate with all woods and leaves from any installed mod.

<details>
<summary>BlockSetAPI examples</summary>

![BlockSetAPI define](https://i.imgur.com/UXqIcTu.png)
![BlockSetAPI register](https://i.imgur.com/0pbcAXp.png)

</details>

### 🔷 Custom Baked Models

Custom model loaders and Quad utilities for advanced rendering.

<details>
<summary>Model Loader & Quad Utils examples</summary>

![Model Loader](https://i.imgur.com/oRY0fS8.png)
![Quad Utils](https://i.imgur.com/hu4aYCz.png)

</details>

### 🪙 Custom Villager Trades

Add custom trades to any villager via the `moonlight/villager_trades` datapack folder - no code required. See Supplementaries or Sawmill for real-world examples.

### 🧙 More Utilities

- **Block Color API** - detect any modded block's DyeColor and get the equivalent in a different color, dynamically for any block or item
- **Custom Map Markers** - data-driven custom map decorations and markers with full rendering control
- **Dynamic Villager AI** - add tasks and modify villager schedules without overriding the entire AI
- **First & Third Person Item Animations** - simple interface for custom animations similar to the crossbow or spyglass
- **Soft Fluid System** - data-driven virtual fluid system supporting bottles, bowls, buckets, stews, and drinks
- **Grindstone Trigger** - custom advancement trigger for items passing through a grindstone
- **DispenserHelper**, **Global Datapack Folder**, **Debug Renderers**

To import this library, go to the Files section and click **"Copy Gradle Line"**, then paste it into your `build.gradle`.

<p style="text-align:center"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/separators/blue.png" alt="separator" width="1688" height="42"></p>

Modding takes a lot of my time. If you like what I do and want to support me, you'll receive a custom **Globe** and/or **Statue** just for you - this also applies if you buy a server from Akliz using the code below.

<p style="text-align:center"><a href="https://ko-fi.com/mehvahdjukaar"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/badges/kofi.png" alt="Ko-Fi"></a></p>

Need a server? **Akliz** offers top-tier servers built for modded Minecraft, with a great community and support team.  
Use code **"supplementaries"** to get **20% off** and support me at the same time!

<p style="text-align:center"><a href="https://www.akliz.net/supplementaries"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/badges/akliz.png" alt="Akliz Server Hosting" width="640" height="150"></a></p>

<p style="text-align:center"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/separators/blue.png" alt="separator" width="1688" height="42"></p>

<p style="text-align:center">
<a href="https://modrinth.com/mod/supplementaries"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/supplementaries.gif" alt="Supplementaries" width="125" height="125"></a>
<a href="https://modrinth.com/mod/amendments"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/amendments.gif" alt="Amendments" width="125" height="125"></a>
<a href="https://modrinth.com/mod/every-compat"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/every-compat.webp" alt="Every Compat (Wood Good)" width="125" height="125"></a>
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
