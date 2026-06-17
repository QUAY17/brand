"""Rasterize the QUAY brand SVGs into shipping image assets.

Reads the four canonical vector files in brand-assets/ (logo-dark, logo-light,
favicon-dark, favicon-light) and renders them to transparent PNGs and a
multi-size favicon.ico in the repo-root assets/ directory. SVG rasterization
runs through headless Chrome so gradients, the blur glow, and the Syne wordmark
(loaded from Google Fonts) render exactly as designed; Pillow downscales the
masters and assembles the .ico.

Usage:
    python brand-assets/build-assets.py

Re-run any time the source SVGs change. Requires Chrome (or set CHROME env var)
and Pillow. Network access is needed once so the Syne webfont loads for the
logo wordmark.
"""

from __future__ import annotations

import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from PIL import Image

REPO = Path(__file__).resolve().parent.parent
SRC = REPO / "brand-assets"
OUT = REPO / "assets"

CHROME_CANDIDATES = [
    os.environ.get("CHROME", ""),
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
]

# Favicon raster sizes derived from the 512px master, plus the .ico bundle sizes.
FAVICON_PNG_SIZES = [512, 256, 180, 48, 32, 16]
ICO_SIZES = [16, 32, 48, 256]


def find_chrome() -> str:
    for path in CHROME_CANDIDATES:
        if path and Path(path).is_file():
            return path
    sys.exit("Chrome/Edge not found. Set the CHROME environment variable.")


def wrap_html(svg: str, width: int, height: int) -> str:
    """Wrap an SVG in a margin-less, transparent page sized to the master px."""
    return (
        "<!doctype html><html><head><meta charset='utf-8'>"
        "<style>html,body{margin:0;padding:0;background:transparent}"
        f"svg{{display:block;width:{width}px;height:{height}px}}</style>"
        f"</head><body>{svg}</body></html>"
    )


def render_png(chrome: str, svg_path: Path, out_png: Path, width: int, height: int) -> None:
    svg = svg_path.read_text(encoding="utf-8")
    with tempfile.TemporaryDirectory() as tmp:
        html_path = Path(tmp) / "page.html"
        html_path.write_text(wrap_html(svg, width, height), encoding="utf-8")
        profile = Path(tmp) / "profile"
        subprocess.run(
            [
                chrome,
                "--headless=new",
                "--disable-gpu",
                "--hide-scrollbars",
                "--force-device-scale-factor=1",
                "--default-background-color=00000000",
                "--virtual-time-budget=5000",
                f"--user-data-dir={profile}",
                f"--window-size={width},{height}",
                f"--screenshot={out_png}",
                html_path.as_uri(),
            ],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
    if not out_png.exists():
        sys.exit(f"Render failed: {out_png}")


def main() -> None:
    chrome = find_chrome()
    OUT.mkdir(exist_ok=True)

    # Keep the vector sources alongside the rasters for a self-contained web bundle.
    for name in ("favicon-dark.svg", "favicon-light.svg", "logo-dark.svg", "logo-light.svg"):
        shutil.copyfile(SRC / name, OUT / f"quay-{name}")
    # The site <head> link and the designer's default both expect the dark mark here.
    shutil.copyfile(SRC / "favicon-dark.svg", OUT / "quay-favicon.svg")

    # Favicon masters (64x64 viewBox -> 512 master), then downscale + .ico bundle.
    for variant in ("dark", "light"):
        master = OUT / f"_master-favicon-{variant}.png"
        render_png(chrome, SRC / f"favicon-{variant}.svg", master, 512, 512)
        base = Image.open(master).convert("RGBA")
        for size in FAVICON_PNG_SIZES:
            img = base.resize((size, size), Image.LANCZOS)
            img.save(OUT / f"quay-favicon-{variant}-{size}.png")
        master.unlink()

    # Apple touch icon + .ico use the dark mark (the shipped default).
    dark512 = Image.open(OUT / "quay-favicon-dark-512.png").convert("RGBA")
    dark512.resize((180, 180), Image.LANCZOS).save(OUT / "apple-touch-icon.png")
    dark512.save(OUT / "favicon.ico", sizes=[(s, s) for s in ICO_SIZES])

    # Logo wordmark lockups (232x72 viewBox -> 4x master), plus a half-size.
    for variant in ("dark", "light"):
        master = OUT / f"quay-logo-{variant}.png"
        render_png(chrome, SRC / f"logo-{variant}.svg", master, 928, 288)
        Image.open(master).convert("RGBA").resize((464, 144), Image.LANCZOS).save(
            OUT / f"quay-logo-{variant}-2x.png"
        )

    print(f"Done. Assets written to {OUT}")


if __name__ == "__main__":
    main()
