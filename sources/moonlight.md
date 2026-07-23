---
name: "Moonlight Lib"
slug: moonlight
separator: "assets/separators/moonlight.png"
cf_slug: selene
mr_slug: moonlight
---

[BADGES]
[SEPARATOR]

## 📖 About 📖

Formerly Selene Library, Moonlight Lib is the shared code behind all of MehVahdJukaar's mods.

Players do not need to do anything with it: it is pulled in automatically as a dependency by any mod that requires it.

For developers it is a multiloader foundation aimed at cutting boilerplate. Documentation lives in the [Java Docs](https://github.com/MehVahdJukaar/Moonlight/tree/1.20/common/src/main/java/net/mehvahdjukaar/moonlight/api) and the [example package](https://github.com/MehVahdJukaar/Moonlight/tree/1.20/common/src/example/java). To import it, use **"Copy Gradle Line"** in the Files section.

[SEPARATOR]

## 🛠️ Features 🛠️

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

[SEPARATOR]
[SUPPORT]
[SEPARATOR]
[OUR_MODS]
