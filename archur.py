#!/usr/bin/env python3
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from PIL import ImageOps
from PIL import ImageColor

import random
import argparse
import os


DEFAULT_DIR="/usr/share/archur"

themes = {"solarized": {"text": (147,161,161),
                        "logo": (147,161,161),
                        "background": (0, 43, 54)},
          "black": {"text": (255,255,255),
                        "logo": (255, 255, 255),
                        "background": (0,0,0)},

def get_random_text():
    lines = open(DEFAULT_DIR+'/text.txt').read().splitlines()
    return random.choice(lines)


def get_random_theme():
    key = random.choice(list(themes.keys()))
    return themes[key]


def text_draw(draw, text, pixel, ress, theme):
    text = text.split("\\n")
    W, H = ress
    base_height = (H/100)*70
    for i in text:
        font = ImageFont.truetype("DejaVuSansMono.ttf", pixel)
        w, h = font.getsize(i)
        draw.text(((W-w)/2, base_height), i, theme["text"], font=font)
        base_height += (H/100)*8


def generate_img(output="", theme={}, text="", resolution=(1920,1080), text_scale=1.0, logo_scale=1.0):

    # img = Image.open(backdrop)
    img = Image.new("RGB", resolution, theme["background"])
    W, H = img.size

    logo = Image.open(DEFAULT_DIR+"/assets/logo.png")
    colorized_img = ImageOps.colorize(logo.convert("L"), theme["logo"], theme["background"])
    size = int((W/100)*17*logo_scale)
    logo_newsize = colorized_img.resize((size, size), Image.ANTIALIAS)
    img.paste(logo_newsize, (int((W-size)/2), int((H-size)/2)))

    draw = ImageDraw.Draw(img)

    base_font_pixle = int((56/1920)*resolution[0]*text_scale)

    font = ImageFont.truetype("DejaVuSansMono.ttf", base_font_pixle)
    w, h = font.getsize(text)

    text_draw(draw, text, base_font_pixle, img.size, theme)

    img.save(output, quality=100)


def main():
    parser = argparse.ArgumentParser(description='Generate random Arch wallpaper')
    parser.add_argument('-o','--output', help='Output file name', required=True)
    parser.add_argument('-t','--theme', default=get_random_theme(), help='The theme to use, else random. \'black\' or \'solarized\'', required=False)
    parser.add_argument('--text', default=get_random_text(), help='Text on the picture, or random', required=False)
    parser.add_argument('-r', '--resolution', default=(1920,1080), help='Sets the resolution of the image. Example: 1920x1080', required=False)
    parser.add_argument('-ts', '--text-scale', default=(1.0), help='Sets scale for the text. Example: 1.75', required=False)
    parser.add_argument('-ls', '--logo-scale', default=(1.0), help='Sets scale for the logo. Example: 3.0', required=False)
    parser.add_argument('-fg', '--foreground-color', type=str, help='Color for the text and the logo.', required=False)
    parser.add_argument('-bg', '--background-color', type=str, help='Color for the background.', required=False)
    args = vars(parser.parse_args())

    output = args["output"]

    if isinstance(args["theme"], str):
        args["theme"] = themes[args["theme"]]

    if isinstance(args["resolution"], str):
        x,y = args["resolution"].split("x")
        args["resolution"] = (int(x),int(y))

    if args.get("foreground_color"):
        try:
            args["theme"]["text"] = ImageColor.getrgb(args["foreground_color"])
        except: pass

    if args.get("background_color"):
        try:
            args["theme"]["background"] = ImageColor.getrgb(args["background_color"])
        except: pass


    generate_img(output=output, theme=args["theme"], text=args["text"], resolution=args["resolution"],
        text_scale=float(args["text_scale"]), logo_scale=float(args["logo_scale"]))


if __name__ == '__main__':
    main()
