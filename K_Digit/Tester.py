#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 13:02:50 2016

@author: oracle
"""

import k_digit

x = -1235     
y = 1000.5

x1 = k_digit.chop(x,3)
print(x1)

x2 = k_digit.round(x,3)
print(x2)

x3 = k_digit.add(x,y,3)
x4 = k_digit.add(x,y,3,"chop")
print(x3)
print(x4)

x5 = k_digit.subtract(x,y,3)
x6 = k_digit.subtract(x,y,3,"chop")
print(x5)
print(x6)

x7 = k_digit.multiply(x,y,3)
x8 = k_digit.multiply(x,y,3,"chop")
print(x7)
print(x8)

x9 = k_digit.divide(x,y,3)
x10 = k_digit.divide(x,y,3,"chop")
print(x9)
print(x10)

x11 = k_digit.factorial(10,3)
x12 = k_digit.factorial(10,3,"chop")
print(x11)
print(x12)