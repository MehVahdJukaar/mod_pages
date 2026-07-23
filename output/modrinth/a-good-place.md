<p style="text-align:center"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/separators/a-good-place.png" alt="separator" width="1688" height="42"></p>

<h2 style="text-align:center">📖 About 📖</h2>

A Good Place adds a short animation when a block is placed, so blocks slide, pop or swing into position instead of appearing instantly.

It is client-side, works on block entities, and ships with a default animation applied to most blocks. The whole system is driven by resource packs, so the animation can be changed or given different settings per block.

<p style="text-align:center"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/separators/a-good-place.png" alt="separator" width="1688" height="42"></p>

<h2 style="text-align:center">🖼️ Media 🖼️</h2>

![Placement animation example](https://i.imgur.com/oZwNaFD.gif)

<p style="text-align:center"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/separators/a-good-place.png" alt="separator" width="1688" height="42"></p>

<h2 style="text-align:center">🔧 Features 🔧</h2>

- A pre-made sample pack is placed in your resource pack folder on first launch
- Animations are JSON files in a `placement_animations` folder, each targeting a set of blocks
- Every animation layers four parts: **scale**, **translation**, **rotation** and **height scale**
- Each part has a `_curve` value setting how it eases, from linear at `0` to sharply front- or back-loaded near `1` and `-1`
- Which blocks a file applies to is set by `predicates`, working like vanilla's worldgen block predicates: `matching_blocks`, `matching_state`, `has_collision` and `is_double_block`, combined with `not` and `any_of`
- A `priority` field lets a specific pack override a general one
- The full field reference, including `restrict_direction`, `rotation_pivot`, `duration` and an optional `sound`, is in the [mod's README](https://github.com/enjarai/a-good-place)

A minimal pop-in animation for stone:

```json
{
  "predicates": [
    {
      "predicate_type": "tag_match",
      "tag": "minecraft:stone"
    }
  ],
  "scale": 0.2,
  "scale_curve": 0.92
}
```

> You may need to enable the sample resource pack in the resource pack menu the first time you install the mod.

<p style="text-align:center"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/separators/a-good-place.png" alt="separator" width="1688" height="42"></p>

<h2 style="text-align:center">❤️ Support Me ❤️</h2>

Modding takes a lot of my time. If you like what I do and want to support me, you'll receive a custom **Globe** and/or **Statue** just for you - this also applies if you buy a server from Akliz using the code below.

<p style="text-align:center"><a href="https://ko-fi.com/mehvahdjukaar"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/badges/kofi.png" alt="Ko-Fi"></a></p>

Need a server? **Akliz** offers top-tier servers built for modded Minecraft, with a great community and support team.  
Use code **"supplementaries"** to get **20% off** and support me at the same time!

<p style="text-align:center"><a href="https://www.akliz.net/supplementaries"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/badges/akliz.png" alt="Akliz Server Hosting" width="640" height="150"></a></p>

<p style="text-align:center"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/separators/a-good-place.png" alt="separator" width="1688" height="42"></p>

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
<a href="https://modrinth.com/mod/vista"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/vista.gif" alt="Vista" width="125" height="125"></a>
<a href="https://modrinth.com/mod/heartstone"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/heartstone.gif" alt="Heartstone" width="125" height="125"></a>
<a href="https://modrinth.com/mod/fast-paintings"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/fast-paintings.png" alt="Fast Paintings" width="125" height="125"></a>
<a href="https://modrinth.com/mod/mmmmmmmmmmmm"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/mmmmmmmmmmmm.png" alt="MmmMmmMmmMmm" width="125" height="125"></a>
<a href="https://modrinth.com/mod/just-enough-effect-descriptions-jeed"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/jeed.png" alt="JEED" width="125" height="125"></a>
<a href="https://modrinth.com/mod/advancement-frames"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/advancement-frames.png" alt="Advancement Frames" width="125" height="125"></a>
<a href="https://modrinth.com/mod/randomium-ore"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/randomium.png" alt="Randomium" width="125" height="125"></a>
<a href="https://modrinth.com/mod/moyai"><img src="https://raw.githubusercontent.com/MehVahdJukaar/mod_pages/master/assets/mod_icons/moyai.png" alt="Moyai" width="125" height="125"></a>
</p>
