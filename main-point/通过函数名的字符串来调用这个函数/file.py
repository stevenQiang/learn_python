# -*- coding: utf-8 -*-


if __name__ == "__main__":
    dict_func = {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8, 8: 9, 9: 0}
    # getattr做为一个内建函数，hasattr判断有没有这个方法
    # 利用getattr来进行实例绑定，然后来获取对象的相关方法
    result = getattr(dict_func, 'items')
    print result()

