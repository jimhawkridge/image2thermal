#!/usr/bin/env python

import argparse
from math import ceil
from PIL import Image
import sys

MAX_WIDTH = 800

parser = argparse.ArgumentParser(description='Convert image for thermal printing.')
parser.add_argument('filename', metavar='image', type=str, nargs=1, help='the filename of the image to be converted')

args = parser.parse_args()

im = Image.open(args.filename[0])
w, h = im.size

if w > MAX_WIDTH:
    im.thumbnail((MAX_WIDTH, h/(w/float(MAX_WIDTH))), Image.ANTIALIAS)
    w, h = im.size

im = im.convert('1')

sys.stdout.write('\x1b~G')
line_len = chr(int(ceil(w/8.0)))
for i in range(0, h):
    sys.stdout.write(line_len)
    for j in range(0, w, 8):
        b = ''
        for x in range(j, min(w, j+8)):
            b += str(int(im.getpixel((x, i)) == 0))
        sys.stdout.write(chr(int(b.ljust(8, '0'), 2)))
    sys.stdout.write('\x00')
sys.stdout.write('\x80')
