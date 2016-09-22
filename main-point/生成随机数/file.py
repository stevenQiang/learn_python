# -*- coding: utf-8 -*-
import random, string


def get_random_data():
    print ''.join([random.choice(string.letters + string.digits) for i in xrange(6)])


if __name__ == '__main__':
    get_random_data()
