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
parser.add_argument('-c','--text-color', help='Color for the text on the picture. Default: White', required=False)

text_colors = {"solarized.png": (147,161,161),
               "black.png": (255,255,255)}

def get_random_text():
    lines = open('./text.txt').read().splitlines()
    return random.choice(lines)


def get_random_backdrop():
    backdrop = random.choice(os.listdir("./backdrop"))
    print(backdrop)
    return "./backdrop/"+backdrop, text_colors.get(backdrop, (255, 255, 255))


def generate_img(output="", backdrop="", text="", text_color=(255,255,255)):
    print(text_color)
    img = Image.open(backdrop)
    W, H = img.size
    draw = ImageDraw.Draw(img)

    font = ImageFont.truetype("DejaVuSansMono.ttf", 76)
    w, h = font.getsize(text)
    draw.text(((W-w)/2, (H/100)*70), text, text_color, font=font)
    img.save(output)


def main():
    args = parser.parse_args()

    output = args.output

    if args.backdrop:
        backdrop = args.backdrop
        text_color = None
    else:
        backdrop, text_color = get_random_backdrop()

    if args.text:
        text = args.text
    else:
        text = get_random_text()

    if args.text_color:
        text_color = args.text_color
    elif not text_color:
        text_color = text_colors.get(backdrop, (255, 255, 255))

    generate_img(output=output, backdrop=backdrop,
                 text=text, text_color=text_color)


if __name__ == '__main__':
    main()
