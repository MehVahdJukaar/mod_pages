<p style="text-align:center"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/separators/pack-editor.png" alt="separator" width="1688" height="42"></p>

<h2 style="text-align:center">📖 About 📖</h2>

Nautilus Studio is an in-game data and resource pack workbench. Instead of hand-writing JSON and guessing at the right fields, it opens a full editor alongside the game: pick a file, fill in a generated form, hit reload, and the change appears in the running world.

The forms are built automatically from the game's own content definitions, so it works with modded content as well as vanilla.

<p style="text-align:center"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/separators/pack-editor.png" alt="separator" width="1688" height="42"></p>

<h2 style="text-align:center">🖼️ Media 🖼️</h2>

![The Nautilus Studio workbench with file tree, generated form, and live JSON](https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/media/packs_editor.png)

<p style="text-align:center"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/separators/pack-editor.png" alt="separator" width="1688" height="42"></p>

<h2 style="text-align:center">📦 Features 📦</h2>

### What It Can Edit

- **Worldgen**: configured and placed features, carvers, biomes, noise settings, density functions, world presets
- **Structures**: structures, structure sets, jigsaw pools
- **Loot and Predicates**: loot tables, item modifiers, predicates
- **Recipes and Advancements**
- **Enchantments**
- **World and Dimension**: dimensions, dimension types
- **Mob Variants**, **Decoration and Trims**, **Items and Sound**, and more
- Anything a mod registers. [**Polytone**](https://modrinth.com/mod/polytone) registers its colormaps, particle effects and custom models, for example
- Any custom codec, pointed at by class name, even for content the editor has never seen
- Anything it cannot parse falls back to a live-validated raw JSON editor with syntax highlighting

### Using It

- Join a world first: the editor needs live registries to build its forms and to reload
- Open it from the **Mod Menu** entry on Fabric, or the config-screen button in the mods list on NeoForge
- The workbench opens in its own window beside the game
- Hit reload to push changes into the running world

> Nautilus Studio runs best on **Fabric**. On NeoForge the editor window can occasionally fail to open, due to Java's headless-window restrictions.

<p style="text-align:center"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/separators/pack-editor.png" alt="separator" width="1688" height="42"></p>

<h2 style="text-align:center">🛠️ For Mod Developers 🛠️</h2>

For most things the mod should just work. However if you want proper compat here is what you can do:

To register your codec so they appear by default in the editor you can register them like such:

```java
NautilusStudioApi.register(
    "My Mod",                  // group name, shown next to "Minecraft"
    "Widget Layout",           // this content type's label
    MY_CODEC,                  // your per-file Codec (the DIRECT_CODEC)
    Side.CLIENT_RESOURCES,     // CLIENT_RESOURCES (assets/) or SERVER_DATA (data/)
    "mymod/widgets"            // folder the files live in
);
```

To get nicer widgets, a color picker, a slider, a dropdown for a sum type, build your codec as a [**CodecUI**](https://github.com/MehVahdJukaar/codecui) `SchemaCodec` and pass that instead. It stays a real `Codec` with the same wire format. Anything CodecUI can't read falls back to a validated raw-JSON editor, so registering is always safe.

Simply add these lines (jar-in-jar, so CodecUI ships inside your mod) and replace your `Codec` calls with `SchemaCodec` calls, following the API in that class:

```gradle
repositories {
    maven { url "https://registry.somethingcatchy.net/repository/maven-public/" }
}

dependencies {
    // Fabric (Loom)
    modImplementation "net.mehvahdjukaar:codecui-fabric:1.21.11-0.4.0"
    include           "net.mehvahdjukaar:codecui-fabric:1.21.11-0.4.0"

    // NeoForge (ModDevGradle)
    implementation "net.mehvahdjukaar:codecui-neoforge:1.21.11-0.4.0"
    jarJar         "net.mehvahdjukaar:codecui-neoforge:1.21.11-0.4.0"
}
```

See the [CodecUI repo](https://github.com/MehVahdJukaar/codecui) for the full DSL and examples.

<p style="text-align:center"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/separators/pack-editor.png" alt="separator" width="1688" height="42"></p>

<h2 style="text-align:center">❓ F.A.Q. ❓</h2>

**Q: Is this client-side only?**

**A:** Yes. The editor is a client tool: it edits pack files on disk and reloads your client. You don't need it on a server.

**Q: Do players need this to use my pack/mod?**

**A:** No. Nautilus Studio is a *creation* tool. The packs you make with it are plain vanilla data/resource packs that work for everyone.

**Q: Does it work with modded content?**

**A:** Yes. Any mod that registers its codec (a one-liner, thanks to CodecUI) shows up automatically. You can also add custom codecs yourself by class name.

**Q: What if Nautilus Studio doesn't understand a file?**

**A:** It falls back to a live-validated raw JSON editor with syntax highlighting, so you can still edit anything.

**Q: Do I need CodecUI as a dependency?**

**A:** No. Nautilus Studio bundles it. You only touch CodecUI directly if you want to hand-tune your editor's widgets.

**Q: Fabric or NeoForge?**

**A:** Both are supported. Fabric is the smoother experience; on NeoForge the external window can occasionally hit AWT headless limitations.

<p style="text-align:center"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/separators/pack-editor.png" alt="separator" width="1688" height="42"></p>

<h2 style="text-align:center">❤️ Support Me ❤️</h2>

Modding takes a lot of my time. If you like what I do and want to support me, you'll receive a custom **Globe** and/or **Statue** just for you - this also applies if you buy a server from Akliz using the code below.

<p style="text-align:center"><a href="https://ko-fi.com/mehvahdjukaar"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/badges/kofi.png" alt="Ko-Fi"></a></p>

Need a server? **Akliz** offers top-tier servers built for modded Minecraft, with a great community and support team.  
Use code **"supplementaries"** to get **20% off** and support me at the same time!

<p style="text-align:center"><a href="https://www.akliz.net/supplementaries"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/badges/akliz.png" alt="Akliz Server Hosting" width="640" height="150"></a></p>

<p style="text-align:center"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/separators/pack-editor.png" alt="separator" width="1688" height="42"></p>

<h2 style="text-align:center">🦉 Our Mods 🦉</h2>

<p style="text-align:center">
<a href="https://modrinth.com/mod/supplementaries"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/supplementaries.gif" alt="Supplementaries" width="125" height="125"></a>
<a href="https://modrinth.com/mod/amendments"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/amendments.gif" alt="Amendments" width="125" height="125"></a>
<a href="https://modrinth.com/mod/every-compat"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/every-compat.gif" alt="Every Compat (Wood Good)" width="125" height="125"></a>
<a href="https://modrinth.com/mod/supplementaries-squared"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/supp-squared.png" alt="Supplementaries Squared" width="125" height="125"></a>
<a href="https://modrinth.com/mod/map-atlases"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/map-atlases.png" alt="Map Atlases" width="125" height="125"></a>
<a href="https://modrinth.com/mod/universal-sawmill"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/sawmill.png" alt="Universal Sawmill" width="125" height="125"></a>
<a href="https://modrinth.com/mod/polytone"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/polytone.png" alt="Polytone" width="125" height="125"></a>
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
