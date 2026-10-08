#!/usr/bin/env python3
"""One-off converter: rewrites claat-generated Google Codelab pages
(index.html + redirect.md) into standard just-the-docs markdown pages.

Run from the repo root:  python3 codelab2md.py
"""
import re
import os
import html as htmllib
import html as hm
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(".")

# Codelab *sources* (exported index.html + codelab.json) live outside docs/ so
# Jekyll never serves them. Each codelab's page is a <name>.md file inside its
# own docs/ folder, e.g. docs/devcontainer/new-accounts/new-accounts.md, with
# its images in a sibling img/ folder.
SRC_ROOT = Path("codelab-sources")

# --- Codelab metadata -------------------------------------------------------
# dir -> (title, parent, grand_parent, nav_order, redirect target,
#         intro (or None), duration_minutes (or None))
META = {
    "computing/jetstream2": (
        "ACCESS via Jetstream2", "External Sources", "Computing Resources", 1,
        "/docs/computing/external-sources#nsf-access-program",
        "Follow this tutorial to learn how to use the Jetstream2 supercomputing "
        "facilities with your ACCESS credits. Learn to navigate Jetstream2's "
        "interface, set up VS Code, and use development containers inside "
        "Jetstream2!", None),
    "devcontainer/new-accounts": (
        "PSTAT User Account Sign-up", "Develop in Container", None, 0,
        "/docs/devcontainer#setup", None, None),
    "devcontainer/new-devices": (
        "New Device Access", "Develop in Container", None, 1,
        "/docs/devcontainer#setup", None, None),
    "devcontainer/basic-usage": (
        "Basic Container Usage on a Server", "Develop in Container", None, 2,
        "/docs/devcontainer#setup", None, None),
    "devcontainer/container-management": (
        "Container Management", "Develop in Container", None, 4,
        "/docs/devcontainer#management", None, None),
    "devcontainer/file-management": (
        "File Management", "Develop in Container", None, 5,
        "/docs/devcontainer#management", None, None),
    "devcontainer/job-management": (
        "Job Management", "Develop in Container", None, 6,
        "/docs/devcontainer#management", None, None),
    "devcontainer/editing-dockerfile": (
        "Editing Dockerfile", "Develop in Container", None, 7,
        "/docs/devcontainer#additional-features", None, None),
    "devcontainer/github-codespaces": (
        "GitHub Codespaces", "Develop in Container", None, 8,
        "/docs/devcontainer#additional-features", None, None),
    "devcontainer/troubleshooting": (
        "Troubleshooting Common Issues", "Develop in Container", None, 9,
        "/docs/devcontainer#setup", None, None),
    "department/printer-driver-win": (
        "Installing Windows Printer Drivers", "Department Management", None, 1,
        "/docs/department#drivers",
        "Use this guide to install the Kyocera printer drivers on a Windows machine.", None),
    "department/printer-driver-mac": (
        "Installing MacOS Printer Drivers", "Department Management", None, 2,
        "/docs/department#drivers",
        "Use this guide to install the Kyocera printer drivers on a MacOS machine.", None),
    "department/printer-use": (
        "Using the Printer", "Department Management", None, 2,
        "/docs/department#printing", None, None),
    "container-workshop": (
        "Container Workshop (June 2024)", "Container Workshop", None, 1,
        "https://ucsbcarpentry.github.io/workshop/2024/06/04/ucsb-containers.html",
        "Materials from the June 2024 Container-Driven Reproducible Research "
        "Computing workshop hosted by the PSTAT department.", 120),
    "container-workshop-w2025": (
        "Container Workshop (February 2025)", "Container Workshop", None, 2,
        "https://ucsbcarpentry.github.io/workshop/2025/02/05/ucsb-containers.html",
        "Materials from the February 2025 Container-Driven Reproducible Research "
        "Computing workshop hosted by the PSTAT department.", 145),
}

