# -*- coding: utf-8 -*-
# 第 0005 题： 你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。
import os
from PIL import Image, ImageDraw, ImageFont

PHOTO_TYPE = ['png', 'jpg', 'jpeg']


def phone_list(path='./', size=(1136, 640)):
    # 利用os.listdir()来获得某个目录下面的所有文件
    for i in os.listdir(path):
        photo_split = i.split('.')
        # 判断是不是图片文件
        if len(photo_split) >= 2 and photo_split[-1] in PHOTO_TYPE:
            # 获得图片的全路径
            photo_dir = os.path.join(path, i)
            avatar = Image.open(photo_dir)
            # 改变图片size
            avatar.resize(size)
            avatar.show()


if __name__ == '__main__':
    phone_list('./')
