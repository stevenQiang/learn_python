# -*- coding: utf-8 -*-

# yield就是生成器，yield的用法就跟return一样；
# 当使用yield的时候，函数并没有运行，函数仅仅返回生成器的对象，这对于函数返回一个很大的集合并且希望只读一次的时候，就会非常方便。
# 生成器的好处，你不需要读这个值两次，


def yield_point2():
    yield "abcd"


def yield_point():
    for i in range(3):
        yield i+i

if __name__ == '__main__':
    a = yield_point2()
    print a
    print a.next()
    print "--------"
    b = yield_point()
    for i in b:
        print i
