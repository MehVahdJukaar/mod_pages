<p style="text-align:center">
<a href="https://discord.gg/qdKRTDf8Cv"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/badges/discord.svg" alt="Discord" height="56"></a>
<a href="https://patreon.com/mehvahdjukaar"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/badges/patreon.svg" alt="Patreon" height="56"></a>
<a href="https://www.twitter.com/Supplementariez"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/badges/twitter.svg" alt="Twitter" height="56"></a>
<a href="https://www.youtube.com/channel/UCOaLLgwzOdbH6rCI7izCptw"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/badges/youtube.svg" alt="YouTube" height="56"></a>
</p>

<p style="text-align:center"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/separators/pack-editor.png" alt="separator" width="1688" height="42"></p>

<p style="text-align:center"><span style="font-size:24px"><strong>📖 About 📖</strong></span></p>

<p><span style="font-size:18px"><strong>Nautilus Studio</strong> is an in-game <strong>data & resource pack workbench</strong>.</span></p>

<p><span style="font-size:18px">Instead of hand-writing JSON in a text editor and guessing at the right fields, it adds a fully fledged IDE alongside your game.</span></p>

<p><span style="font-size:18px">In short, pick a file, fill in the fields, hit reload, and watch the change appear in your world instantly.</span></p>

<p><span style="font-size:18px">It reads the game's own definitions to build these editors automatically, works with any mod.</span></p>

<p style="text-align:center"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/separators/pack-editor.png" alt="separator" width="1688" height="42"></p>

<p style="text-align:center"><span style="font-size:24px"><strong>🖼️ Media 🖼️</strong></span></p>

<p style="text-align:center"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/media/packs_editor.png" alt="The Nautilus Studio workbench with file tree, generated form, and live JSON"></p>

<p style="text-align:center"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/separators/pack-editor.png" alt="separator" width="1688" height="42"></p>

<p style="text-align:center"><span style="font-size:24px"><strong>📦 What It Can Edit 📦</strong></span></p>

<p><span style="font-size:18px">Out of the box, Nautilus Studio ships form editors for a broad slice of vanilla content, including:</span></p>

<ul>
<li><span style="font-size:18px"><strong>Worldgen</strong>: configured & placed features, carvers, biomes, noise settings, density functions, world presets</span></li>
<li><span style="font-size:18px"><strong>Structures</strong>: structures, structure sets, jigsaw pools</span></li>
<li><span style="font-size:18px"><strong>Loot & Predicates</strong>: loot tables, item modifiers, predicates</span></li>
<li><span style="font-size:18px"><strong>Recipes & Advancements</strong></span></li>
<li><span style="font-size:18px"><strong>Enchantments</strong></span></li>
<li><span style="font-size:18px"><strong>World & Dimension</strong>: dimensions, dimension types</span></li>
<li><span style="font-size:18px"><strong>Mob Variants</strong>, <strong>Decoration & Trims</strong>, <strong>Items & Sound</strong>, and more</span></li>
</ul>

<p><span style="font-size:18px">...plus whatever mods contribute. <a href="https://modrinth.com/mod/polytone"><strong>Polytone</strong></a>, for example, registers its content so you can edit colormaps, particle effects and custom models right inside the workbench. You can even point it at a <strong>custom codec by class name</strong> to generate an editor for content it has never seen before.</span></p>

<p style="text-align:center"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/separators/pack-editor.png" alt="separator" width="1688" height="42"></p>

<p style="text-align:center"><span style="font-size:24px"><strong>🚀 Getting Started 🚀</strong></span></p>

<ol>
<li><span style="font-size:18px">Install Nautilus Studio and join a world (the editor needs a live world for registries and reloads).</span></li>
<li><span style="font-size:18px">On <strong>Fabric</strong>, open it from the <strong>Mod Menu</strong> entry. On <strong>NeoForge</strong>, open it from the mod's config-screen button in the mods list.</span></li>
<li><span style="font-size:18px">The workbench window opens beside your game. Open a pack folder, pick a file, and start editing.</span></li>
<li><span style="font-size:18px">Hit <strong>reload</strong> to push your changes into the running game.</span></li>
</ol>

<blockquote><p><span style="font-size:18px"><strong>Tip:</strong> Nautilus Studio runs best on <strong>Fabric</strong>. On NeoForge the editor window can occasionally fail to open due to Java's headless-window restrictions.</span></p></blockquote>

<p style="text-align:center"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/separators/pack-editor.png" alt="separator" width="1688" height="42"></p>

<p style="text-align:center"><span style="font-size:24px"><strong>🛠️ For Mod Developers 🛠️</strong></span></p>

