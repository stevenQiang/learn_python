# -*- coding: utf-8 -*-
import os
file_dir = os.path.dirname('./test/test')
# 用来判断文件夹存不存在
if os.path.exists(file_dir):
    print "存在"
else:
    print "不存在"
    # 创建文件夹
    os.makedirs(file_dir)
