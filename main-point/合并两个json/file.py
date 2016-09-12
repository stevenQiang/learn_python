# -*- coding: utf-8 -*-

x = {'a': 1, 'b': 2}
y = {'c': 3, 'd': 4}
# 合并两个字符串，利用元组方式
print dict(x.items()+y.items())

# 合并两个字符串，利用update方法，最后值存到x
x.update(y)
print x
