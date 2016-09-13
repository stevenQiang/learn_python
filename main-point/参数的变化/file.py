# -*- coding: utf-8 -*-


# 这样的话，a其实指向的是一个内存地址，并不是一个[]
def func(a=[]):
    print a
    a.append(2)
    return a

func()
func()
func()

# 但是在js里不会有这种情况，js是默认值。