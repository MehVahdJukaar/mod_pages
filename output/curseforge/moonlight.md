<p style="text-align:center">
<a href="https://discord.gg/qdKRTDf8Cv"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/badges/discord.svg" alt="Discord" height="56"></a>
<a href="https://patreon.com/mehvahdjukaar"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/badges/patreon.svg" alt="Patreon" height="56"></a>
<a href="https://www.twitter.com/Supplementariez"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/badges/twitter.svg" alt="Twitter" height="56"></a>
<a href="https://www.youtube.com/channel/UCOaLLgwzOdbH6rCI7izCptw"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/badges/youtube.svg" alt="YouTube" height="56"></a>
</p>

<p style="text-align:center"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/separators/blue.png" alt="separator" width="1688" height="42"></p>

<p style="text-align:center"><span style="font-size:24px"><strong>📖 About 📖</strong></span></p>

<p><span style="font-size:18px">Formerly known as Selene Library, <strong>Moonlight Lib</strong> is a collection of utilities and shared code used across all of MehVahdJukaar's mods.</span></p>

<p><span style="font-size:18px"><strong>If you're a player:</strong> You don't need to do anything special — Moonlight is automatically pulled in as a dependency when you install any mod that requires it. Just install it and forget about it.</span></p>

<p><span style="font-size:18px"><strong>If you're a developer:</strong> This library gives you a solid multiloader foundation with a focus on simplicity over boilerplate. Full documentation is available in the <a href="https://github.com/MehVahdJukaar/Moonlight/tree/1.20/common/src/main/java/net/mehvahdjukaar/moonlight/api">Java Docs</a> and <a href="https://github.com/MehVahdJukaar/Moonlight/tree/1.20/common/src/example/java">example package</a> on GitHub.</span></p>

<p style="text-align:center"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/separators/blue.png" alt="separator" width="1688" height="42"></p>

<p style="text-align:center"><span style="font-size:24px"><strong>🛠️ Features 🛠️</strong></span></p>

<p><strong>🎨 Dynamic Assets</strong></p>

<p><span style="font-size:18px">Generate any asset dynamically for datapacks and resource packs. Includes an extensive API for generating dynamic textures: palette extraction, cropping, reshaping, automatic recoloring, and more.</span></p>

<p><span style="font-size:18px"><strong>Dynamic resource generation example:</strong></span></p>
<div class="spoiler"><img src="https://i.imgur.com/RipgGvz.png" alt="Dynamic Resources"></div>

<p><span style="font-size:18px"><strong>Texture recoloring example:</strong></span></p>
<div class="spoiler"><img src="https://i.imgur.com/8X9USvL.png" alt="Texture Recoloring"></div>

<p><span style="font-size:18px"><strong>Palette manipulation example:</strong></span></p>
<div class="spoiler"><img src="https://i.imgur.com/2Yiu8C5.png" alt="Palette Manipulation"></div>

<p><strong>🌍 Multiloader Utilities</strong></p>

<p><span style="font-size:18px">Simple static helper functions that emulate Forge behavior on Fabric. Four main API classes: <code>PlatHelper</code>, <code>ClientHelper</code>, <code>RegHelper</code>, <code>ForgeHelper</code>. Plus <code>ConfigBuilder</code> (Codec support, early loading, auto client-sync) and <code>ChannelHandler</code> for networking.</span></p>

<p><span style="font-size:18px"><strong>PlatHelper example:</strong></span></p>
<div class="spoiler"><img src="https://i.imgur.com/J09BP39.png" alt="PlatHelper"></div>

<p><span style="font-size:18px"><strong>RegHelper example:</strong></span></p>
<div class="spoiler"><img src="https://i.imgur.com/EcNchXA.png" alt="RegHelper"></div>

<p><span style="font-size:18px"><strong>ConfigBuilder example:</strong></span></p>
<div class="spoiler"><img src="https://i.imgur.com/XRxW9nv.png" alt="ConfigBuilder"></div>

<p><span style="font-size:18px"><strong>ChannelHandler example:</strong></span></p>
<div class="spoiler"><img src="https://i.imgur.com/rE22Fcm.png" alt="ChannelHandler"></div>

<p><strong>📒 Dynamic Registration (BlockSetAPI)</strong></p>

<p><span style="font-size:18px">Detect "block sets" right after all blocks are registered and dynamically register new entries that depend on them. Built-in <code>WoodTypeRegistry</code> and <code>LeavesTypeRegistry</code> automatically populate with all woods and leaves from any installed mod.</span></p>

<p><span style="font-size:18px"><strong>BlockSetAPI examples:</strong></span></p>
<div class="spoiler"><img src="https://i.imgur.com/UXqIcTu.png" alt="BlockSetAPI define">
<img src="https://i.imgur.com/0pbcAXp.png" alt="BlockSetAPI register"></div>

<p><strong>🔷 Custom Baked Models</strong></p>

<p><span style="font-size:18px">Custom model loaders and Quad utilities for advanced rendering.</span></p>

<p><span style="font-size:18px"><strong>Model Loader & Quad Utils examples:</strong></span></p>
<div class="spoiler"><img src="https://i.imgur.com/oRY0fS8.png" alt="Model Loader">
<img src="https://i.imgur.com/hu4aYCz.png" alt="Quad Utils"></div>

<p><strong>🪙 Custom Villager Trades</strong></p>

<p><span style="font-size:18px">Add custom trades to any villager via the <code>moonlight/villager_trades</code> datapack folder — no code required. See Supplementaries or Sawmill for real-world examples.</span></p>

