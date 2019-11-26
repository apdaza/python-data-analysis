#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from numpy import *
"""
-------------------------------------------------------------
Type                                Character code
-------------------------------------------------------------
integer                             i
Unsigned integer                    u
Single precision float              f
Double precision float              d
bool                                b
complex                             D
string                              S
unicode                             U
Void                                V
"""

af = arange(7, dtype='f')
print(af)
print(af.dtype)

ac = arange(7, dtype='D')
print(ac)
print(ac.dtype)

print(sctypeDict.keys())

t = dtype('float64')
print(t.char)
print(t.type)
print(t.str)