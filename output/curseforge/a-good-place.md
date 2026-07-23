<p style="text-align:center">
<a href="https://discord.gg/qdKRTDf8Cv"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/badges/discord.svg" alt="Discord" height="56"></a>
<a href="https://patreon.com/mehvahdjukaar"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/badges/patreon.svg" alt="Patreon" height="56"></a>
<a href="https://www.twitter.com/Supplementariez"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/badges/twitter.svg" alt="Twitter" height="56"></a>
<a href="https://www.youtube.com/channel/UCOaLLgwzOdbH6rCI7izCptw"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/badges/youtube.svg" alt="YouTube" height="56"></a>
</p>

<p style="text-align:center"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/separators/green.png" alt="separator" width="1688" height="42"></p>

<p style="text-align:center"><span style="font-size:24px"><strong>📖 About 📖</strong></span></p>

<p><span style="font-size:18px">Placing a block in vanilla is instant and lifeless: one frame it isn't there, the next it is. A Good Place gives it a little animation, so blocks pop, slide or swing into place instead of just appearing.</span></p>

<p><span style="font-size:18px">It's client-side, it works on tile entities too, and it ships with a sensible default animation applied to most blocks out of the box. The interesting part is that the whole thing is driven by resource packs, so if you don't like how it looks you can change it, and if you want different blocks to animate differently you can do that too.</span></p>

<p style="text-align:center"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/separators/green.png" alt="separator" width="1688" height="42"></p>

<p style="text-align:center"><span style="font-size:24px"><strong>🖼️ Media 🖼️</strong></span></p>

<p style="text-align:center"><img src="https://i.imgur.com/oZwNaFD.gif" alt="Placement animation example"></p>

<p style="text-align:center"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/separators/green.png" alt="separator" width="1688" height="42"></p>

<p style="text-align:center"><span style="font-size:24px"><strong>🔧 Customization 🔧</strong></span></p>

<p><span style="font-size:18px">Everything is a resource pack. Open your resource pack folder and you'll find a pre-made sample pack with a <code>placement_animations</code> folder inside. Drop one or more JSON files in there: each one targets a set of blocks and gives them an animation.</span></p>

<p><span style="font-size:18px">An animation is four animations layered together: <strong>scale</strong>, <strong>translation</strong>, <strong>rotation</strong> and <strong>height scale</strong>. Each has an accompanying <code>_curve</code> value controlling how it eases, from linear at <code>0</code> to sharply front- or back-loaded as it approaches <code>1</code> or <code>-1</code>.</span></p>

<p><span style="font-size:18px">A minimal pop-in animation for stone:</span></p>

<pre><code>{
  "predicates": [
    {
      "predicate_type": "tag_match",
      "tag": "minecraft:stone"
    }
  ],
  "scale": 0.2,
  "scale_curve": 0.92
}</code></pre>

<p><span style="font-size:18px">Which blocks a file applies to is controlled by <code>predicates</code>, the same idea as vanilla's worldgen block predicates. You get <code>matching_blocks</code>, <code>matching_state</code>, <code>has_collision</code>, <code>is_double_block</code>, plus <code>not</code> and <code>any_of</code> to combine them. Files also have a <code>priority</code> so a more specific pack can override a general one.</span></p>

<p><span style="font-size:18px">The full field reference, including <code>restrict_direction</code>, <code>rotation_pivot</code>, <code>duration</code> and the optional <code>sound</code> to play on placement, is in the <a href="https://github.com/enjarai/a-good-place">mod's README and wiki</a>.</span></p>

<blockquote><p><span style="font-size:18px">You may need to enable the sample resource pack in your resource pack menu the first time you install the mod.</span></p></blockquote>

<p><span style="font-size:18px">Made something good? Share it with us on Discord.</span></p>

<p style="text-align:center"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/separators/green.png" alt="separator" width="1688" height="42"></p>

<p><span style="font-size:18px">Modding takes a lot of my time. If you like what I do and want to support me, you'll receive a custom <strong>Globe</strong> and/or <strong>Statue</strong> just for you - this also applies if you buy a server from Akliz using the code below.</span></p>

<p style="text-align:center"><a href="https://ko-fi.com/mehvahdjukaar"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/badges/kofi.png" alt="Ko-Fi"></a></p>

