# -*- coding: utf-8 -*-
# 求相对应范围里面的回文，并且所有数不大于n


# 判断是不是回文
def palindrome(a):
    a = str(a)
    len_a = len(a)
    for i in range(int(len_a/2)):
        if a[i] != a[len_a - i - 1]:
            return False
    return True


def number_sum(number, maxNumber):
    total = 0
    for i in str(number):
        total += int(i)
    return maxNumber >= total >= 5


def func(n):
    result_list = []
    for i in range(10000, 1000000):
        if palindrome(i) and number_sum(i, n):
            result_list.append(i)
    return result_list

if __name__ == '__main__':
    result = func(52)
    print(result, len(result))
