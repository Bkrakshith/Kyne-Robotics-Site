#!/usr/bin/env python3
"""Write docs/COPY.md: the words of every page, in page order, for review and editing.

The HTML pages are the source. Run this after a copy change so the copy deck stays in step:

    python3 tools/export_copy.py
"""
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGES = [
    ("index.html", "Home"),
    ("services.html", "Services"),
    ("programmes.html", "Programmes"),
    ("technology.html", "Technology"),
    ("work.html", "Work"),
    ("work-packoff-cell.html", "Case study: AgiBot G2 pack-off cell"),
    ("work-wardzero.html", "Case study: WardZero"),
    ("company.html", "Company"),
    ("contact.html", "Contact"),
    ("404.html", "Page not found"),
]
SKIP = {"script", "style", "svg", "head", "select", "video"}
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"}
BLOCKS = {"h1": "### ", "h2": "#### ", "h3": "##### ", "p": "", "li": "- ", "figcaption": "> ",
          "summary": "**Q:** ", "dt": "**", "dd": "", "td": "", "th": "", "label": "Field: ", "legend": "Field: "}
LABELS = {"eyebrow", "stat-card__label", "case-card__tag", "info-card__num", "status-box__label", "tag"}


class CopyParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out, self.stack, self.buf, self.meta = [], [], [], {}

    @property
    def skipping(self):
        return any(skip for _, _, skip in self.stack)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "meta" and attrs.get("name") == "description":
            self.meta["description"] = attrs.get("content", "")
        if tag in VOID:
            return
        classes = set((attrs.get("class") or "").split())
        skip = tag in SKIP or attrs.get("aria-hidden") == "true" or "visually-hidden" in classes
        kind = tag if tag in BLOCKS else None
        if tag in ("a", "button", "span") and classes & {"btn", "pill-link__label"}:
            kind = "button"
        elif classes & {"step__title", "stat-card__value"}:
            kind = "strong"
        if classes & LABELS:
            kind = "label"
        if kind and not self.skipping:
            self.flush()
        self.stack.append((tag, kind, skip))

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        while self.stack:
            t, kind, _ = self.stack[-1]
            was_skipping = self.skipping
            self.stack.pop()
            if kind and not was_skipping:
                self.flush(kind)
            if t == tag:
                break

    def handle_data(self, data):
        if not self.skipping:
            self.buf.append(data)

    def flush(self, kind=None):
        text = " ".join(" ".join(self.buf).split())
        self.buf = []
        if not text:
            return
        if kind == "button":
            self.out.append(f"[{text}]")
        elif kind == "label":
            self.out.append(f"*{text.upper()}*")
        elif kind == "strong":
            self.out.append(f"**{text}**")
        elif kind == "dt":
            self.out.append(f"**{text}:**")
        elif kind:
            self.out.append(BLOCKS[kind] + text)
        else:
            self.out.append(text)


def strip_shared(page: str) -> str:
    for name in ("header", "footer"):
        start, end = page.find(f"<!-- @{name} -->"), page.find(f"<!-- /@{name} -->")
        if start != -1 and end != -1:
            page = page[:start] + page[end:]
    return page


def main() -> None:
    lines = ["# Kyne Robotics website copy", "",
             "Generated from the HTML pages by `tools/export_copy.py`. Edit the pages, then run the script again.",
             "Shared navigation and footer text is listed once at the end.", ""]
    for file, title in PAGES:
        parser = CopyParser()
        page = (ROOT / file).read_text()
        title_tag = page.split("<title>", 1)[1].split("</title>", 1)[0]
        parser.feed(strip_shared(page))
        parser.flush()
        lines += ["---", "", f"## Page: {title} (`{file}`)", "",
                  f"Browser title: {title_tag}  ", f"Meta description: {parser.meta.get('description', '')}", ""]
        for item in parser.out:
            lines += [item, ""]
    footer = (ROOT / "partials/footer.html").read_text()
    parser = CopyParser()
    parser.feed(footer)
    parser.flush()
    lines += ["---", "", "## Shared footer", ""] + [f"{x}\n" for x in parser.out]
    out = ROOT / "docs/COPY.md"
    out.parent.mkdir(exist_ok=True)
    out.write_text("\n".join(lines).rstrip() + "\n")
    print(f"wrote {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
