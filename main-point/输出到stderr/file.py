# -*- coding: utf-8 -*-
import sys
from __future__ import print_function

# 重定向标准错误信息
sys.stderr.write("this is test")

print('WRANING:', file=sys.stderr)