# Steps whose body already contains an internal `<h2>` title matching the
# step label; the step label heading is skipped for these.
SKIP_STEP_LABEL = set()

# Old absolute links (old site domain) -> new permalinks (most specific first).
# URLs that lost their host (https:///docs/...) become site-root relative
def fix_urls(text: str) -> str:
    return text.replace("https:///docs", "/docs")


REPLACEMENTS = [
    # codelab step anchors: "#N" referred to step N-1 (Introduction == step 0)
    ("computing.pstat.ucsb.edu/docs/devcontainer/basic-usage/#2", "/docs/devcontainer/basic-usage/#connecting-to-a-server"),
    ("computing.pstat.ucsb.edu/docs/devcontainer/basic-usage/#6", "/docs/devcontainer/basic-usage/#using-github"),
    ("computing.pstat.ucsb.edu/docs/devcontainer/new-accounts/#1", "/docs/devcontainer/new-accounts/#generating-keys--windows"),
    ("computing.pstat.ucsb.edu/docs/devcontainer/new-accounts/#2", "/docs/devcontainer/new-accounts/#generating-keys--macoslinux"),
    # codelab permalinks
    ("computing.pstat.ucsb.edu/docs/computing#remote-computing-sources", "/docs/computing#remote-computing-sources"),
    ("computing.pstat.ucsb.edu/docs/devcontainer/new-devices//", "/docs/devcontainer/new-devices/"),
    ("computing.pstat.ucsb.edu/docs/devcontainer/new-devices/", "/docs/devcontainer/new-devices/"),
    ("computing.pstat.ucsb.edu/docs/devcontainer/new-accounts/", "/docs/devcontainer/new-accounts/"),
    ("computing.pstat.ucsb.edu/docs/devcontainer/basic-usage/", "/docs/devcontainer/basic-usage/"),
    ("computing.pstat.ucsb.edu/docs/devcontainer/file-management/", "/docs/devcontainer/file-management/"),
    ("computing.pstat.ucsb.edu/docs/devcontainer/job-management/", "/docs/devcontainer/job-management/"),
    ("computing.pstat.ucsb.edu/docs/devcontainer/vscode-setup/", "/docs/devcontainer/basic-usage/"),
    ("computing.pstat.ucsb.edu/docs/devcontainer#additional-features", "/docs/devcontainer#additional-features"),
    ("computing.pstat.ucsb.edu/docs/devcontainer#management", "/docs/devcontainer#management"),
    ("computing.pstat.ucsb.edu/docs/devcontainer#develop-in-container", "/docs/devcontainer"),
    ("computing.pstat.ucsb.edu/docs/department.html#printing", "/docs/department#printing"),
]

# --- HTML -> Markdown helpers ------------------------------------------------

def clean_text(t: str) -> str:
    t = htmllib.unescape(t)
    t = t.replace("\xa0", " ")
    t = re.sub(r"\s*\n\s*", " ", t)
    t = re.sub(r"  +", " ", t)
    return t.strip()


def strip_inline_tags(t: str) -> str:
    return re.sub(r"<[^>]+>", "", t)


def links_to_md(t: str) -> str:
    def conv(m):
        text = clean_text(m.group(2))
        if not text:
            return ""  # link with only a dropped entity (e.g. &#34;) -> nothing
        href = m.group(1)
        # URLs that lost their host are made site-root relative
        if href.startswith("https:///"):
            href = href[len("https:"):]
        # old domain URLs become site-root relative
        href = href.replace("https://computing.pstat.ucsb.edu", "")
        return f"[{text}]({href})"
    return re.sub(r'<a href="([^"]+)"[^>]*>(.*?)</a>', conv, t, flags=re.S)


