# -*- coding: utf-8 -*-

# operator模块提供的itemgetter函数用于获取对象的哪些维的数据
import operator

x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# operator.itemgetter(1) 代表的是值，0代表的是key
result = sorted(x.items(), key=operator.itemgetter(1))
print result
