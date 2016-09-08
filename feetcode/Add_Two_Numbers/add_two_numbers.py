# -*- coding: utf-8 -*-

# 链表操作
# 当情况为0, 0的时候，当情况为5, 5,出错


class ListNode(object):
    def __init__(self, x):
        self.val = x  # 信息域
        self.next = None  # 指针域


def add(l1, l2):
    result = ListNode(0)
    current = result
    total = 0
    output = []
    while l1 or l2 or total != 0:
        val = total
        if l1:
            val += l1.val
            l1 = l1.next
        if l2:
            val += l2.val
            l2 = l2.next
        total, val = val / 10, val % 10
        current.next = ListNode(val)
        current = current.next
        print total
        output.append(val)
    print output
    return output


if __name__ == '__main__':
    a = ListNode(5)
    b = ListNode(5)
    add(a, b)
