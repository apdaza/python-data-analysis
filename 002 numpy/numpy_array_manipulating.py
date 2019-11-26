#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from numpy import *

#Manipulating array shapes
b = arange(24).reshape(2,3,4)
print(b)
print(b.ravel())
print(b.flatten())
b.shape = (6,4)
print(b)
print(b.transpose())
b.resize((2,12))
print(b)

#Stacking arrays
a = arange(9).reshape(3,3)
print(a)
b = 2 * a
print(b)
c = arange(2)
print(c)
d = 2 * c
print(d)
#Horizontal stacking
print(hstack((a, b)))
print(concatenate((a, b), axis=1))
#Vertical stacking
print(vstack((a, b)))
print(concatenate((a, b), axis=0))
#depth stacking
print(dstack((a, b)))
#colum_stack
print(column_stack((c, d)))
print(column_stack((a, b)))
#row_stack
print(row_stack((c, d)))
print(row_stack((a, b)))
#Splitting NumPy arrays
print(hsplit(a,3))
print(split(a, 3, axis=1))

print(vsplit(a,3))
print(split(a, 3, axis=0))

c = arange(27).reshape(3, 3, 3)
print(c)
print(dsplit(c, 3))