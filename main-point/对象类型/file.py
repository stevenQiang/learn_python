# -*- coding: utf-8 -*-

# 查看一个对象的类型
a = [1, 2, 4]
print type(a)

# 或者可以用另外一个内建函数isinstance()，因为接受派生类
print isinstance(a, list)
print isinstance(a, (list, tuple))
