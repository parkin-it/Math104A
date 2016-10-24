#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 13:48:28 2016

@author: Nathan A Cheadle
"""

import sys
sys.path.insert(0, '/Users/oracle/Python/Math104A/SolutionOneVariable/')

import OneVariableSolution as OVS
import numpy as np

print("--------------A---------------")
p_out = OVS.newtonFalse(1,2,"np.exp(x)+2**(-x)+2*np.cos(x)-6",10e-5)
print("Final Guess = " + str(p_out))

print("--------------B---------------")
p_out = OVS.newtonFalse(1.3,2,"np.log(x-1)+np.cos(x-1)",10e-5)
print("Final Guess = " + str(p_out))

print("--------------C---------------")
p_out = OVS.newtonFalse(2,3,"2*x*np.cos(2*x)-(x-2)**2",10e-5)
print("Final Guess = " + str(p_out))
p_out = OVS.newtonFalse(3,4,"2*x*np.cos(2*x)-(x-2)**2",10e-5)
print("Final Guess = " + str(p_out))

print("--------------D---------------")
p_out = OVS.newtonFalse(1,2,"(x-2)**2-np.log(x)",10e-5)
print("Final Guess = " + str(p_out))
p_out = OVS.newtonFalse(np.exp(1),4,"(x-2)**2-np.log(x)",10e-5)
print("Final Guess = " + str(p_out))

print("--------------E---------------")
p_out = OVS.newtonFalse(0,1,"np.exp(x)-3*x**2",10e-5)
print("Final Guess = " + str(p_out))
p_out = OVS.newtonFalse(3,5,"np.exp(x)-3*x**2",10e-5)
print("Final Guess = " + str(p_out))

print("--------------F---------------")
p_out = OVS.newtonFalse(0,1,"np.sin(x)-np.exp(-x)",10e-5)
print("Final Guess = " + str(p_out))
p_out = OVS.newtonFalse(3,4,"np.sin(x)-np.exp(-x)",10e-5)
print("Final Guess = " + str(p_out))
p_out = OVS.newtonFalse(6,7,"np.sin(x)-np.exp(-x)",10e-5)
print("Final Guess = " + str(p_out))