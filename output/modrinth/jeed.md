<p style="text-align:center"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/separators/jeed.png" alt="separator" width="1688" height="42"></p>

<h2 style="text-align:center">📖 About 📖</h2>

JEED is a JEI, REI and EMI plugin that adds an **Effects** recipe category, giving every status effect a proper information panel.

Open it by clicking a status effect icon in the recipe viewer, or an active effect box on the inventory screen. Each entry lists which items provide the effect, what it does, which mod adds it, and its color.

<p style="text-align:center"><img src="https://i.imgur.com/P8qv5ZN.png" alt="JEED screenshot" width="600" height="313"> <img src="https://i.imgur.com/UfGgoGG.png" alt="JEED screenshot 2" width="600" height="313"></p>

<p style="text-align:center"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/separators/jeed.png" alt="separator" width="1688" height="42"></p>

<h2 style="text-align:center">🧪 Features 🧪</h2>

- Every registered status effect is picked up automatically, modded ones included
- Modded effects have no description until someone writes one, which any resource pack can do
- Add the key `effect.[mod_id].[effect_name].description` to a language file
- Modders can use the `JeedAPI` class to register screen extensions for custom GUIs, or to tell JEED where effects are rendered so they become clickable
- For effects or effect-providing items JEED cannot detect, add one of these recipe types:

<details>
<summary>jeed:effect_provider - link an item to an effect it provides</summary>
<pre><code>{
  "type": "jeed:effect_provider",
  "effect": "minecraft:haste",
  "providers": [
    { "item": "minecraft:beacon" }
  ]
}</code></pre>
Also supports `"fluid_providers"` and `"effect_providers"` (tags or lists of fluids/effects).
</details>

<details>
<summary>jeed:potion_provider - mark an item as a potion container (like tipped arrows)</summary>
<pre><code>{
  "type": "jeed:potion_provider",
  "providers": [
    { "item": "minecraft:splash_potion" },
    { "item": "minecraft:tipped_arrow" }
  ]
}</code></pre>
</details>

If you'd like to help add built-in descriptions for common modded effects, reach out on Discord!

<p style="text-align:center"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/separators/jeed.png" alt="separator" width="1688" height="42"></p>

<h2 style="text-align:center">❤️ Support Me ❤️</h2>

Modding takes a lot of my time. If you like what I do and want to support me, you'll receive a custom **Globe** and/or **Statue** just for you - this also applies if you buy a server from Akliz using the code below.

<p style="text-align:center"><a href="https://ko-fi.com/mehvahdjukaar"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/badges/kofi.png" alt="Ko-Fi"></a></p>

Need a server? **Akliz** offers top-tier servers built for modded Minecraft, with a great community and support team.  
Use code **"supplementaries"** to get **20% off** and support me at the same time!

<p style="text-align:center"><a href="https://www.akliz.net/supplementaries"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/badges/akliz.png" alt="Akliz Server Hosting" width="640" height="150"></a></p>

<p style="text-align:center"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/separators/jeed.png" alt="separator" width="1688" height="42"></p>

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
<a href="https://modrinth.com/mod/advancement-frames"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/advancement-frames.png" alt="Advancement Frames" width="125" height="125"></a>
<a href="https://modrinth.com/mod/randomium-ore"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/randomium.png" alt="Randomium" width="125" height="125"></a>
<a href="https://modrinth.com/mod/moyai"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/moyai.png" alt="Moyai" width="125" height="125"></a>
</p>