<p><strong>🧙 More Utilities</strong></p>

<ul>
<li><span style="font-size:18px"><strong>Block Color API</strong> — detect any modded block's DyeColor and get the equivalent in a different color, dynamically for any block or item</span></li>
<li><span style="font-size:18px"><strong>Custom Map Markers</strong> — data-driven custom map decorations and markers with full rendering control</span></li>
<li><span style="font-size:18px"><strong>Dynamic Villager AI</strong> — add tasks and modify villager schedules without overriding the entire AI</span></li>
<li><span style="font-size:18px"><strong>First & Third Person Item Animations</strong> — simple interface for custom animations similar to the crossbow or spyglass</span></li>
<li><span style="font-size:18px"><strong>Soft Fluid System</strong> — data-driven virtual fluid system supporting bottles, bowls, buckets, stews, and drinks</span></li>
<li><span style="font-size:18px"><strong>Grindstone Trigger</strong> — custom advancement trigger for items passing through a grindstone</span></li>
<li><span style="font-size:18px"><strong>DispenserHelper</strong>, <strong>Global Datapack Folder</strong>, <strong>Debug Renderers</strong></span></li>
</ul>

<p><span style="font-size:18px">To import this library, go to the Files section and click <strong>"Copy Gradle Line"</strong>, then paste it into your <code>build.gradle</code>.</span></p>

<p style="text-align:center"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/separators/blue.png" alt="separator" width="1688" height="42"></p>

<p><span style="font-size:18px">Modding takes a lot of my time. If you like what I do and want to support me, you'll receive a custom <strong>Globe</strong> and/or <strong>Statue</strong> just for you — this also applies if you buy a server from Akliz using the code below.</span></p>

<p style="text-align:center"><a href="https://ko-fi.com/mehvahdjukaar"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/badges/kofi.png" alt="Ko-Fi"></a></p>

<p><span style="font-size:18px">Need a server? <strong>Akliz</strong> offers top-tier servers built for modded Minecraft, with a great community and support team.<br>Use code <strong>"supplementaries"</strong> to get <strong>20% off</strong> and support me at the same time!</span></p>

<p style="text-align:center"><a href="https://www.akliz.net/supplementaries"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/badges/akliz.png" alt="Akliz Server Hosting" width="640" height="150"></a></p>

<p style="text-align:center"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/separators/blue.png" alt="separator" width="1688" height="42"></p>

<p style="text-align:center">
<a href="https://www.curseforge.com/minecraft/mc-mods/supplementaries"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/supplementaries.gif" alt="Supplementaries" width="125" height="125"></a>
<a href="https://www.curseforge.com/minecraft/mc-mods/haunted-harvest"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/haunted-harvest.webp" alt="Haunted Harvest" width="125" height="125"></a>
<a href="https://www.curseforge.com/minecraft/mc-mods/snowy-spirit"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/snowy-spirit.webp" alt="Snowy Spirit" width="125" height="125"></a>
<a href="https://www.curseforge.com/minecraft/mc-mods/labels"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/labels.webp" alt="Storage Labels" width="125" height="125"></a>
<a href="https://www.curseforge.com/minecraft/mc-mods/goated"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/goated.webp" alt="Goated" width="125" height="125"></a>
<a href="https://www.curseforge.com/minecraft/mc-mods/mystical-oak-tree"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/mystical-oak-tree.webp" alt="Mystical Oak Tree" width="125" height="125"></a>
<a href="https://www.curseforge.com/minecraft/mc-mods/vista"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/vista.gif" alt="Vista" width="125" height="125"></a>
<a href="https://www.curseforge.com/minecraft/mc-mods/mmmmmmmmmmmm"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/mmmmmmmmmmmm.png" alt="MmmMmmMmmMmm" width="125" height="125"></a>
<a href="https://www.curseforge.com/minecraft/mc-mods/moyai"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/moyai.webp" alt="Moyai" width="125" height="125"></a>
<a href="https://www.curseforge.com/minecraft/mc-mods/just-enough-effect-descriptions-jeed"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/jeed.webp" alt="JEED" width="125" height="125"></a>
<a href="https://www.curseforge.com/minecraft/mc-mods/better-lily-pads"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/better-lily-pads.webp" alt="Better Lily Pads" width="125" height="125"></a>
<a href="https://www.curseforge.com/minecraft/mc-mods/advancement-frames"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/advancement-frames.png" alt="Advancement Frames" width="125" height="125"></a>
<a href="https://www.curseforge.com/minecraft/mc-mods/randomium-ore"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/randomium.webp" alt="Randomium" width="125" height="125"></a>
<a href="https://www.curseforge.com/minecraft/mc-mods/sleep-tight"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/sleep-tight.png" alt="Sleep Tight" width="125" height="125"></a>
<a href="https://www.curseforge.com/minecraft/mc-mods/polytone"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/polytone.png" alt="Polytone" width="125" height="125"></a>
<a href="https://www.curseforge.com/minecraft/mc-mods/heartstone"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/heartstone.webp" alt="Heartstone" width="125" height="125"></a>
<a href="https://www.curseforge.com/minecraft/mc-mods/map-atlases-forge"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/map-atlases.png" alt="Map Atlases" width="125" height="125"></a>
<a href="https://www.curseforge.com/minecraft/mc-mods/sawmill"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/sawmill.webp" alt="Universal Sawmill" width="125" height="125"></a>
<a href="https://www.curseforge.com/minecraft/mc-mods/amendments"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/amendments.gif" alt="Amendments" width="125" height="125"></a>
</p>
