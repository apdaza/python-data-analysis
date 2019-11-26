#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from numpy import *

#creating an array
a = arange(5)
print(a)
print(a.dtype)
print(a.shape)

#creating a multidimensional array
m = array([arange(2),arange(2)])
print(m)
print(m.dtype)
print(m.shape)

#selecting NumPy array elements
a = array([[1,2],[3,4]])
print(a)
print(a[0,0])
print(a[0,1])
print(a[1,0])
print(a[1,1])
print(a[0])
print(a[1])

#slicing and indexing
a = arange(9)
print(a[3:7])
print(a[:7:2])
print(a[::-1])
