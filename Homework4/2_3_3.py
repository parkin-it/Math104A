#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 16:01:20 2016

@author: Nathan A Cheadle
"""

import sys
sys.path.insert(0, '/Users/oracle/Python/Math104A/SolutionOneVariable/')

import OneVariableSolution as OVS

p_out = OVS.newton(1, "x**2-6", "2*x")
print("Final Guess = " + str(p_out))

p_out = OVS.newtonSecant(3,2,"x**2-6")
print("Final Guess = " + str(p_out))

p_out = OVS.newtonFalse(3,2,"x**2-6")
print("Final Guess = " + str(p_out))