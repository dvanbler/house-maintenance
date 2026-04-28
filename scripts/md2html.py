#!/usr/bin/env python3
"""Convert a Markdown file to GitHub-styled HTML, output to stdout."""

import sys
import os
import markdown

GITHUB_CSS = """
  *, *::before, *::after { box-sizing: border-box; }
  body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Noto Sans", Helvetica, Arial, sans-serif;
    font-size: 16px;
    line-height: 1.5;
    color: #1f2328;
    background-color: #ffffff;
    margin: 0;
    padding: 32px;
  }
  .markdown-body {
    max-width: 800px;
    margin: 0 auto;
    padding: 40px;
    border: 1px solid #d0d7de;
    border-radius: 6px;
  }
  .markdown-body h1, .markdown-body h2 {
    padding-bottom: 0.3em;
    border-bottom: 1px solid #d0d7de;
  }
  .markdown-body h1 { font-size: 2em; margin: 0.67em 0; }
  .markdown-body h2 { font-size: 1.5em; }
  .markdown-body h3 { font-size: 1.25em; }
  .markdown-body h4 { font-size: 1em; }
  .markdown-body h5 { font-size: 0.875em; }
  .markdown-body h6 { font-size: 0.85em; color: #656d76; }
  .markdown-body h1, .markdown-body h2, .markdown-body h3,
  .markdown-body h4, .markdown-body h5, .markdown-body h6 {
    font-weight: 600;
    line-height: 1.25;
    margin-top: 24px;
    margin-bottom: 16px;
  }
  .markdown-body p { margin-top: 0; margin-bottom: 16px; }
  .markdown-body a { color: #0969da; text-decoration: none; }
  .markdown-body a:hover { text-decoration: underline; }
  .markdown-body code {
    font-family: ui-monospace, SFMono-Regular, SF Mono, Menlo, Consolas, "Liberation Mono", monospace;
    font-size: 85%;
    background-color: #f6f8fa;
    border-radius: 6px;
    padding: 0.2em 0.4em;
  }
  .markdown-body pre {
    background-color: #f6f8fa;
    border-radius: 6px;
    font-size: 85%;
    line-height: 1.45;
    overflow: auto;
    padding: 16px;
    margin-bottom: 16px;
  }
  .markdown-body pre code {
    background-color: transparent;
    border: 0;
    display: inline;
    font-size: 100%;
    line-height: inherit;
    margin: 0;
    overflow: visible;
    padding: 0;
    word-wrap: normal;
  }
  .markdown-body blockquote {
    border-left: 0.25em solid #d0d7de;
    color: #656d76;
    margin: 0 0 16px 0;
    padding: 0 1em;
  }
  .markdown-body ul, .markdown-body ol {
    margin-top: 0;
    margin-bottom: 16px;
    padding-left: 2em;
  }
  .markdown-body li + li { margin-top: 0.25em; }
  .markdown-body li > ul, .markdown-body li > ol { margin-top: 0.25em; margin-bottom: 0; }
  .markdown-body img { max-width: 100%; border-style: none; }
  .markdown-body hr {
    background-color: #d0d7de;
    border: 0;
    height: 0.25em;
    margin: 24px 0;
    padding: 0;
  }
  .markdown-body table {
    border-collapse: collapse;
    border-spacing: 0;
    display: block;
    max-width: 100%;
    overflow: auto;
    width: max-content;
    margin-bottom: 16px;
  }
  .markdown-body table th {
    background-color: #f6f8fa;
    font-weight: 600;
  }
  .markdown-body table th, .markdown-body table td {
    border: 1px solid #d0d7de;
    padding: 6px 13px;
  }
  .markdown-body table tr:nth-child(2n) { background-color: #f6f8fa; }
  .markdown-body input[type="checkbox"] { margin-right: 0.5em; }
"""

EXTENSIONS = [
    "tables",
    "fenced_code",
    "codehilite",
    "toc",
    "nl2br",
    "sane_lists",
    "attr_list",
    "def_list",
    "footnotes",
    "md_in_html",
    "smarty",
]

EXTENSION_CONFIGS = {
    "codehilite": {"guess_lang": False, "noclasses": True},
    "smarty": {"smart_dashes": True, "smart_quotes": True, "smart_ellipses": True},
}


def convert(md_path: str) -> str:
    with open(md_path, "r", encoding="utf-8") as f:
        source = f.read()

    title = os.path.splitext(os.path.basename(md_path))[0]

    # Try all extensions; fall back gracefully if one is missing.
    exts, configs = list(EXTENSIONS), dict(EXTENSION_CONFIGS)
    available = []
    for ext in exts:
        try:
            md = markdown.Markdown(extensions=[ext], extension_configs=configs if ext in configs else {})
            available.append(ext)
        except Exception:
            pass

    md = markdown.Markdown(
        extensions=available,
        extension_configs={k: v for k, v in configs.items() if k in available},
    )
    body = md.convert(source)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <style>{GITHUB_CSS}
  </style>
</head>
<body>
  <div class="markdown-body">
{body}
  </div>
</body>
</html>
"""


def main():
    if len(sys.argv) != 2:
        print(f"Usage: {os.path.basename(sys.argv[0])} <file.md>", file=sys.stderr)
        sys.exit(1)

    md_path = sys.argv[1]
    if not os.path.isfile(md_path):
        print(f"Error: file not found: {md_path}", file=sys.stderr)
        sys.exit(1)

    print(convert(md_path))


if __name__ == "__main__":
    main()
