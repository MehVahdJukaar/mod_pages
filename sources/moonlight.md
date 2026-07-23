---
name: "Moonlight Lib"
slug: moonlight
separator: "assets/separators/blue.png"
icon: null
cf_slug: selene
mr_slug: moonlight
---

[BADGES]
[SEPARATOR]

## 📖 About 📖

Formerly known as Selene Library, **Moonlight Lib** is a collection of utilities and shared code used across all of MehVahdJukaar's mods.

**If you're a player:** You don't need to do anything special - Moonlight is automatically pulled in as a dependency when you install any mod that requires it. Just install it and forget about it.

**If you're a developer:** This library gives you a solid multiloader foundation with a focus on simplicity over boilerplate. Full documentation is available in the [Java Docs](https://github.com/MehVahdJukaar/Moonlight/tree/1.20/common/src/main/java/net/mehvahdjukaar/moonlight/api) and [example package](https://github.com/MehVahdJukaar/Moonlight/tree/1.20/common/src/example/java) on GitHub.

[SEPARATOR]

## 🛠️ Features 🛠️

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

[SEPARATOR]
[SUPPORT]
[SEPARATOR]
[OUR_MODS]