def inline_md(t: str) -> str:
    """Convert inline HTML (links, <code>, <strong>, <em>) to markdown text."""
    # 1) <code> first (on raw text) so escaped entities inside stay intact;
    #    its inner text is protected by being wrapped in backticks.
    t = re.sub(r"<code>([^<]*?)</code>(\s*[,\.\)!?:;])",
               lambda m: f"`{(m.group(1) or '').strip()}`{m.group(2)}", t)
    t = re.sub(r"<code>([^<]*?)</code>",
               lambda m: f"`{(m.group(1) or '').strip()}`" if (m.group(1) or '').strip() else "", t)
    # 2) bold/italic, innermost-first (collapsed duplicates disappear in later passes)
    for _ in range(3):
        t = re.sub(r"<strong>([^<]*?)</strong>(\s*[,\.\)!?:;])",
                   lambda m: f"**{clean_text(hm.unescape(m.group(1)))}**{m.group(2)}", t)
        t = re.sub(r"<strong>([^<]*?)</strong>",
                   lambda m: f"**{clean_text(hm.unescape(m.group(1)))}**"
                   if m.group(1) and m.group(1).strip() else "", t)
        t = re.sub(r"<em>([^<]*?)</em>(\s*[,\.\)!?:;])",
                   lambda m: f"*{clean_text(hm.unescape(m.group(1)))}*{m.group(2)}", t)
        t = re.sub(r"<em>([^<]*?)</em>",
                   lambda m: f"*{clean_text(hm.unescape(m.group(1)))}*"
                   if m.group(1) and m.group(1).strip() else "", t)
        if "<strong" not in t and "<em" not in t:
            break
    # 3) restore quotes/entities ElementTree dropped, but only in *text* nodes —
    #    doing it over the whole string would corrupt attribute values (e.g. href)
    def fix_text(inner: str) -> str:
        inner = re.sub(r'"(?!;)', '&#34;', inner)
        inner = re.sub(r"'(?!;)", '&#39;', inner)
        inner = re.sub(r"&(?![#a-zA-Z0-9]+;)", '&amp;', inner)
        return htmllib.unescape(inner)
    t = re.sub(r'>([^<]+)<', lambda m: '>' + fix_text(m.group(1)) + '<', t)
    t = re.sub(r'^([^<]+)', lambda m: fix_text(m.group(1)), t)
    # guard: decode valid leftover entities, drop bare ones
    t = re.sub(r'&#(\d+);', lambda m: chr(int(m.group(1))), t)
    t = re.sub(r'&([a-zA-Z]+);', lambda m: {'lt':'<','gt':'>','amp':'&','quot':'"','apos':"'",
                                             'ldquo':'\u201c','rdquo':'\u201d','rsquo':'\u2019','lsquo':'\u2018'}.get(m.group(1), ''), t)
    t = re.sub(r'&(?![#a-zA-Z0-9]+;)', '', t)
    # inline images (from list items / aside text) -> markdown images
    def imgmd(m):
        srcm = re.search(r'src="([^"]+)"', m.group(0))
        altm = re.search(r'alt="([^"]*)"', m.group(0))
        if srcm:
            alt = altm.group(1) if altm and altm.group(1) else ""
            return f" ![{alt}]({srcm.group(1)}) "
        return " "
    t = re.sub(r"<img[^>]*?/?>", imgmd, t)
    t = links_to_md(t)
    # tidy bold/italic: drop empty marker runs (****) and add a space between
    # two *adjacent* marker runs (**a****b** -> **a** **b**). A marker followed
    # by a normal word or punctuation (e.g. "text**!Word") is a legitimate
    # closing/opening boundary and must be left alone.
    t = re.sub(r'\*{2,3}(?=\*{1,3})', '', t)   # collapse empty runs first
    t = re.sub(r'(?<=\S)\*{2,3}(?=\*)', ' ', t)  # space between adjacent runs
    # protect code spans from tag-stripping (they may contain <placeholders>)
    codes = []
    def keep(m):
        codes.append(m.group(0))
        return f"\x00{len(codes)-1}\x00"
    t = re.sub(r"`[^`]*`", keep, t)
    t = strip_inline_tags(t)
    t = re.sub(r"\x00(\d+)\x00", lambda m: codes[int(m.group(1))], t)
    return clean_text(t)



