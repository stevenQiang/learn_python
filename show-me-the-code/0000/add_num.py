# -*- coding:utf-8 -*-
# 第 0000 题：将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果

from PIL import Image, ImageDraw, ImageFont


def add_num(image_source, num):
    avatar = Image.open(image_source)
    draw_avatar = ImageDraw.Draw(avatar)
    x_size, y_size = avatar.size
    font_size = min(x_size, y_size)
    # 选择字体
    export_font = ImageFont.truetype('Futura.ttf', font_size / 3)
    # 在图片上添加字
    draw_avatar.text([1.5 * x_size / 2, 0], str(num), font=export_font, fill=(255, 0, 0))
    avatar.show()

if __name__ == '__main__':
    try:
        image_name = None
        while True:
            image_name = raw_input("Input image name(exit please input 0):")
            print image_name
            if image_name:
                break
        if image_name == '0':
            print "exit..."
        else:
            add_num(image_name, '9')
    except KeyboardInterrupt:
        print "\nexit..."
