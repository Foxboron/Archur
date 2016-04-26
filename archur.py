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



def multi_line_draw(draw, text, pixel, ress, theme):
    text = text.split("\\n")
    W, H = ress
    base_height = (H/100)*70
    for i in text:
        font = ImageFont.truetype("DejaVuSansMono.ttf", pixel)
        w, h = font.getsize(i)
        draw.text(((W-w)/2, base_height), i, theme["text"], font=font)
        base_height += (H/100)*8


def generate_img(output="", theme={}, text="", resolution=(1920,1080)):

    # img = Image.open(backdrop)
    img = Image.new("RGB", resolution, theme["background"])
    W, H = img.size

    logo = Image.open("./assets/logo.png")
    colorized_img = ImageOps.colorize(logo.convert("L"), theme["text"], theme["background"])
    size = int((W/100)*17)
    logo_newsize = colorized_img.resize((size, size), Image.ANTIALIAS)
    img.paste(logo_newsize, (int((W-size)/2), int((H-size)/2)))

    draw = ImageDraw.Draw(img)

    base_font_pixle = int((76/1920)*resolution[0])
    font = ImageFont.truetype("DejaVuSansMono.ttf", base_font_pixle)
    w, h = font.getsize(text)

    if "\\n" in text:
        print(text)
        multi_line_draw(draw, text, base_font_pixle, img.size, theme)
    else:
        font = ImageFont.truetype("DejaVuSansMono.ttf", base_font_pixle)
        w, h = font.getsize(text)
        draw.text(((W-w)/2, (H/100)*70), text, theme["text"], font=font)

    img.save(output, quality=100)


def main():
    parser = argparse.ArgumentParser(description='Generate random Arch wallpaper')
    parser.add_argument('-o','--output', help='Output file name', required=True)
    parser.add_argument('-t','--theme', default=get_random_theme(), help='The theme to use, else random. \'black\' or \'solarized\'', required=False)
    parser.add_argument('--text', default=get_random_text(), help='Text on the picture, or random', required=False)
    parser.add_argument('-r', '--resolution', default=(1920,1080), help='Sets the resolution of the image. Example: 1920x1080', required=False)
    parser.add_argument('--text-color', help='Color for the text on the picture. Default: White', required=False)
    args = parser.parse_args()

    output = args.output

    if args.text_color:
        args.theme["text"] = args.text_color

    if isinstance(args.theme, str):
        args.theme = themes[args.theme]

    if isinstance(args.resolution, str):
        x,y = args.resolution.split("x")
        args.resolution = (int(x),int(y))

    generate_img(output=output, theme=args.theme, text=args.text, resolution=args.resolution)


if __name__ == '__main__':
    main()
