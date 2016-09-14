# -*- coding: utf-8 -*-

# http://www.cnblogs.com/pylemon/archive/2011/05/18/2050179.html
# strip 去掉字符串左边和右边的,
# rstrip 去掉字符串右边的
# lstrip 去掉字符串左边的
# 用法：
a = "yes a b"
# 会把ye解析成一个list,['y','e']，然后开始遍历，如果出现在这个list的话，就去掉
a.strip('ye')
# 结果: 's a b'
