"""Build Perlead brand SVGs from Newsreader (OFL) glyph outlines.

Usage: python3 tools/make_brand.py /path/to/Newsreader[opsz,wght].ttf
Writes web/brand/*.svg. PNG exports are rendered with headless Chrome (see tools/export_brand.sh).
"""
import sys, os
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen

INK, PAPER, ACCENT = "#16181b", "#f7f5f1", "#1f4d3a"
OUT = os.path.join(os.path.dirname(__file__), "..", "web", "brand")

font = instancer.instantiateVariableFont(TTFont(sys.argv[1]), {"opsz": 72, "wght": 500})
gs, cmap = font.getGlyphSet(), font.getBestCmap()
upm = font["head"].unitsPerEm
cap = font["OS/2"].sCapHeight

def path_for(text, scale, x0, baseline, tracking=0.0):
    pen = SVGPathPen(gs)
    x = 0
    for ch in text:
        g = cmap[ord(ch)]
        tp = TransformPen(pen, (scale, 0, 0, -scale, x0 + x * scale, baseline))
        gs[g].draw(tp)
        x += gs[g].width + tracking * upm
    return pen.getCommands(), x * scale

def bounds(text):
    bp = BoundsPen(gs); x = 0
    for ch in text:
        g = cmap[ord(ch)]
        gs[g].draw(TransformPen(bp, (1, 0, 0, 1, x, 0))); x += gs[g].width
    return bp.bounds

def mark_paths(size=64, bg=ACCENT, fg=PAPER, p=0.56):
    # Serif P centered optically, plus a small square: the "next step" marker from the design system.
    xmin, ymin, xmax, ymax = bounds("P")
    s = (size * p) / cap
    w = (xmax - xmin) * s
    x0 = (size - w) / 2 - xmin * s - size * 0.04
    base = size / 2 + cap * s / 2
    d, _ = path_for("P", s, x0, base)
    q = size * 0.11
    sq_x = x0 + xmax * s + size * 0.02
    sq_y = base - q
    r = size * 0.16
    return (f'<rect width="{size}" height="{size}" rx="{r:.2f}" fill="{bg}"/>'
            f'<path d="{d}" fill="{fg}"/>'
            f'<rect x="{sq_x:.2f}" y="{sq_y:.2f}" width="{q:.2f}" height="{q:.2f}" fill="{fg}"/>')

def svg(w, h, body, title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:.0f} {h:.0f}" width="{w:.0f}" height="{h:.0f}" role="img" aria-label="{title}">'
            f'<title>{title}</title>{body}</svg>\n')

def wordmark(color=INK, mark_bg=ACCENT, mark_fg=PAPER):
    H = 64
    s = (H * 0.62) / cap
    gap = 18
    d, adv = path_for("Perlead", s, H + gap, H / 2 + cap * s / 2 , tracking=-0.01)
    W = H + gap + adv
    return W, H, f'<g>{mark_paths(H, mark_bg, mark_fg)}</g><path d="{d}" fill="{color}"/>'

os.makedirs(OUT, exist_ok=True)
open(f"{OUT}/logo-mark.svg", "w").write(svg(64, 64, mark_paths(), "Perlead"))
open(f"{OUT}/favicon.svg", "w").write(svg(64, 64, mark_paths(p=0.68), "Perlead"))  # larger glyph for 16px legibility
W, H, body = wordmark()
open(f"{OUT}/logo.svg", "w").write(svg(W, H, body, "Perlead"))
W, H, body = wordmark(color=PAPER, mark_bg=PAPER, mark_fg=INK)
open(f"{OUT}/logo-reversed.svg", "w").write(svg(W, H, body, "Perlead"))
# Text-only wordmark for small inline use
s = 40 / cap
d, adv = path_for("Perlead", s, 0, 44, tracking=-0.01)
open(f"{OUT}/wordmark.svg", "w").write(svg(adv, 56, f'<path d="{d}" fill="{INK}"/>', "Perlead"))
print("ok", W, H)
