#!/usr/bin/env python3
"""
Generate CurseForge and Modrinth mod pages from source .md files.

Usage:
    python generate.py                      # regenerate all
    python generate.py sources/vista.md     # regenerate one mod
"""

import json
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("Error: PyYAML not found. Install with: pip install pyyaml")
    sys.exit(1)

ROOT = Path(__file__).parent


# ── Config & data loading ─────────────────────────────────────────────────────

def load_config():
    return json.loads((ROOT / "config.json").read_text())


def load_mods():
    data = json.loads((ROOT / "mods.json").read_text())
    return {m["slug"]: m for m in data["mods"]}


def parse_source(path):
    text = Path(path).read_text(encoding="utf-8")
    parts = text.split("---", 2)
    if len(parts) < 3:
        raise ValueError(f"No YAML frontmatter found in {path}")
    fm = yaml.safe_load(parts[1])
    body = parts[2].lstrip("\n")
    return fm, body


# ── URL helpers ───────────────────────────────────────────────────────────────

def github_raw(config, asset_path):
    u, r, b = config["github_user"], config["github_repo"], config["github_branch"]
    return f"https://raw.githubusercontent.com/{u}/{r}/{b}/{asset_path}"


def resolve_url(config, url_or_path):
    """Full URL → use as-is. Local path (no http) → GitHub raw URL."""
    if url_or_path and not str(url_or_path).startswith("http"):
        return github_raw(config, url_or_path)
    return url_or_path


# ── Placeholder expanders ─────────────────────────────────────────────────────

def expand_banner(config, fm, platform):
    if platform != "cf" or not fm.get("banner_url"):
        return ""
    url = fm["banner_url"]
    link = fm.get("banner_link", "")
    img = f'<img src="{url}" alt="{fm["name"]}" width="1519" height="855">'
    inner = f'<a href="{link}">{img}</a>' if link else img
    return f'<p style="text-align:center">\n  {inner}\n</p>'


def expand_badges(config, fm, platform):
    if platform != "cf":
        return ""
    s, b = config["social"], config["badge_images"]
    def img(key, label):
        url = resolve_url(config, b[key])
        return f'<a href="{s[key]}"><img src="{url}" alt="{label}" height="56"></a>'
    return (
        '<p style="text-align:center">\n'
        + img("discord", "Discord") + "\n"
        + img("patreon", "Patreon") + "\n"
        + img("twitter", "Twitter") + "\n"
        + img("youtube", "YouTube") + "\n"
        + "</p>"
    )


def expand_separator(config, fm):
    url = resolve_url(config, fm["separator"])
    return f'<p style="text-align:center"><img src="{url}" alt="separator" width="1688" height="42"></p>'


def expand_support(config, fm, platform):
    kofi_url = config["kofi"]["url"]
    kofi_img = resolve_url(config, config["kofi"]["image"])
    akliz = config["akliz"]
    # Per-mod akliz code from frontmatter overrides config default
    code = fm.get("akliz_code") or akliz["code"]
    akliz_base = akliz["url"].rsplit("/", 1)[0]
    akliz_url = f"{akliz_base}/{code}"
    akliz_img = resolve_url(config, akliz["image"])
    pct = akliz["discount_pct"]
    # Support text is in config so it can be swapped centrally
    raw_text = config.get("support_text", "")

    if platform == "cf":
        cf_text = md_to_cf_inline(raw_text)
        return "\n".join([
            f'<p><span style="font-size:18px">{cf_text}</span></p>',
            "",
            f'<p style="text-align:center"><a href="{kofi_url}"><img src="{kofi_img}" alt="Ko-Fi"></a></p>',
            "",
            f'<p><span style="font-size:18px">Need a server? <strong>Akliz</strong> offers top-tier servers built for modded Minecraft, '
            f'with a great community and support team.<br>'
            f'Use code <strong>"{code}"</strong> to get <strong>{pct}% off</strong> and support me at the same time!</span></p>',
            "",
            f'<p style="text-align:center"><a href="{akliz_url}"><img src="{akliz_img}" alt="Akliz Server Hosting" width="640" height="150"></a></p>',
        ])
    else:
        return "\n".join([
            raw_text,
            "",
            f'<p style="text-align:center"><a href="{kofi_url}"><img src="{kofi_img}" alt="Ko-Fi"></a></p>',
            "",
            f"Need a server? **Akliz** offers top-tier servers built for modded Minecraft, with a great community and support team.  ",
            f'Use code **"{code}"** to get **{pct}% off** and support me at the same time!',
            "",
            f'<p style="text-align:center"><a href="{akliz_url}"><img src="{akliz_img}" alt="Akliz Server Hosting" width="640" height="150"></a></p>',
        ])


