#!/usr/bin/env python3
"""Copy partials/header.html and partials/footer.html into every page.

Each page marks the shared blocks with <!-- @header --> ... <!-- /@header --> and
<!-- @footer --> ... <!-- /@footer -->. The page's <body data-page="..."> sets which
main navigation link gets aria-current="page".

    python3 tools/sync_partials.py
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PARTIALS = {name: (ROOT / "partials" / f"{name}.html").read_text().rstrip("\n") for name in ("header", "footer")}


def fill(page: str, name: str, body: str) -> str:
    pattern = re.compile(rf"<!-- @{name} -->\n(?:.*?\n)?<!-- /@{name} -->", re.S)
    if not pattern.search(page):
        raise SystemExit(f"missing <!-- @{name} --> markers")
    return pattern.sub(lambda m: f"<!-- @{name} -->\n{body}\n<!-- /@{name} -->", page)


def main() -> None:
    for path in sorted(ROOT.glob("*.html")):
        page = path.read_text()
        current = re.search(r'<body[^>]*data-page="([^"]+)"', page)
        header = PARTIALS["header"]
        if current:
            header = header.replace(f'data-nav="{current.group(1)}"', f'data-nav="{current.group(1)}" aria-current="page"')
        page = fill(page, "header", header)
        page = fill(page, "footer", PARTIALS["footer"])
        path.write_text(page)
        print(f"synced {path.name}")


if __name__ == "__main__":
    main()
