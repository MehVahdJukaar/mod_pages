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

JEED is a JEI, REI and EMI plugin that adds an **Effects** recipe category, giving every status effect a proper information panel.

Open it by clicking a status effect icon in the recipe viewer, or an active effect box on the inventory screen. Each entry lists which items provide the effect, what it does, which mod adds it, and its color.

<p style="text-align:center"><img src="https://i.imgur.com/P8qv5ZN.png" alt="JEED screenshot" width="600" height="313"> <img src="https://i.imgur.com/UfGgoGG.png" alt="JEED screenshot 2" width="600" height="313"></p>

[SEPARATOR]

## 🧪 Features 🧪

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

[SEPARATOR]
[SUPPORT]
[SEPARATOR]
[OUR_MODS]