<p><span style="font-size:18px">Need a server? <strong>Akliz</strong> offers top-tier servers built for modded Minecraft, with a great community and support team.<br>Use code <strong>"supplementaries"</strong> to get <strong>20% off</strong> and support me at the same time!</span></p>

<p style="text-align:center"><a href="https://www.akliz.net/supplementaries"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/badges/akliz.png" alt="Akliz Server Hosting" width="640" height="150"></a></p>

<p style="text-align:center"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/separators/green.png" alt="separator" width="1688" height="42"></p>

<p style="text-align:center">
<a href="https://www.curseforge.com/minecraft/mc-mods/supplementaries"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/supplementaries.gif" alt="Supplementaries" width="125" height="125"></a>
<a href="https://www.curseforge.com/minecraft/mc-mods/amendments"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/amendments.gif" alt="Amendments" width="125" height="125"></a>
<a href="https://www.curseforge.com/minecraft/mc-mods/every-compat"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/every-compat.webp" alt="Every Compat (Wood Good)" width="125" height="125"></a>
<a href="https://www.curseforge.com/minecraft/mc-mods/supplementaries-squared"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/supp-squared.webp" alt="Supplementaries Squared" width="125" height="125"></a>
<a href="https://www.curseforge.com/minecraft/mc-mods/map-atlases-forge"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/map-atlases.png" alt="Map Atlases" width="125" height="125"></a>
<a href="https://www.curseforge.com/minecraft/mc-mods/sawmill"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/sawmill.webp" alt="Universal Sawmill" width="125" height="125"></a>
<a href="https://www.curseforge.com/minecraft/mc-mods/polytone"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/polytone.png" alt="Polytone" width="125" height="125"></a>
<a href="https://www.curseforge.com/minecraft/mc-mods/snowy-spirit"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/snowy-spirit.webp" alt="Snowy Spirit" width="125" height="125"></a>
<a href="https://www.curseforge.com/minecraft/mc-mods/haunted-harvest"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/haunted-harvest.webp" alt="Haunted Harvest" width="125" height="125"></a>
<a href="https://www.curseforge.com/minecraft/mc-mods/sleep-tight"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/sleep-tight.png" alt="Sleep Tight" width="125" height="125"></a>
<a href="https://www.curseforge.com/minecraft/mc-mods/smarter-farmers-farmers-replant"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/smarter-farmers.webp" alt="Smarter Farmers" width="125" height="125"></a>
<a href="https://www.curseforge.com/minecraft/mc-mods/mystical-oak-tree"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/mystical-oak-tree.webp" alt="Mystical Oak Tree" width="125" height="125"></a>
<a href="https://www.curseforge.com/minecraft/mc-mods/labels"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/labels.webp" alt="Storage Labels" width="125" height="125"></a>
<a href="https://www.curseforge.com/minecraft/mc-mods/goated"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/goated.webp" alt="Goated" width="125" height="125"></a>
<a href="https://www.curseforge.com/minecraft/mc-mods/vista"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/vista.gif" alt="Vista" width="125" height="125"></a>
<a href="https://www.curseforge.com/minecraft/mc-mods/heartstone"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/heartstone.webp" alt="Heartstone" width="125" height="125"></a>
<a href="https://www.curseforge.com/minecraft/mc-mods/fast-paintings"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/fast-paintings.png" alt="Fast Paintings" width="125" height="125"></a>
<a href="https://www.curseforge.com/minecraft/mc-mods/mmmmmmmmmmmm"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/mmmmmmmmmmmm.png" alt="MmmMmmMmmMmm" width="125" height="125"></a>
<a href="https://www.curseforge.com/minecraft/mc-mods/just-enough-effect-descriptions-jeed"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/jeed.webp" alt="JEED" width="125" height="125"></a>
<a href="https://www.curseforge.com/minecraft/mc-mods/advancement-frames"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/advancement-frames.png" alt="Advancement Frames" width="125" height="125"></a>
<a href="https://www.curseforge.com/minecraft/mc-mods/randomium-ore"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/randomium.webp" alt="Randomium" width="125" height="125"></a>
<a href="https://www.curseforge.com/minecraft/mc-mods/moyai"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/moyai.webp" alt="Moyai" width="125" height="125"></a>
</p>
