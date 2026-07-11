<p style="text-align:center"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/separators/teal.png" alt="separator" width="1688" height="42"></p>

<h2 style="text-align:center">📖 About 📖</h2>

**PackEditor** is an in-game **data & resource pack workbench**. Instead of hand-writing JSON in a text editor and guessing at the right fields, it opens a real desktop window right next to your game and turns any content format into an **editable form** — pick a file, fill in the fields, hit reload, and watch the change appear in your world instantly.

It reads the game's own definitions to build these editors automatically, so it always knows exactly which fields exist, what type each one is, and what values are valid. No more typos, no more missing brackets, no more digging through the wiki to remember a field name.

**PackEditor is content-agnostic.** Out of the box it can edit dozens of vanilla content types, and any mod can plug its own content in with a single line of code.

<p style="text-align:center"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/separators/teal.png" alt="separator" width="1688" height="42"></p>

<h2 style="text-align:center">🖼️ Media 🖼️</h2>

![The PackEditor workbench — file tree, generated form, and live JSON](https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/media/pack-editor-1.png)

![Editing content through auto-generated form widgets](https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/media/pack-editor-2.png)

![Browsing a pack and reloading the game live](https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/media/pack-editor-3.png)

<p style="text-align:center"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/separators/teal.png" alt="separator" width="1688" height="42"></p>

<h2 style="text-align:center">✨ Features ✨</h2>

- 🧩 **Auto-generated editors** — every content type becomes a typed form built from the game's own codecs. The editor always matches the real format.
- 🗂️ **Pack file browser** — open any data or resource pack and navigate it in a familiar file tree, with data and asset content clearly separated.
- 🎛️ **Smart widgets** — dropdowns for enums, color pickers for colors, add/remove rows for lists and maps, and **registry pickers** that let you search real block/item/entity IDs instead of typing them by hand.
- 📝 **Raw JSON fallback** — anything too custom to introspect drops to a live-validated JSON editor with **syntax highlighting**, so you're never locked out of a file.
- 🔄 **Live reload** — apply your edits to the running game with one click and see them immediately, no restart required.
- 🖥️ **Real desktop UI** — a modern, resizable window (FlatLaf) that lives beside Minecraft, not cramped inside a game screen.
- 🔌 **Content-agnostic** — ships with editors for a wide range of vanilla content, and any mod can register its own.

<p style="text-align:center"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/separators/teal.png" alt="separator" width="1688" height="42"></p>

<h2 style="text-align:center">📦 What It Can Edit 📦</h2>

Out of the box, PackEditor ships form editors for a broad slice of vanilla content, including:

- **Worldgen** — configured & placed features, carvers, biomes, noise settings, density functions, world presets
- **Structures** — structures, structure sets, jigsaw pools
- **Loot & Predicates** — loot tables, item modifiers, predicates
- **Recipes & Advancements**
- **Enchantments**
- **World & Dimension** — dimensions, dimension types
- **Mob Variants**, **Decoration & Trims**, **Items & Sound**, and more

