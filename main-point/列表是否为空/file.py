# -*- coding: utf-8 -*-
# 判断是否为空，用这个上方法最好


def list_empty(a):
    if a:
        print "a not empty"
    else:
        print "a is empty"

if __name__ == "__main__":
    list_empty([1])
    list_empty({'a': 1})
