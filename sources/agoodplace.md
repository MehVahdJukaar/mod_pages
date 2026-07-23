---
name: "A Good Place"
slug: a-good-place
separator: "assets/separators/a-good-place.png"
cf_slug: a-good-place
mr_slug: a-good-place
---

[BADGES]
[SEPARATOR]

## 📖 About 📖

A Good Place adds a short animation when a block is placed, so blocks slide, pop or swing into position instead of appearing instantly.

It is client-side, works on block entities, and ships with a default animation applied to most blocks. The whole system is driven by resource packs, so the animation can be changed or given different settings per block.

[SEPARATOR]

## 🖼️ Media 🖼️

![Placement animation example](https://i.imgur.com/oZwNaFD.gif)

[SEPARATOR]

## 🔧 Features 🔧

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

[SEPARATOR]
[SUPPORT]
[SEPARATOR]
[OUR_MODS]
