#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 14:13:15 2016

@author: Nathan A Cheadle
"""

import sys
sys.path.insert(0, '/Users/oracle/Python/Math104A/SolutionOneVariable/')

import OneVariableSolution as OVS
import numpy as np

print("--------------A---------------")
print("----Newton's Method----")
p_out = OVS.newton(1.5,"x**2-4*x+4-np.log(x)","2*x-4-(1/x)",10e-7)
print("Final Guess = " + str(p_out))
p_out = OVS.newton(3,"x**2-4*x+4-np.log(x)","2*x-4-(1/x)",10e-7)
print("Final Guess = " + str(p_out))
print("----Newton Secant Method----")
p_out = OVS.newtonSecant(1,2,"x**2-4*x+4-np.log(x)",10e-7)
print("Final Guess = " + str(p_out))
p_out = OVS.newtonSecant(2,4,"x**2-4*x+4-np.log(x)",10e-7)
print("Final Guess = " + str(p_out))
print("----False Proposition Method----")
p_out = OVS.newtonFalse(1,2,"x**2-4*x+4-np.log(x)",10e-7)
print("Final Guess = " + str(p_out))
p_out = OVS.newtonFalse(2,4,"x**2-4*x+4-np.log(x)",10e-7)
print("Final Guess = " + str(p_out))

print("--------------B---------------")
print("----Newton's Method----")
p_out = OVS.newton(.25,"x+1-2*np.sin(np.pi*x)","1-2*np.pi*np.cos(np.pi*x)",10e-7)
print("Final Guess = " + str(p_out))
p_out = OVS.newton(.75,"x+1-2*np.sin(np.pi*x)","1-2*np.pi*np.cos(np.pi*x)",10e-7)
print("Final Guess = " + str(p_out))
print("----Newton Secant Method----")
p_out = OVS.newtonSecant(0,.5,"x+1-2*np.sin(np.pi*x)",10e-7)
print("Final Guess = " + str(p_out))
p_out = OVS.newtonSecant(.5,1,"x+1-2*np.sin(np.pi*x)",10e-7)
print("Final Guess = " + str(p_out))
print("----False Proposition Method----")
p_out = OVS.newtonFalse(0,.5,"x+1-2*np.sin(np.pi*x)",10e-7)
print("Final Guess = " + str(p_out))
p_out = OVS.newtonFalse(.5,1,"x+1-2*np.sin(np.pi*x)",10e-7)
print("Final Guess = " + str(p_out))