#!/usr/bin/env python3
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

import random
import argparse
import os


# Arguments
parser = argparse.ArgumentParser(description='Generate random Arch wallpaper')
# parser.add_argument('output filename', metavar='[OUTPUT]', help='Output filename')
parser.add_argument('-o','--output', help='Output file name', required=True)
parser.add_argument('-b','--backdrop', help='Backdrop to use, else random. \'black\' or \'solarized\'', required=False)
parser.add_argument('-t','--text', help='Text on the picture, or random', required=False)


def get_random_text():
    lines = open('./text.txt').read().splitlines()
    return random.choice(lines)


def get_random_backdrop():
    return "./backdrop/"+random.choice(os.listdir("./backdrop"))


def main(output="", backdrop="", text=""):
    print(backdrop)
    img = Image.open(backdrop)
    W, H = img.size
    draw = ImageDraw.Draw(img)

    font = ImageFont.truetype("DejaVuSansMono.ttf", 76)
    w, h = font.getsize(text)
    draw.text(((W-w)/2, (H/100)*70), text, (255, 255, 255), font=font)
    img.save(output)


if __name__ == '__main__':
    args = parser.parse_args()
    print(args)
    if args.output:
        output = args.output
    if args.backdrop:
        backdrop=args.backdrop
    else:
        backdrop=get_random_backdrop()
    if args.text:
        text=args.text
    else:
        text=get_random_text()

    main(output=output, backdrop=backdrop, text=text)