<p><span style="font-size:18px">For most things the mod should just work. However if you want proper compat here is what you can do:</span></p>

<p><span style="font-size:18px">To register your codec so they appear by default in the editor you can register them like such:</span></p>

<pre><code>NautilusStudioApi.register(
    "My Mod",                  // group name, shown next to "Minecraft"
    "Widget Layout",           // this content type's label
    MY_CODEC,                  // your per-file Codec (the DIRECT_CODEC)
    Side.CLIENT_RESOURCES,     // CLIENT_RESOURCES (assets/) or SERVER_DATA (data/)
    "mymod/widgets"            // folder the files live in
);</code></pre>

<p><span style="font-size:18px">To get nicer widgets, a color picker, a slider, a dropdown for a sum type, build your codec as a <a href="https://github.com/MehVahdJukaar/codecui"><strong>CodecUI</strong></a> <code>SchemaCodec</code> and pass that instead. It stays a real <code>Codec</code> with the same wire format. Anything CodecUI can't read falls back to a validated raw-JSON editor, so registering is always safe.</span></p>

<p><span style="font-size:18px">Simply add these lines (jar-in-jar, so CodecUI ships inside your mod) and replace your <code>Codec</code> calls with <code>SchemaCodec</code> calls, following the API in that class:</span></p>

<pre><code>repositories {
    maven { url "https://registry.somethingcatchy.net/repository/maven-public/" }
}

dependencies {
    // Fabric (Loom)
    modImplementation "net.mehvahdjukaar:codecui-fabric:1.21.11-0.4.0"
    include           "net.mehvahdjukaar:codecui-fabric:1.21.11-0.4.0"

    // NeoForge (ModDevGradle)
    implementation "net.mehvahdjukaar:codecui-neoforge:1.21.11-0.4.0"
    jarJar         "net.mehvahdjukaar:codecui-neoforge:1.21.11-0.4.0"
}</code></pre>

<p><span style="font-size:18px">See the <a href="https://github.com/MehVahdJukaar/codecui">CodecUI repo</a> for the full DSL and examples.</span></p>

<p style="text-align:center"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/separators/pack-editor.png" alt="separator" width="1688" height="42"></p>

<p style="text-align:center"><span style="font-size:24px"><strong>❓ F.A.Q. ❓</strong></span></p>

<p><span style="font-size:18px"><strong>Q: Is this client-side only?</strong></span></p>

<p><span style="font-size:18px"><strong>A:</strong> Yes. The editor is a client tool: it edits pack files on disk and reloads your client. You don't need it on a server.</span></p>

<p><span style="font-size:18px"><strong>Q: Do players need this to use my pack/mod?</strong></span></p>

<p><span style="font-size:18px"><strong>A:</strong> No. Nautilus Studio is a <em>creation</em> tool. The packs you make with it are plain vanilla data/resource packs that work for everyone.</span></p>

<p><span style="font-size:18px"><strong>Q: Does it work with modded content?</strong></span></p>

<p><span style="font-size:18px"><strong>A:</strong> Yes. Any mod that registers its codec (a one-liner, thanks to CodecUI) shows up automatically. You can also add custom codecs yourself by class name.</span></p>

<p><span style="font-size:18px"><strong>Q: What if Nautilus Studio doesn't understand a file?</strong></span></p>

<p><span style="font-size:18px"><strong>A:</strong> It falls back to a live-validated raw JSON editor with syntax highlighting, so you can still edit anything.</span></p>

<p><span style="font-size:18px"><strong>Q: Do I need CodecUI as a dependency?</strong></span></p>

<p><span style="font-size:18px"><strong>A:</strong> No. Nautilus Studio bundles it. You only touch CodecUI directly if you want to hand-tune your editor's widgets.</span></p>

<p><span style="font-size:18px"><strong>Q: Fabric or NeoForge?</strong></span></p>

<p><span style="font-size:18px"><strong>A:</strong> Both are supported. Fabric is the smoother experience; on NeoForge the external window can occasionally hit AWT headless limitations.</span></p>

<p style="text-align:center"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/separators/pack-editor.png" alt="separator" width="1688" height="42"></p>

<p><span style="font-size:18px">Modding takes a lot of my time. If you like what I do and want to support me, you'll receive a custom <strong>Globe</strong> and/or <strong>Statue</strong> just for you - this also applies if you buy a server from Akliz using the code below.</span></p>

<p style="text-align:center"><a href="https://ko-fi.com/mehvahdjukaar"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/badges/kofi.png" alt="Ko-Fi"></a></p>