...plus whatever mods contribute. For example, [**Polytone**](https://modrinth.com/mod/polytone) registers its content so you can edit colormaps, particle effects, custom models and the rest of its resource-pack format right inside PackEditor. You can even point it at a **custom codec by class name** to generate an editor for content it's never seen before.

<p style="text-align:center"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/separators/teal.png" alt="separator" width="1688" height="42"></p>

<h2 style="text-align:center">🚀 Getting Started 🚀</h2>

1. Install PackEditor and join a world (the editor needs a live world for registries and reloads).
2. On **Fabric**, open it from the **Mod Menu** entry. On **NeoForge**, open it from the mod's config-screen button in the mods list.
3. The workbench window opens beside your game. Open a pack folder, pick a file, and start editing.
4. Hit **reload** to push your changes into the running game.

> **Tip:** PackEditor runs best on **Fabric**. On NeoForge the editor window can occasionally fail to open due to Java's headless-window restrictions.

<p style="text-align:center"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/separators/teal.png" alt="separator" width="1688" height="42"></p>

<h2 style="text-align:center">🛠️ For Mod Developers 🛠️</h2>

Have your own data-driven content? Make it editable in one call — no UI code required:

```java
PackEditorApi.register(
    "My Mod",              // library group (your mod's name)
    "Widget Layout",       // human-readable content name
    MY_CODEC,              // your existing per-file codec
    Side.ASSETS,           // assets/ or data/
    "mymod/widgets"        // in-pack folder
);
```

PackEditor turns your codec into a full form editor automatically, groups your content under your mod's name next to the vanilla entries, and handles file placement, validation, and reloads for you. Anything it can't introspect gracefully falls back to a validated raw-JSON editor.

<p style="text-align:center"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/separators/teal.png" alt="separator" width="1688" height="42"></p>

<h2 style="text-align:center">❓ F.A.Q. ❓</h2>

**Q: Is this client-side only?**

**A:** Yes. The editor is a client tool — it edits pack files on disk and reloads your client. You don't need it on a server.

**Q: Do players need this to use my pack/mod?**

**A:** No. PackEditor is a *creation* tool. The packs you make with it are plain vanilla data/resource packs that work for everyone.

**Q: Does it work with modded content?**

**A:** Yes — any mod that registers its codecs (a one-liner) shows up automatically. You can also add custom codecs yourself by class name.

**Q: What if PackEditor doesn't understand a file?**

**A:** It falls back to a live-validated raw JSON editor with syntax highlighting, so you can still edit anything.

**Q: Fabric or NeoForge?**

**A:** Both are supported. Fabric is the smoother experience — on NeoForge the external window can occasionally hit AWT headless limitations.

<p style="text-align:center"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/separators/teal.png" alt="separator" width="1688" height="42"></p>

Modding takes a lot of my time. If you like what I do and want to support me, you'll receive a custom **Globe** and/or **Statue** just for you — this also applies if you buy a server from Akliz using the code below.

<p style="text-align:center"><a href="https://ko-fi.com/mehvahdjukaar"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/badges/kofi.png" alt="Ko-Fi"></a></p>

Need a server? **Akliz** offers top-tier servers built for modded Minecraft, with a great community and support team.  
Use code **"supplementaries"** to get **20% off** and support me at the same time!

<p style="text-align:center"><a href="https://www.akliz.net/supplementaries"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/badges/akliz.png" alt="Akliz Server Hosting" width="640" height="150"></a></p>

<p style="text-align:center"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/separators/teal.png" alt="separator" width="1688" height="42"></p>

<p style="text-align:center">
<a href="https://modrinth.com/mod/supplementaries"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/supplementaries.gif" alt="Supplementaries" width="125" height="125"></a>
<a href="https://modrinth.com/mod/haunted-harvest"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/haunted-harvest.webp" alt="Haunted Harvest" width="125" height="125"></a>
<a href="https://modrinth.com/mod/snowy-spirit"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/snowy-spirit.webp" alt="Snowy Spirit" width="125" height="125"></a>
<a href="https://modrinth.com/mod/labels"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/labels.webp" alt="Storage Labels" width="125" height="125"></a>
<a href="https://modrinth.com/mod/goated"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/goated.webp" alt="Goated" width="125" height="125"></a>
<a href="https://modrinth.com/mod/mystical-oak-tree"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/mystical-oak-tree.webp" alt="Mystical Oak Tree" width="125" height="125"></a>
<a href="https://modrinth.com/mod/vista"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/vista.gif" alt="Vista" width="125" height="125"></a>
<a href="https://modrinth.com/mod/mmmmmmmmmmmm"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/mmmmmmmmmmmm.png" alt="MmmMmmMmmMmm" width="125" height="125"></a>
<a href="https://modrinth.com/mod/moyai"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/moyai.webp" alt="Moyai" width="125" height="125"></a>
<a href="https://modrinth.com/mod/just-enough-effect-descriptions-jeed"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/jeed.webp" alt="JEED" width="125" height="125"></a>
<a href="https://modrinth.com/mod/advancement-frames"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/advancement-frames.png" alt="Advancement Frames" width="125" height="125"></a>
<a href="https://modrinth.com/mod/randomium-ore"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/randomium.webp" alt="Randomium" width="125" height="125"></a>
<a href="https://modrinth.com/mod/sleep-tight"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/sleep-tight.png" alt="Sleep Tight" width="125" height="125"></a>
<a href="https://modrinth.com/mod/polytone"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/polytone.png" alt="Polytone" width="125" height="125"></a>
<a href="https://modrinth.com/mod/heartstone"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/heartstone.webp" alt="Heartstone" width="125" height="125"></a>
<a href="https://modrinth.com/mod/map-atlases"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/map-atlases.png" alt="Map Atlases" width="125" height="125"></a>
<a href="https://modrinth.com/mod/universal-sawmill"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/sawmill.webp" alt="Universal Sawmill" width="125" height="125"></a>
<a href="https://modrinth.com/mod/amendments"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/amendments.gif" alt="Amendments" width="125" height="125"></a>
<a href="https://modrinth.com/mod/fast-paintings"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/fast-paintings.png" alt="Fast Paintings" width="125" height="125"></a>
</p>
