#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from numpy import *

"""
-------------------------------------------------------------------------------
Type                    Description
-------------------------------------------------------------------------------
bool                    Boolean (True or False) stored as a bit
inti                    Platform integer (normally either int32 or int64)
int8                    Byte (-128 to 127)
int16                   Integer (-32768 to 32767)
int32                   Integer (-2 ** 31 to 2 ** 31 -1)
int64                   Integer (-2 ** 63 to 2 ** 63 -1)
uint8                   Unsigned integer (0 to 255)
uint16                  Unsigned integer (0 to 65535)
uint32                  Unsigned integer (0 to 2 ** 32 - 1)
uint64                  Unsigned integer (0 to 2 ** 64 - 1)
float16                 Half precision float: sign bit, 5 bits exponent, and 10 bits mantissa
float32                 Single precision float: sign bit, 8 bits exponent, and 23 bits mantissa
float64 or float        Double precision float: sign bit, 11 bits exponent, and 52 bits mantissa
complex64               Complex number, represented by two 64-bit floats (real and imaginary components)         
complex128 or complex   Complex number, represented by two 32-bit floats (real and imaginary components)
"""

f = float64(42)
print(f)
i = int8(42.8)
print(i)
b = bool(0)
print(b)
ft = float(True)
print(ft)
ff = float(False)
print(ff)

a = arange(7, dtype=uint16)
print(a)
print(a.dtype)