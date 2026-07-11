---
name: "PackEditor"
slug: pack-editor
separator: "assets/separators/teal.png"
icon: null
cf_slug: pack-editor
mr_slug: pack-editor
---

[BADGES]
[SEPARATOR]

## 📖 About 📖

**PackEditor** is an in-game **data & resource pack workbench**. Instead of hand-writing JSON in a text editor and guessing at the right fields, it opens a real desktop window right next to your game and turns any content format into an **editable form**: pick a file, fill in the fields, hit reload, and watch the change appear in your world instantly.

It reads the game's own definitions to build these editors automatically, so it always knows exactly which fields exist, what type each one is, and what values are valid. No more typos, no more missing brackets, no more digging through the wiki to remember a field name.

**PackEditor is content-agnostic.** Out of the box it can edit dozens of vanilla content types, and any mod can plug its own content in with a single line of code.

[SEPARATOR]

## 🖼️ Media 🖼️

![The PackEditor workbench with file tree, generated form, and live JSON](assets/media/packs_editor.png)

[SEPARATOR]

## ✨ Features ✨

- 🧩 **Auto-generated editors**: every content type becomes a typed form built from the game's own codecs, so the editor always matches the real format
- 🗂️ **Pack file browser**: open any data or resource pack and navigate it in a familiar file tree
- 🎛️ **Smart widgets**: dropdowns for enums, color pickers, add/remove rows for lists, and **registry pickers** that search real block/item/entity IDs
- 📝 **Raw JSON fallback**: anything too custom to introspect gets a live-validated JSON editor with **syntax highlighting**
- 🔄 **Live reload**: push your edits into the running game with one click, no restart needed
- 🖥️ **Real desktop UI**: a modern, resizable window beside Minecraft, not cramped inside a game screen
- 🔌 **Content-agnostic**: ships with editors for a wide range of vanilla content, and any mod can register its own

[SEPARATOR]

## 📦 What It Can Edit 📦

Out of the box, PackEditor ships form editors for a broad slice of vanilla content, including:

- **Worldgen**: configured & placed features, carvers, biomes, noise settings, density functions, world presets
- **Structures**: structures, structure sets, jigsaw pools
- **Loot & Predicates**: loot tables, item modifiers, predicates
- **Recipes & Advancements**
- **Enchantments**
- **World & Dimension**: dimensions, dimension types
- **Mob Variants**, **Decoration & Trims**, **Items & Sound**, and more

...plus whatever mods contribute. [**Polytone**](https://modrinth.com/mod/polytone), for example, registers its content so you can edit colormaps, particle effects and custom models right inside PackEditor. You can even point it at a **custom codec by class name** to generate an editor for content it has never seen before.

[SEPARATOR]

## 🚀 Getting Started 🚀

1. Install PackEditor and join a world (the editor needs a live world for registries and reloads).
2. On **Fabric**, open it from the **Mod Menu** entry. On **NeoForge**, open it from the mod's config-screen button in the mods list.
3. The workbench window opens beside your game. Open a pack folder, pick a file, and start editing.
4. Hit **reload** to push your changes into the running game.

> **Tip:** PackEditor runs best on **Fabric**. On NeoForge the editor window can occasionally fail to open due to Java's headless-window restrictions.

[SEPARATOR]

## 🛠️ For Mod Developers 🛠️

Have your own data-driven content? Make it editable in one call, no UI code required:

```java
PackEditorApi.register(
    "My Mod",              // library group (your mod's name)
    "Widget Layout",       // human-readable content name
    MY_CODEC,              // your existing per-file codec
    Side.ASSETS,           // assets/ or data/
    "mymod/widgets"        // in-pack folder
);
```

PackEditor turns your codec into a full form editor automatically, groups your content under your mod's name next to the vanilla entries, and handles file placement, validation and reloads for you. Anything it can't introspect falls back to the validated raw-JSON editor.

[SEPARATOR]

## ❓ F.A.Q. ❓

**Q: Is this client-side only?**
**A:** Yes. The editor is a client tool: it edits pack files on disk and reloads your client. You don't need it on a server.

**Q: Do players need this to use my pack/mod?**
**A:** No. PackEditor is a *creation* tool. The packs you make with it are plain vanilla data/resource packs that work for everyone.

**Q: Does it work with modded content?**
**A:** Yes. Any mod that registers its codecs (a one-liner) shows up automatically. You can also add custom codecs yourself by class name.

**Q: What if PackEditor doesn't understand a file?**
**A:** It falls back to a live-validated raw JSON editor with syntax highlighting, so you can still edit anything.

**Q: Fabric or NeoForge?**
**A:** Both are supported. Fabric is the smoother experience; on NeoForge the external window can occasionally hit AWT headless limitations.

[SEPARATOR]
[SUPPORT]
[SEPARATOR]
[OUR_MODS]
