#!/usr/bin/env python3
"""
Generate one separator per mod, colored from that mod's own icon.

Usage:
    python assets/separators/make_separators.py            # all mods in mods.json
    python assets/separators/make_separators.py vista       # just these slugs

Writes assets/separators/<slug>.png for every mod. A mod can pin its colors with
"separator_colors": ["edge_hex", "center_hex"] in mods.json, which skips extraction.
"""

import colorsys
import json
import sys
from collections import defaultdict
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    sys.exit("Pillow is required: pip install Pillow")

from make_separator import WIDTH, HEIGHT, build_gradient, hex_to_rgb

ROOT = Path(__file__).resolve().parents[2]
ICONS = ROOT / "assets" / "mod_icons"
OUT = ROOT / "assets" / "separators"

HUE_BINS = 18

# The bar sits behind text on both light and dark page backgrounds, so extracted
# colors get pushed into a fixed band rather than used raw. Keeps the set looking
# like a family instead of 26 unrelated smudges.
MIN_SAT, MAX_SAT = 0.45, 0.95
EDGE_VALUE, CENTER_VALUE = 0.52, 0.92

# A second hue is only worth using if it's a neighbour of the first. Letting the
# gradient travel halfway around the wheel turns the bar into a rainbow smear.
MIN_HUE_DISTANCE, MAX_HUE_DISTANCE = 1, 2


def to_hex(rgb):
    return "%02x%02x%02x" % rgb


def icon_path(slug, mod):
    """Prefer <slug>.png: the animated gifs some mods use sample badly."""
    png = ICONS / f"{slug}.png"
    if png.exists():
        return png
    icon = mod.get("icon")
    return ROOT / icon if icon else None


def dominant_hues(path):
    """Two dominant hues from an icon, weighted by how much colored area each covers.

    Grays, near-blacks and near-whites are dropped first: almost every Minecraft
    icon has a dark outline that would otherwise win by pixel count alone.
    """
    img = Image.open(path).convert("RGBA")
    img.thumbnail((96, 96))

    weight = defaultdict(float)
    sat_sum = defaultdict(float)
    val_sum = defaultdict(float)

    for r, g, b, a in img.getdata():
        if a < 128:
            continue
        h, s, v = colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)
        if s < 0.22 or v < 0.18 or (v > 0.97 and s < 0.12):
            continue
        # Saturation-weighted so a small vivid accent can outrank a large muddy area
        w = s * s
        b_idx = int(h * HUE_BINS) % HUE_BINS
        weight[b_idx] += w
        sat_sum[b_idx] += s * w
        val_sum[b_idx] += v * w

    if not weight:
        return None

    ranked = sorted(weight, key=lambda k: weight[k], reverse=True)

    def bin_hsv(b_idx):
        w = weight[b_idx]
        return (b_idx + 0.5) / HUE_BINS, sat_sum[b_idx] / w, val_sum[b_idx] / w

    primary = bin_hsv(ranked[0])

    secondary = None
    for b_idx in ranked[1:]:
        dist = abs(b_idx - ranked[0])
        dist = min(dist, HUE_BINS - dist)
        if MIN_HUE_DISTANCE <= dist <= MAX_HUE_DISTANCE and weight[b_idx] > weight[ranked[0]] * 0.15:
            secondary = bin_hsv(b_idx)
            break

    return primary, secondary


def normalize(hsv, value):
    h, s, _ = hsv
    return colorsys.hsv_to_rgb(h, min(max(s, MIN_SAT), MAX_SAT), value)


def colors_for(slug, mod):
    pinned = mod.get("separator_colors")
    if pinned:
        return pinned[0].lstrip("#"), pinned[1].lstrip("#")

    path = icon_path(slug, mod)
    if not path or not path.exists():
        return None

    found = dominant_hues(path)
    if not found:
        return None
    primary, secondary = found

    # With one usable hue, the gradient runs dark-to-bright within it instead
    edge_hsv = secondary or primary
    edge = normalize(edge_hsv, EDGE_VALUE)
    center = normalize(primary, CENTER_VALUE)
    return (
        to_hex(tuple(int(c * 255) for c in edge)),
        to_hex(tuple(int(c * 255) for c in center)),
    )


def main():
    mods = json.loads((ROOT / "mods.json").read_text())["mods"]
    wanted = set(sys.argv[1:])

    for mod in mods:
        slug = mod["slug"]
        if wanted and slug not in wanted:
            continue

        result = colors_for(slug, mod)
        if not result:
            print(f"  {slug}: no icon to sample, skipped")
            continue
        edge, center = result

        img = Image.new("RGB", (WIDTH, HEIGHT))
        img.putdata(build_gradient(edge, center) * HEIGHT)
        img.save(OUT / f"{slug}.png")
        print(f"  {slug}: #{edge} -> #{center}")


if __name__ == "__main__":
    main()