def md_escape(text: str) -> str:
    return text.replace("|", "\\|").replace("\n", " ")


def strip_all(t: str) -> str:
    return re.sub(r"<[^>]+>", "", t)


def _inner_et(el) -> str:
    """ElementTree serialization that keeps the last descendant's tail."""
    parts = [el.text or ""]
    children = list(el)
    for c in children:
        parts.append(ET.tostring(c, encoding="unicode"))
    if children:
        parts.append(children[-1].tail or "")
    return " ".join(x for x in parts if x and x.strip())


def _img_count(html: str) -> int:
    return len(re.findall(r'<img[^>]*>', html))


def inner_text(el, raw: str) -> str:
    """Return the raw inner HTML of *el* taken from the source string *raw*
    (avoiding ElementTree serialization quirks)."""
    tag = el.tag
    # Build a regex for the exact opening tag used for el
    # (attributes order is preserved by ET only for the first few; instead
    #  match on tag name and use a simple depth counter).
    import re as _re
    # find all occurrences of this tag in raw and pick the one whose content
    # best matches el (by comparing a text fingerprint)
    import html as _h
    # fingerprints: first and last 20 non-space chars of the element's full text
    full = _h.unescape(strip_all("".join(el.itertext())))
    nonsp = [c for c in full if not c.isspace()]
    fp = "".join(nonsp[:20])
    fp_end = "".join(nonsp[-20:])
    n_imgs = len(list(el.iter("img")))
    img_srcs = [c.get("src") for c in el.iter("img") if c.get("src")]
    open_re = _re.compile(r"<" + tag + r"(\s[^>]*)?>")
    for m in open_re.finditer(raw):
        # crude balance check: count opening/closing of *tag* from m.end()
        depth = 1
        pos = m.end()
        while depth > 0 and pos < len(raw):
            nxt_open = raw.find("<" + tag, pos)
            nxt_close = raw.find("</" + tag + ">", pos)
            if nxt_close == -1:
                pos = len(raw)
                break
            if nxt_open != -1 and nxt_open < nxt_close:
                depth += 1
                pos = nxt_open + len(tag) + 1
            else:
                depth -= 1
                pos = nxt_close + len(tag) + 2
        inner = raw[m.end():pos - len(tag) - 2] if depth == 0 else None
        if inner is None:
            continue
        # fingerprints of the candidate
        cand = _h.unescape(strip_all(inner))
        cand_nonsp = [c for c in cand if not c.isspace()]
        cand_fp = "".join(cand_nonsp[:20])
        cand_fp_end = "".join(cand_nonsp[-20:])
        if not (len(fp) >= 3 and fp == cand_fp and fp_end == cand_fp_end):
            continue
        # disambiguate: the element's own direct text must appear in the candidate
        direct = re.sub(r"\s+", " ", _h.unescape(strip_all(el.text or ""))).strip()
        if direct and direct not in _h.unescape(strip_all(inner)):
            continue
        # disambiguate: number of images inside the candidate must match
        if _img_count(inner) != n_imgs:
            continue
        # disambiguate: image srcs must appear in the candidate (handles
        # elements that are identical except for attribute values)
        if img_srcs and not all(src in inner for src in img_srcs):
            continue
        return inner
    # fallback: ElementTree serialization (keeps the last descendant's tail)
    return _inner_et(el)


def _remove_top(tag: str, s: str) -> str:
    """Remove the first top-level <tag>...</tag> (balanced) from s."""
    import re as _re
    open_re = _re.compile(r"<" + tag + r"(\s[^>]*)?>")
    for m in open_re.finditer(s):
        depth = 1
        pos = m.end()
        while depth > 0 and pos < len(s):
            nxt_open = s.find("<" + tag, pos)
            nxt_close = s.find("</" + tag + ">", pos)
            if nxt_close == -1:
                return s[:m.start()] + s[pos:]
            if nxt_open != -1 and nxt_open < nxt_close:
                depth += 1
                pos = nxt_open + len(tag) + 1
            else:
                depth -= 1
                pos = nxt_close + len(tag) + 2
        return s[:m.start()] + s[pos:]
    return s


