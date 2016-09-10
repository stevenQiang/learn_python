# -*- coding: utf-8 -*-
# 第 0016 题： 纯文本文件 numbers.txt, 里面的内容（包括方括号）如下所示：
# Python中一般使用xlrd库来读取Excel文件，使用xlwt库来生成Excel文件，使用xlutils库复制和修改Excel文件。
from xlwt import *
import json


def write_xlr():
    with open('numbers.txt', 'r') as f:
        # 利用json.loads()转成list格式
        read_result = f.read().decode('utf-8')
        read_result = json.loads(read_result)
        book = Workbook()
        sheet = book.add_sheet('numbers')
        for index, value in enumerate(read_result):
            print index, value
            for i, j in enumerate(value):
                sheet.write(index, i, j)
        book.save('numbers.xls')


if __name__ == "__main__":
    write_xlr()
