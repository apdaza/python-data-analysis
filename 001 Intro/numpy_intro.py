#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from numpy import arange

def pythonsum(n):
    a = list(range(n))
    b = list(range(n))
    c = []

    for i in range(len(a)):
        a[i] = i ** 2
        b[i] = i ** 3
        c.append(a[i] + b[i])

    return c

def numpysum(n):
    a = arange(n) ** 2
    b = arange(n) ** 3
    c = a + b
    return c

print(pythonsum(5))

print(numpysum(5))