def element_md(el, raw: str) -> list:
    """Render one (top-level) element of a step body to markdown lines."""
    lines = []
    tag = el.tag

    if tag in ("h1", "h2", "h3", "h4"):
        level = int(tag[1])
        lines.append("#" * (level + 1) + " " + inline_md(inner_text(el, raw)))
        lines.append("")
        return lines

    if tag == "p":
        imgs = [c for c in el if c.tag == "img"]
        text = inline_md(inner_text(el, raw))
        if text:
            lines.append(text)
        if imgs:
            for img in imgs:
                src = img.get("src")
                alt = img.get("alt", "")
                if src:
                    lines.append(f"![{alt}]({src})" if alt else f"![]({src})")
        if text or imgs:
            lines.append("")
        return lines

    if tag == "pre":
        # Handle <pre><code>...</code></pre> (nested code blocks)
        code = el.find("code")
        if code is not None:
            text = "".join(code.itertext())
            text = htmllib.unescape(text)
            # Preserve newlines but normalize whitespace
            text = re.sub(r"[ \t]+\n", "\n", text)
            text = re.sub(r"\n[ \t]+", "\n", text)
            text = text.strip()
            if text:
                lines.append("```")
                lines.append(text)
                lines.append("```")
                lines.append("")
            return lines
        text = clean_text(ET.tostring(el, encoding="unicode"))
        text = re.sub(r"^<pre>|</pre>$", "", text)
        if text:
            lines.append("```")
            lines.append(text)
            lines.append("```")
            lines.append("")
        return lines

    if tag in ("ul", "ol"):
        i = 1
        if tag == "ol":
            i = int(el.get("start", "1"))
        for li in el.findall("li"):
            prefix = f"{i}. " if tag == "ol" else "- "
            i += 1
            nested = [c for c in li if c.tag in ("ul", "ol")]
            # inner text of li excluding nested lists
            li_raw = inner_text(li, raw)
            # remove nested list markup from the li raw (they're rendered separately)
            for n in nested:
                n_open = f"<{n.tag}"
                # crude: remove from first n_open to its matching close
                li_raw = _remove_top(n.tag, li_raw)
            text = inline_md(li_raw)
            lines.append(prefix + text)
            for n in nested:
                for line in element_md(n):
                    lines.append("  " + line if line else "")
        lines.append("")
        return lines

    if tag == "aside":
        kind = el.get("class", "special")
        label = "note" if kind == "special" else "warning"
        text = inline_md(inner_text(el, raw))
        if text:
            lines.append("{: .%s }" % label)
            lines.append(text)
            lines.append("")
        return lines

    if tag == "table":
        rows = el.findall("tr")
        if rows:
            def cells(tr):
                return [md_escape(inline_md(inner_text(c, raw)))
                        for c in tr if c.tag in ("td", "th")]
            first = cells(rows[0])
            lines.append("| " + " | ".join(first) + " |")
            lines.append("|" + "---|" * len(first))
            for tr in rows[1:]:
                c = cells(tr)
                lines.append("| " + " | ".join(c) + " |")
            lines.append("")
        return lines

    if tag == "img":
        src = el.get("src")
        alt = el.get("alt", "")
        if src:
            lines.append(f"![{alt}]({src})" if alt else f"![]({src})")
            lines.append("")
        return lines

    # fallback: unknown element
    text = inline_md(inner_text(el, raw))
    if text:
        lines.append(text)
        lines.append("")
    return lines


