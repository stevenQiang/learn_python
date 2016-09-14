# -*- coding: utf-8 -*-


# 把字符串分割,10一个
def change_list(list_a):
    return {i: list_a[i: i+10] for i in xrange(0, len(list_a), 10)}

if __name__ == "__main__":
    print change_list(range(100))
