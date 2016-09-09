# -*- coding: utf-8 -*-
import random, string
from PIL import Image, ImageDraw, ImageFont


def get_random_number(number=4):
    charts = string.digits + string.letters
    return [random.choice(charts) for x in range(number)]


def get_color(x, y):
    return random.randint(x, y), random.randint(x, y), random.randint(x, y)


def get_image():
    width = 240
    height = 60
    image = Image.new('RGB', (width, height), (255, 255, 255))
    export_font = ImageFont.truetype('arialbd.ttf', 30)
    draw = ImageDraw.Draw(image)
    # 填充像素
    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill=get_color(64, 255))
    # 写文字
    for index, number in enumerate(get_random_number()):
        draw.text((60 * index + 10, 10), number, font=export_font, fill=get_color(32, 127))
    image.show('test.jpg')


if __name__ == '__main__':
    get_image()
