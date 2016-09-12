# -*- coding: utf-8 -*-
from enum import Enum


class Animals(Enum):
    ant = 1
    dog = 2
    cat = 3

animals = Animals
print animals.cat
