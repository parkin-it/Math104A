#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 16:35:00 2016

@author: Nathan A Cheadle
"""

import OneVariableSolution as OVS

print("Bisection: ")
p_out = OVS.bisection(.25,2,"x**2-2*x+1")
print("Final Guess = " + str(p_out))

print("Fixed Point Iteration: ")
p_out = OVS.fixedpoint(.5,"x**2")
print("Final Guess = " + str(p_out))

print("Newton-Secant: ")
p_out = OVS.newtonSecant(.95, .97, "x**2-2*x+1")
print("Final Guess = " + str(p_out))

print("Newton: ")
p_out = OVS.newton(.95,"x**2-2*x+1", "2*x-2")
print("Final Guess = " + str(p_out))