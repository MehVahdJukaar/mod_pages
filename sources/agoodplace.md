---
name: "A Good Place"
slug: a-good-place
separator: "assets/separators/green.png"
icon: "assets/mod_icons/a-good-place.webp"
cf_slug: a-good-place
mr_slug: a-good-place
---

[BADGES]
[SEPARATOR]

## 📖 About 📖

Placing a block in vanilla is instant and lifeless: one frame it isn't there, the next it is. A Good Place gives it a little animation, so blocks pop, slide or swing into place instead of just appearing.

It's client-side, it works on tile entities too, and it ships with a sensible default animation applied to most blocks out of the box. The interesting part is that the whole thing is driven by resource packs, so if you don't like how it looks you can change it, and if you want different blocks to animate differently you can do that too.

[SEPARATOR]

## 🖼️ Media 🖼️

![Placement animation example](https://i.imgur.com/oZwNaFD.gif)

[SEPARATOR]

## 🔧 Customization 🔧

Everything is a resource pack. Open your resource pack folder and you'll find a pre-made sample pack with a `placement_animations` folder inside. Drop one or more JSON files in there: each one targets a set of blocks and gives them an animation.

An animation is four animations layered together: **scale**, **translation**, **rotation** and **height scale**. Each has an accompanying `_curve` value controlling how it eases, from linear at `0` to sharply front- or back-loaded as it approaches `1` or `-1`.

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

Which blocks a file applies to is controlled by `predicates`, the same idea as vanilla's worldgen block predicates. You get `matching_blocks`, `matching_state`, `has_collision`, `is_double_block`, plus `not` and `any_of` to combine them. Files also have a `priority` so a more specific pack can override a general one.

The full field reference, including `restrict_direction`, `rotation_pivot`, `duration` and the optional `sound` to play on placement, is in the [mod's README and wiki](https://github.com/enjarai/a-good-place).

> You may need to enable the sample resource pack in your resource pack menu the first time you install the mod.

Made something good? Share it with us on Discord.

[SEPARATOR]
[SUPPORT]
[SEPARATOR]
[OUR_MODS]
