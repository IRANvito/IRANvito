#!/usr/bin/env python3
"""Regenerate the PNG icons in this directory (requires Pillow):

    python3 internal/webui/assets/icons/generate.py internal/webui/assets/icons

Draws the panel's "IV" mark on the dark ground, matching iconSVG in
internal/webui/handlers_app.go.
"""
import sys, os
from PIL import Image, ImageDraw, ImageFont

FONT = '/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf'


def make(size, maskable=False):
    S = size * 4
    bg = Image.new('RGBA', (S, S))
    px = bg.load()
    for y in range(S):
        c = int(38 - 31 * y / S)
        for x in range(S):
            px[x, y] = (c, c, c, 255)
    if maskable:
        im = bg
    else:
        im = Image.new('RGBA', (S, S), (0, 0, 0, 0))
        mask = Image.new('L', (S, S), 0)
        ImageDraw.Draw(mask).rounded_rectangle((0, 0, S - 1, S - 1), radius=int(S * 0.22), fill=255)
        im.paste(bg, (0, 0), mask)
    d = ImageDraw.Draw(im)
    font = ImageFont.truetype(FONT, int(S * (0.40 if maskable else 0.46)))
    b = d.textbbox((0, 0), 'IV', font=font)
    w, h = b[2] - b[0], b[3] - b[1]
    d.text(((S - w) / 2 - b[0], (S - h) / 2 - b[1]), 'IV', font=font, fill=(255, 255, 255, 255))
    bw, bh = int(w * 0.62), max(4, int(S * 0.018))
    y0 = int((S + h) / 2 + S * 0.05)
    d.rounded_rectangle(((S - bw) / 2, y0, (S + bw) / 2, y0 + bh), radius=bh // 2, fill=(230, 60, 60, 255))
    return im.resize((size, size), Image.LANCZOS)


if __name__ == '__main__':
    out = sys.argv[1] if len(sys.argv) > 1 else '.'
    make(512).save(os.path.join(out, 'icon-512.png'))
    make(192).save(os.path.join(out, 'icon-192.png'))
    make(180).save(os.path.join(out, 'apple-touch-icon.png'))
    make(512, True).save(os.path.join(out, 'icon-maskable-512.png'))