def expand_our_mods(config, fm, all_mods, platform):
    slug = fm["slug"]
    lines = ['<p style="text-align:center">']
    for mod in all_mods.values():
        if mod["slug"] == slug or not mod.get("icon"):
            continue
        icon = resolve_url(config, mod["icon"])
        name = mod["name"]
        url = (
            f"https://www.curseforge.com/minecraft/mc-mods/{mod['cf_slug']}"
            if platform == "cf"
            else f"https://modrinth.com/mod/{mod['mr_slug']}"
        )
        lines.append(f'<a href="{url}"><img src="{icon}" alt="{name}" width="125" height="125"></a>')
    lines.append("</p>")
    return "\n".join(lines)


def expand_youtube(token, platform):
    m = re.match(r"\[YOUTUBE:\s*([^\]|]+?)(?:\s*\|\s*([^\]]+))?\]", token)
    if not m:
        return token
    vid_id = m.group(1).strip()
    caption = (m.group(2) or "").strip()
    iframe = (
        f'<p style="text-align:center">'
        f'<iframe src="https://www.youtube.com/embed/{vid_id}?wmode=transparent" '
        f'width="638" height="358" allowfullscreen="allowfullscreen"></iframe>'
        f"</p>"
    )
    if not caption:
        return iframe
    caption_line = (
        f'<p><span style="font-size:18px"><strong>{caption}:</strong></span></p>'
        if platform == "cf"
        else f"**{caption}:**"
    )
    return caption_line + "\n\n" + iframe


# ── Inline markdown → CF HTML ─────────────────────────────────────────────────

def md_to_cf_inline(text):
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"<em>\1</em>", text)
    text = re.sub(r"`(.+?)`", r"<code>\1</code>", text)
    text = re.sub(r"\[([^\]]+)\]\(([^\)]+)\)", r'<a href="\2">\1</a>', text)
    return text


def md_img_to_html(text):
    return re.sub(r"!\[([^\]]*)\]\(([^\)]+)\)", r'<img src="\2" alt="\1">', text)


# ── Block renderers ───────────────────────────────────────────────────────────

def render_h2(text, platform):
    if platform == "cf":
        return f'<p style="text-align:center"><span style="font-size:24px"><strong>{text}</strong></span></p>'
    return f'<h2 style="text-align:center">{text}</h2>'


def render_h3(text, platform):
    if platform == "cf":
        return f"<p><strong>{text}</strong></p>"
    return f"### {text}"


def render_list(items, platform):
    if platform == "cf":
        lis = "\n".join(
            f'<li><span style="font-size:18px">{md_to_cf_inline(item)}</span></li>'
            for item in items
        )
        return f"<ul>\n{lis}\n</ul>"
    return "\n".join(f"- {item}" for item in items)


def render_ordered_list(items, platform):
    if platform == "cf":
        lis = "\n".join(
            f'<li><span style="font-size:18px">{md_to_cf_inline(item)}</span></li>'
            for item in items
        )
        return f"<ol>\n{lis}\n</ol>"
    return "\n".join(f"{idx + 1}. {item}" for idx, item in enumerate(items))


def render_paragraph(text, platform):
    if platform == "cf":
        return f'<p><span style="font-size:18px">{md_to_cf_inline(text)}</span></p>'
    return text


def render_blockquote(text, platform):
    if platform == "cf":
        return f'<blockquote><p><span style="font-size:18px">{md_to_cf_inline(text)}</span></p></blockquote>'
    return f"> {text}"


# ── <details> / spoiler blocks ────────────────────────────────────────────────

def parse_details_block(lines, start):
    """Parse <details>...</details> starting at index `start`.
    Returns (summary, content_lines, next_index)."""
    summary = ""
    content_lines = []
    i = start + 1
    while i < len(lines):
        s = lines[i].strip()
        if s == "</details>":
            return summary, content_lines, i + 1
        m = re.match(r"<summary>(.*?)</summary>", s)
        if m:
            summary = m.group(1)
        else:
            content_lines.append(lines[i])
        i += 1
    return summary, content_lines, i


def render_details(summary, content_lines, platform):
    if platform == "mr":
        body = "\n".join(content_lines)
        return f"<details>\n<summary>{summary}</summary>\n{body}\n</details>"
    # CF: bold label + spoiler div (handles images, code blocks, and text)
    processed = []
    in_pre = False
    for cl in content_lines:
        s = cl.strip()
        if not s and not in_pre:
            continue
        if "<pre" in s:
            in_pre = True
        if in_pre or s.startswith("<"):
            processed.append(cl)
        elif s.startswith("!["):
            processed.append(md_img_to_html(s))
        else:
            processed.append(f'<span style="font-size:18px">{md_to_cf_inline(s)}</span>')
        if "</pre" in s:
            in_pre = False
    inner = "\n".join(processed)
    return (
        f'<p><span style="font-size:18px"><strong>{summary}:</strong></span></p>\n'
        f'<div class="spoiler">{inner}</div>'
    )


# ── Main body processor ───────────────────────────────────────────────────────