def step_to_md(body_el, body_raw: str, label: str, skip_label: bool) -> str:
    parts = []
    if label and not skip_label:
        parts.append(f"## {htmllib.unescape(label)}")
        parts.append("")
    for el in body_el:
        parts.extend(element_md(el, body_raw))
    return "\n".join(parts)


def convert(cdir: str) -> None:
    title, parent, grand_parent, nav_order, redirect, intro, duration = META[cdir]
    # cdir is relative to codelab-sources/, e.g. "devcontainer/new-accounts"
    rel = Path(cdir)                 # <area>/<name>
    src_dir = SRC_ROOT / rel         # codelab-sources/<area>/<name>
    html = (src_dir / "index.html").read_text()
    # output: docs/<area>/<name>/<name>.md
    out_path = ROOT / "docs" / rel.parent / rel.name / f"{rel.name}.md"

    steps = re.findall(
        r'<google-codelab-step label="([^"]*)" duration="(\d+)">(.*?)</google-codelab-step>',
        html, re.S)

    out = []
    out.append("---")
    out.append("layout: default")
    out.append(f'title: "{title}"')
    out.append(f'parent: "{parent}"')
    if grand_parent:
        out.append(f'grand_parent: "{grand_parent}"')
    out.append(f"nav_order: {nav_order}")
    out.append(f"permalink: /docs/{rel.as_posix()}")
    if duration:
        out.append(f"read_time: {duration}")
    out.append("---")
    out.append("")

    if intro:
        out.append(intro)
        out.append("")

    for i, (label, dur, body) in enumerate(steps):
        body = body.strip()
        # make the body XML-valid: bare attributes, img without alt, unclosed tags
        body = re.sub(r'<h(\d) is-upgraded>', r'<h\1>', body)
        body = re.sub(r'<img (?![^>\n]*alt=)', '<img alt="" ', body)
        body = re.sub(r'<img(\s[^>]*[^/\s])>', r'<img\1/>', body)
        # self-close void tags left open by claat (e.g. <br> in a Google Doc "hard break")
        body = re.sub(r'<br>', '<br/>', body)
        # broken source: unescaped brackets in a <code> snippet (jetstream2 step 2)
        body = body.replace('<code><your-key-name></code>', '<code>&lt;your-key-name&gt;</code>')
        # paper-button -> plain link
        body = re.sub(r'<a href="([^"]+)"[^>]*>\s*<paper-button class="[^"]*"[^>]*>(.*?)</paper-button>\s*</a>',
                      r'<a href="\1">\2</a>', body, flags=re.S)
        # inline images inside text: convert to <img> ... </img> placeholders that
        # inline_md will render as markdown images
        def close_img(m):
            attrs = m.group(1) or ""
            if attrs.endswith("/"):
                return '<img inline="1"' + attrs[:-1] + '/>'
            return '<img inline="1"' + attrs + '/>'
        body = re.sub(r'<img alt=""(\s[^>]*)?/?>', close_img, body)
        # drop trailing scripts (none expected)
        body = re.sub(r'<script>.*?</script>', '', body, flags=re.S)
        # wrap for XML parsing
        try:
            body_el = ET.fromstring(f"<wrap>{body}</wrap>")
        except ET.ParseError as e:
            print(f"!! XML parse error in {cdir} step {i}: {e}")
            body_el = ET.fromstring(f"<wrap><p>{re.sub(chr(60) + r'[^>]+', ' ', body)}</p></wrap>")
        skip = (cdir, i) in SKIP_STEP_LABEL
        out.append(step_to_md(body_el, body, htmllib.unescape(label), skip))
        out.append("")

    out.append(f'**Next up:** continue on to [the related wiki page]({redirect}).')

    text = "\n".join(out)
    for old, new in REPLACEMENTS:
        text = text.replace(old, new)
    text = fix_urls(text)

    target = out_path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text)
    print(f"converted {cdir} -> {target}")


for cdir in META:
    convert(cdir)
