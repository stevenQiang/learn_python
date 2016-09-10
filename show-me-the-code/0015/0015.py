# -*- coding: utf-8 -*-
# 第 0015 题： 纯文本文件 city.txt为城市信息, 里面的内容（包括花括号）如下所示：
# Python中一般使用xlrd库来读取Excel文件，使用xlwt库来生成Excel文件，使用xlutils库复制和修改Excel文件。
from xlwt import *
import json


def write_xlr():
    f = open('city.txt', 'rb')
    # 利用json.load()转成json格式
    read_result = json.load(f)
    book = Workbook()
    sheet = book.add_sheet('city')
    for index, value in enumerate(read_result):
        sheet.write(index, 0, value)
        sheet.write(index, 1, read_result[value])
    book.save('city.xls')


if __name__ == "__main__":
    write_xlr()
