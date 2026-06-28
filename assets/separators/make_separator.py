#!/usr/bin/env python3
"""
Generate a symmetric HSV gradient separator image.

Usage:
    python make_separator.py <name> <edge_hex> <center_hex>

Example:
    python make_separator.py cyan ff6a00 00c3ff

Output: assets/separators/<name>.png  (3834×94 px, matching existing separators)
"""

import sys
import colorsys
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    sys.exit("Pillow is required: pip install Pillow")


WIDTH = 3834
HEIGHT = 94


def hex_to_rgb(h: str) -> tuple[int, int, int]:
    h = h.lstrip("#")
    return int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)


def rgb_to_hsv(r, g, b):
    return colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)


def hsv_to_rgb_int(h, s, v):
    r, g, b = colorsys.hsv_to_rgb(h, s, v)
    return int(r * 255), int(g * 255), int(b * 255)


def lerp(a, b, t):
    return a + (b - a) * t


def lerp_angle(a, b, t):
    """Interpolate hue angles (0-1) taking the short path around the circle."""
    diff = b - a
    if diff > 0.5:
        diff -= 1.0
    elif diff < -0.5:
        diff += 1.0
    return (a + diff * t) % 1.0


def build_gradient(edge_hex: str, center_hex: str) -> list[tuple[int, int, int]]:
    eh, es, ev = rgb_to_hsv(*hex_to_rgb(edge_hex))
    ch, cs, cv = rgb_to_hsv(*hex_to_rgb(center_hex))

    half = WIDTH // 2
    pixels = []

    for x in range(WIDTH):
        # t goes 0 (edge) → 1 (center) → 0 (edge)
        if x < half:
            t = x / (half - 1)
        else:
            t = (WIDTH - 1 - x) / (half - 1)

        h = lerp_angle(eh, ch, t)
        s = lerp(es, cs, t)
        v = lerp(ev, cv, t)
        pixels.append(hsv_to_rgb_int(h, s, v))

    return pixels


def main():
    if len(sys.argv) != 4:
        sys.exit("Usage: python make_separator.py <name> <edge_hex> <center_hex>")

    name = sys.argv[1]
    edge_hex = sys.argv[2].lstrip("#")
    center_hex = sys.argv[3].lstrip("#")

    row = build_gradient(edge_hex, center_hex)
    img = Image.new("RGB", (WIDTH, HEIGHT))
    pixels = row * HEIGHT
    img.putdata(pixels)

    out = Path(__file__).parent / f"{name}.png"
    img.save(out)
    print(f"Saved: {out}  ({WIDTH}×{HEIGHT} px)")


if __name__ == "__main__":
    main()
