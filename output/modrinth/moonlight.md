<p style="text-align:center"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/separators/moonlight.png" alt="separator" width="1688" height="42"></p>

<h2 style="text-align:center">📖 About 📖</h2>

Formerly Selene Library, Moonlight Lib is the shared code behind all of MehVahdJukaar's mods.

Players do not need to do anything with it: it is pulled in automatically as a dependency by any mod that requires it.

For developers it is a multiloader foundation aimed at cutting boilerplate. Documentation lives in the [Java Docs](https://github.com/MehVahdJukaar/Moonlight/tree/1.20/common/src/main/java/net/mehvahdjukaar/moonlight/api) and the [example package](https://github.com/MehVahdJukaar/Moonlight/tree/1.20/common/src/example/java). To import it, use **"Copy Gradle Line"** in the Files section.

<p style="text-align:center"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/separators/moonlight.png" alt="separator" width="1688" height="42"></p>

<h2 style="text-align:center">🛠️ Features 🛠️</h2>

### Dynamic Assets

- Generate any datapack or resource pack asset at runtime
- Texture API covering palette extraction, cropping, reshaping and automatic recoloring

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

### Multiloader Utilities

- Static helpers emulating Forge behavior on Fabric: `PlatHelper`, `ClientHelper`, `RegHelper` and `ForgeHelper`
- `ConfigBuilder` for configs, with Codec support, early loading and automatic client sync
- `ChannelHandler` for networking

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

### Dynamic Registration (BlockSetAPI)

- Detect block sets right after block registration, then register new entries derived from them
- `WoodTypeRegistry` and `LeavesTypeRegistry` populate automatically with every wood and leaf type installed

<details>
<summary>BlockSetAPI examples</summary>

![BlockSetAPI define](https://i.imgur.com/UXqIcTu.png)
![BlockSetAPI register](https://i.imgur.com/0pbcAXp.png)

</details>

### Custom Baked Models

- Custom model loaders and quad utilities for advanced rendering

<details>
<summary>Model Loader & Quad Utils examples</summary>

![Model Loader](https://i.imgur.com/oRY0fS8.png)
![Quad Utils](https://i.imgur.com/hu4aYCz.png)

</details>

### Custom Villager Trades

- Add trades to any villager from the `moonlight/villager_trades` datapack folder, with no code
- Supplementaries and Sawmill use this in production

### More Utilities

- **Block Color API**: detect any modded block's DyeColor and get the equivalent in another color
- **Custom Map Markers**: data-driven map decorations with full rendering control
- **Dynamic Villager AI**: add tasks and change villager schedules without overriding the whole AI
- **Item Animations**: custom first and third person animations, like the crossbow or spyglass
- **Soft Fluid System**: a data-driven virtual fluid system covering bottles, bowls, buckets, stews and drinks
- **Grindstone Trigger**: an advancement trigger for items passing through a grindstone
- **DispenserHelper**, **Global Datapack Folder**, **Debug Renderers**

<p style="text-align:center"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/separators/moonlight.png" alt="separator" width="1688" height="42"></p>

<h2 style="text-align:center">❤️ Support Me ❤️</h2>

Modding takes a lot of my time. If you like what I do and want to support me, you'll receive a custom **Globe** and/or **Statue** just for you - this also applies if you buy a server from Akliz using the code below.

<p style="text-align:center"><a href="https://ko-fi.com/mehvahdjukaar"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/badges/kofi.png" alt="Ko-Fi"></a></p>

Need a server? **Akliz** offers top-tier servers built for modded Minecraft, with a great community and support team.  
Use code **"supplementaries"** to get **20% off** and support me at the same time!

<p style="text-align:center"><a href="https://www.akliz.net/supplementaries"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/badges/akliz.png" alt="Akliz Server Hosting" width="640" height="150"></a></p>

<p style="text-align:center"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/separators/moonlight.png" alt="separator" width="1688" height="42"></p>

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
<a href="https://modrinth.com/mod/vista"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/vista.gif" alt="Vista" width="125" height="125"></a>
<a href="https://modrinth.com/mod/heartstone"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/heartstone.gif" alt="Heartstone" width="125" height="125"></a>
<a href="https://modrinth.com/mod/fast-paintings"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/fast-paintings.png" alt="Fast Paintings" width="125" height="125"></a>
<a href="https://modrinth.com/mod/mmmmmmmmmmmm"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/mmmmmmmmmmmm.png" alt="MmmMmmMmmMmm" width="125" height="125"></a>
<a href="https://modrinth.com/mod/just-enough-effect-descriptions-jeed"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/jeed.png" alt="JEED" width="125" height="125"></a>
<a href="https://modrinth.com/mod/advancement-frames"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/advancement-frames.png" alt="Advancement Frames" width="125" height="125"></a>
<a href="https://modrinth.com/mod/randomium-ore"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/randomium.png" alt="Randomium" width="125" height="125"></a>
<a href="https://modrinth.com/mod/moyai"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/moyai.png" alt="Moyai" width="125" height="125"></a>
</p>
