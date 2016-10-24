#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 15:02:50 2016

@author: Nathan A Cheadle
"""

import sys
sys.path.insert(0, '/Users/oracle/Python/Math104A/SolutionOneVariable/')

import OneVariableSolution as OVS
import numpy as np

p_out = OVS.newton(.03,"(1500/x)*((1+x)**240-1)-750000","(-1500/x**2)*((1+x)**240-1)+(1500/x)*(240*(1+x)**239)")
print("Interest Rate = " + str(p_out))