def preprocess_dependency(body, fm, platform):
    dep = fm.get("dependency")
    if not dep:
        return body
    name = dep["name"]
    url = (
        f"https://www.curseforge.com/minecraft/mc-mods/{dep['cf_slug']}"
        if platform == "cf"
        else f"https://modrinth.com/mod/{dep['mr_slug']}"
    )
    return body.replace("[DEPENDENCY]", f"[{name}]({url})")


def process_body(body, platform, config, fm, all_mods):
    body = preprocess_dependency(body, fm, platform)
    lines = body.split("\n")
    out = []
    i = 0

    while i < len(lines):
        line = lines[i]
        s = line.strip()

        if s == "":
            out.append("")
            i += 1
            continue

        # ── Placeholders ──────────────────────────────────────────────────────
        if s == "[SEPARATOR]":
            out.append(expand_separator(config, fm))
            out.append("")
            i += 1
            continue

        if s == "[BADGES]":
            html = expand_badges(config, fm, platform)
            if html:
                out.append(html)
                out.append("")
            i += 1
            continue

        if s == "[BANNER]":
            html = expand_banner(config, fm, platform)
            if html:
                out.append(html)
                out.append("")
            i += 1
            continue

        if s.startswith("[YOUTUBE:"):
            out.append("")
            out.append(expand_youtube(s, platform))
            out.append("")
            i += 1
            continue

        if s == "[SUPPORT]":
            out.append(expand_support(config, fm, platform))
            out.append("")
            i += 1
            continue

        if s == "[OUR_MODS]":
            out.append(expand_our_mods(config, fm, all_mods, platform))
            out.append("")
            i += 1
            continue

        # ── Headings ──────────────────────────────────────────────────────────
        if s.startswith("## "):
            out.append("")
            out.append(render_h2(s[3:], platform))
            out.append("")
            i += 1
            continue

        if s.startswith("### "):
            out.append("")
            out.append(render_h3(s[4:], platform))
            out.append("")
            i += 1
            continue

        # ── Blockquote ────────────────────────────────────────────────────────
        if s.startswith("> "):
            out.append(render_blockquote(s[2:], platform))
            out.append("")
            i += 1
            continue

        # ── <details> spoiler block ───────────────────────────────────────────
        if s == "<details>":
            summary, content_lines, next_i = parse_details_block(lines, i)
            out.append(render_details(summary, content_lines, platform))
            out.append("")
            i = next_i
            continue

        # ── List items (consecutive) ──────────────────────────────────────────
        if s.startswith("- ") or s.startswith("* "):
            items = []
            while i < len(lines) and (
                lines[i].strip().startswith("- ") or lines[i].strip().startswith("* ")
            ):
                items.append(lines[i].strip()[2:])
                i += 1
            out.append(render_list(items, platform))
            out.append("")
            continue

        # ── Ordered list (consecutive) ────────────────────────────────────────
        if re.match(r"^\d+\. ", s):
            items = []
            while i < len(lines) and re.match(r"^\d+\. ", lines[i].strip()):
                items.append(re.sub(r"^\d+\. ", "", lines[i].strip()))
                i += 1
            out.append(render_ordered_list(items, platform))
            out.append("")
            continue

        # ── Standalone markdown image ─────────────────────────────────────────
        if s.startswith("!["):
            if platform == "cf":
                out.append(f'<p style="text-align:center">{md_img_to_html(s)}</p>')
            else:
                out.append(s)
            out.append("")
            i += 1
            continue

        # ── Raw HTML (pass through unchanged) ────────────────────────────────
        if s.startswith("<"):
            out.append(line)
            i += 1
            continue

        # ── Regular paragraph ─────────────────────────────────────────────────
        out.append(render_paragraph(s, platform))
        out.append("")
        i += 1

    # Collapse runs of blank lines to a single blank line
    result = []
    prev_blank = False
    for ln in out:
        if ln.strip() == "":
            if not prev_blank:
                result.append("")
            prev_blank = True
        else:
            result.append(ln)
            prev_blank = False

    return "\n".join(result).strip()


# ── Top-level generator ───────────────────────────────────────────────────────

def generate_mod(source_path, config, all_mods):
    fm, body = parse_source(source_path)
    slug = fm["slug"]
    print(f"  {slug}")
    for platform, key in [("curseforge", "cf"), ("modrinth", "mr")]:
        result = process_body(body, key, config, fm, all_mods)
        out_path = ROOT / "output" / platform / f"{slug}.md"
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(result + "\n", encoding="utf-8")


def main():
    config = load_config()
    all_mods = load_mods()

    sources = (
        [Path(p) for p in sys.argv[1:]]
        if len(sys.argv) > 1
        else sorted((ROOT / "sources").glob("*.md"))
    )

    if not sources:
        print("No source files found.")
        sys.exit(1)

    print("Generating pages...")
    for src in sources:
        generate_mod(Path(src), config, all_mods)
    print(f"Done. {len(sources)} mod(s) processed.")


if __name__ == "__main__":
    main()
