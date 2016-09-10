# -*- coding: utf-8 -*-
# 第 0014 题： 纯文本文件 student.txt为学生信息, 里面的内容（包括花括号）如下所示：
# Python中一般使用xlrd库来读取Excel文件，使用xlwt库来生成Excel文件，使用xlutils库复制和修改Excel文件。
from xlwt import *
import json


def write_xlr():
    f = open('student.txt', 'rb')
    read_result = json.load(f)
    book = Workbook()
    sheet = book.add_sheet('student')
    for index, value in enumerate(read_result):
        sheet.write(index, 0, value)
        for i, j in enumerate(read_result[value]):
            sheet.write(index, i+1, j)
    book.save('test.xls')


if __name__ == "__main__":
    write_xlr()
