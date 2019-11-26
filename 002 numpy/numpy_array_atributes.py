#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from numpy import *
b = arange(24).reshape(2, 12)
print(b)
print(b.ndim)
print(b.size)
print(b.itemsize)
print(b.nbytes)
print(b.size * b.itemsize)

b.resize(6,4)
print(b)
print(b.T)
print(b.ndim)
