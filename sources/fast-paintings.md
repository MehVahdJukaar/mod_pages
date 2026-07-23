---
name: "Fast Paintings"
slug: fast-paintings
separator: "assets/separators/fast-paintings.png"
cf_slug: fast-paintings
mr_slug: fast-paintings
---

[BADGES]
[SEPARATOR]

## 📖 About 📖

Fast Paintings replaces painting entities with blocks, rendered as baked models instead of through an entity renderer. This removes their rendering and tick cost, and fixes several long-standing painting quirks along the way.

Because paintings are now blocks with JSON models, resource packs can also change their shape.

[SEPARATOR]

## ⚡ Features ⚡

- Paintings render as cheaply as any other block, with no entity tick overhead
- No longer disappear at a distance
- Mipmap support, so they look better far away
- React immediately when their supporting block is broken
- Cannot be destroyed by the `/kill` command
- Still walk-through, so secret doors behind paintings keep working

[SEPARATOR]

## 🖼️ Customization 🖼️

- Each painting part (`top_left`, `top_right` and so on) has its own model JSON that a resource pack can replace
- Any geometry works, so frames, borders and rounded corners are all possible

**Framed Paintings** is a pack that already does this:

<p style="text-align:center"><a href="https://www.curseforge.com/minecraft/texture-packs/framed-paintings-fast-paintings-custom-model"><img src="https://media.forgecdn.net/avatars/955/46/638446800683802696.png" alt="Framed Paintings texture pack" width="200" height="200"></a></p>

[SEPARATOR]
[SUPPORT]
[SEPARATOR]
[OUR_MODS]
