---
name: "Smarter Farmers"
slug: smarter-farmers
separator: "assets/separators/smarter-farmers.png"
cf_slug: smarter-farmers-farmers-replant
mr_slug: smarter-farmers-farmers-replant
---

[BADGES]
[SEPARATOR]

## 📖 About 📖

Vanilla farmers are not good at farming. They ignore modded crops, replant whatever seed happens to be first in their inventory, trample their own farmland and give up on their task constantly.

Smarter Farmers rewrites that behaviour. Farmers now replant what they just harvested, understand crops from any mod, pick up a hoe before working, and generally act like someone who has held a job before.

It slots in on top of other mods that touch farmers: Smarter Farmers' logic always takes priority.

> **Remember to turn on mob griefing.** Farmers can't touch a single block without it.

[SEPARATOR]

## 🌾 What Farmers Can Now Do 🌾

- **Handle modded crops**: plant, harvest and replant crops from any mod
- **Replant sensibly**: they put back what they just harvested instead of grabbing the first seed in the bag
- **Fill in gaps intelligently**: with nothing to replant, they pick a crop based on what's growing around them, so no more lone carrot patch in the middle of your wheat field
- **Accept and pick up seeds** for those crops, while non-farmer villagers no longer hoard them
- **Equip a hoe** while harvesting, of a tier matching their villager level, and equip the seed they're about to plant
- **Stop trampling farmland**
- **Plant pumpkins and melons in a checkerboard**, and know better than to block an existing stem's air space
- **Work on modded farmland** through the `farmer_plantable_on` block tag, which by default includes things like Supplementaries' planter
- **Harvest crop-like blocks that aren't crops** through the `crop_replaceable` tag, covering Immersive Weathering's weeds and the big crop blocks from Overweight Farming and Hefty Crops
- **Survive sweet berry bushes**, which no longer hurt them

Their farm task also fails far less often, which makes the whole village feel less broken.

On top of that, **all villagers** now accept and breed with any modded food item you throw at them.

[SEPARATOR]

## 🔍 Debugging 🔍

The mod ships with debug renderers you can switch on in the configs to see exactly what a farmer is thinking: what it's targeting, what it plans to plant, and why it gave up.

[SEPARATOR]
[SUPPORT]
[SEPARATOR]
[OUR_MODS]