<p><span style="font-size:18px">Need a server? <strong>Akliz</strong> offers top-tier servers built for modded Minecraft, with a great community and support team.<br>Use code <strong>"supplementaries"</strong> to get <strong>20% off</strong> and support me at the same time!</span></p>

<p style="text-align:center"><a href="https://www.akliz.net/supplementaries"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/badges/akliz.png" alt="Akliz Server Hosting" width="640" height="150"></a></p>

<p style="text-align:center"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/separators/pack-editor.png" alt="separator" width="1688" height="42"></p>

<p style="text-align:center">
<a href="https://www.curseforge.com/minecraft/mc-mods/supplementaries"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/supplementaries.gif" alt="Supplementaries" width="125" height="125"></a>
<a href="https://www.curseforge.com/minecraft/mc-mods/amendments"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/amendments.gif" alt="Amendments" width="125" height="125"></a>
<a href="https://www.curseforge.com/minecraft/mc-mods/every-compat"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/every-compat.png" alt="Every Compat (Wood Good)" width="125" height="125"></a>
<a href="https://www.curseforge.com/minecraft/mc-mods/supplementaries-squared"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/supp-squared.png" alt="Supplementaries Squared" width="125" height="125"></a>
<a href="https://www.curseforge.com/minecraft/mc-mods/map-atlases-forge"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/map-atlases.png" alt="Map Atlases" width="125" height="125"></a>
<a href="https://www.curseforge.com/minecraft/mc-mods/sawmill"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/sawmill.png" alt="Universal Sawmill" width="125" height="125"></a>
<a href="https://www.curseforge.com/minecraft/mc-mods/polytone"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/polytone.png" alt="Polytone" width="125" height="125"></a>
<a href="https://www.curseforge.com/minecraft/mc-mods/snowy-spirit"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/snowy-spirit.png" alt="Snowy Spirit" width="125" height="125"></a>
<a href="https://www.curseforge.com/minecraft/mc-mods/haunted-harvest"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/haunted-harvest.png" alt="Haunted Harvest" width="125" height="125"></a>
<a href="https://www.curseforge.com/minecraft/mc-mods/sleep-tight"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/sleep-tight.png" alt="Sleep Tight" width="125" height="125"></a>
<a href="https://www.curseforge.com/minecraft/mc-mods/smarter-farmers-farmers-replant"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/smarter-farmers.png" alt="Smarter Farmers" width="125" height="125"></a>
<a href="https://www.curseforge.com/minecraft/mc-mods/mystical-oak-tree"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/mystical-oak-tree.png" alt="Mystical Oak Tree" width="125" height="125"></a>
<a href="https://www.curseforge.com/minecraft/mc-mods/labels"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/labels.png" alt="Storage Labels" width="125" height="125"></a>
<a href="https://www.curseforge.com/minecraft/mc-mods/goated"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/goated.png" alt="Goated" width="125" height="125"></a>
<a href="https://www.curseforge.com/minecraft/mc-mods/a-good-place"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/a-good-place.png" alt="A Good Place" width="125" height="125"></a>
<a href="https://www.curseforge.com/minecraft/mc-mods/vista"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/vista.gif" alt="Vista" width="125" height="125"></a>
<a href="https://www.curseforge.com/minecraft/mc-mods/heartstone"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/heartstone.png" alt="Heartstone" width="125" height="125"></a>
<a href="https://www.curseforge.com/minecraft/mc-mods/fast-paintings"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/fast-paintings.png" alt="Fast Paintings" width="125" height="125"></a>
<a href="https://www.curseforge.com/minecraft/mc-mods/mmmmmmmmmmmm"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/mmmmmmmmmmmm.png" alt="MmmMmmMmmMmm" width="125" height="125"></a>
<a href="https://www.curseforge.com/minecraft/mc-mods/just-enough-effect-descriptions-jeed"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/jeed.png" alt="JEED" width="125" height="125"></a>
<a href="https://www.curseforge.com/minecraft/mc-mods/jepp"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/jepp.png" alt="JEPP" width="125" height="125"></a>
<a href="https://www.curseforge.com/minecraft/mc-mods/advancement-frames"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/advancement-frames.png" alt="Advancement Frames" width="125" height="125"></a>
<a href="https://www.curseforge.com/minecraft/mc-mods/randomium-ore"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/randomium.png" alt="Randomium" width="125" height="125"></a>
<a href="https://www.curseforge.com/minecraft/mc-mods/moyai"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/moyai.png" alt="Moyai" width="125" height="125"></a>
</p>
