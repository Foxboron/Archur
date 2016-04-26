#!/usr/bin/env python3
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from PIL import ImageOps

import random
import argparse
import os


# Arguments

themes = {"solarized": {"text": (147,161,161),
                        "background": (0, 43, 54)},
          "black": {"text": (255,255,255),
                    "background": (0,0,0)}}

def get_random_text():
    lines = open('./text.txt').read().splitlines()
    return random.choice(lines)


def get_random_theme():
    key = random.choice(list(themes.keys()))
    return themes[key]


def generate_img(output="", theme={}, text=""):

    # img = Image.open(backdrop)
    img = Image.new("RGB", (1920,1080), theme["background"])
    W, H = img.size

    logo = Image.open("./assets/logo.png")
    colorized_img = ImageOps.colorize(logo.convert("L"), theme["text"], theme["background"])
    size = int((W/100)*17)
    logo_newsize = colorized_img.resize((size, size), Image.ANTIALIAS)
    img.paste(logo_newsize, (int((W-size)/2), int((H-size)/2)))

    draw = ImageDraw.Draw(img)

    font = ImageFont.truetype("DejaVuSansMono.ttf", 76)
    w, h = font.getsize(text)
    draw.text(((W-w)/2, (H/100)*70), text, theme["text"], font=font)

    img.save(output, quality=100)


def main():
    parser = argparse.ArgumentParser(description='Generate random Arch wallpaper')
    parser.add_argument('-o','--output', help='Output file name', required=True)
    parser.add_argument('-t','--theme', default=get_random_theme(), help='The theme to use, else random. \'black\' or \'solarized\'', required=False)
    parser.add_argument('--text', default=get_random_text(), help='Text on the picture, or random', required=False)
    parser.add_argument('--text-color', help='Color for the text on the picture. Default: White', required=False)
    args = parser.parse_args()

    output = args.output

    if args.text_color:
        args.theme["text"] = args.text_color

    if args.theme:
        args.theme = themes[args.theme]

    generate_img(output=output, theme=args.theme, text=args.text)


if __name__ == '__main__':
    main()
