
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from datetime import datetime
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

if len(sys.argv) > 1:
    size = int(sys.argv[1])
else:
    size = 10000

start = datetime.now()
c = pythonsum(size)
delta = datetime.now() - start
print("the last 2 elements of de sum", c[-2:])
print("PythomSum elapsed time in microseconds", delta.microseconds)

start = datetime.now()
c = numpysum(size)
delta = datetime.now() - start
print("the last 2 elements of de sum", c[-2:])
print("NumpySum elapsed time in microseconds", delta.microseconds)
