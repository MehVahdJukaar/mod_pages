---
name: "Just Enough Effect Descriptions (JEED)"
slug: jeed
separator: "assets/separators/jeed.png"
cf_slug: just-enough-effect-descriptions-jeed
mr_slug: just-enough-effect-descriptions-jeed
akliz_code: supplementaries
---

[BADGES]
[SEPARATOR]

## 📖 About 📖

Just Enough Effect Descriptions (JEED) is a JEI/REI/EMI plugin that gives status effects a proper information panel.

The mod adds a new **Effects** recipe category. You can access it by clicking any of the status effect icons on the JEI item screen, or by clicking an active effect box on the inventory screen.

Inside you'll find: which items provide the effect, a description of what it does, what mod it comes from, and its effect color.

<p style="text-align:center"><img src="https://i.imgur.com/P8qv5ZN.png" alt="JEED screenshot" width="600" height="313"> <img src="https://i.imgur.com/UfGgoGG.png" alt="JEED screenshot 2" width="600" height="313"></p>

[SEPARATOR]

## 🧪 Customization 🧪

JEED automatically picks up all registered status effects. Modded effects won't have a description by default, but anyone can add one.

**Adding descriptions**: add this key to your language file or resource pack:

`effect.[mod_id].[effect_name].description`

This is something modders can do directly in their mod, or players can do via a resource pack.

**JeedAPI**: modders can use the `JeedAPI` class to register screen extensions for custom GUIs, or tell JEED where effects are rendered so they become clickable.

**Recipe support**: if your mod has custom effects or effect-providing items that JEED can't detect automatically, add one of these recipe types:

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

[SEPARATOR]
[SUPPORT]
[SEPARATOR]
[OUR_MODS]
