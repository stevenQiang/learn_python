# -*- coding: utf-8 -*-


# 在python里面要注意的是，当你传一个值到一个函数里面去，然后修改了那个值之后，原来的那个值也会改变，因为相当于指向了同一个内存地址。
def change_attr(the_list):
    print "before,change in def: ", the_list
    the_list.append("11111")
    print "after,change in def: ", the_list

the_list = [1, 2, 3, 4]
change_attr(the_list)
print the_list
