#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 17:41:06 2016

@author: Nathan A Cheadle
"""
import sys
sys.path.insert(0, '/Users/oracle/Python/Math104A/SolutionOneVariable/')

import OneVariableSolution as OVS

p_out = OVS.bisection(1,0,"math.sqrt(x)-math.cos(x)")

print("Final Guess = " + str(p_out))