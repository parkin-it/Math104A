#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 15:25:14 2016

@author: Nathan A Cheadle
"""

import sys
sys.path.insert(0, '/Users/oracle/Python/Math104A/SolutionOneVariable/')

import OneVariableSolution as OVS
import numpy as np

l = 89 #inches
h = 49 #inches
D = 55 #inches
beta_1 = 11.5*np.pi/180 #radians

A = l*np.sin(beta_1)
B = l*np.cos(beta_1)
C = (h+05.*D)*np.sin(beta_1)-0.5*D*np.tan(beta_1)
E = (h+0.5*D)*np.cos(beta_1)-0.5*D



equation = str(A)+"*np.sin(x)*np.cos(x)+"+str(B)+"*np.sin(x)**2-"+str(C)+"*np.cos(x)-"+str(E)+"*np.sin(x)"
derivative = str(A)+"*np.cos(2*x)+"+str(B)+"*np.sin(2*x)+"+str(C)+"*np.sin(x)-"+str(E)+"*np.cos(x)"

p_out = OVS.newton(33*np.pi/180,equation, derivative) #in radians
print("f(p_out) = "+ str(OVS.f_x(equation,p_out)))
p_out = p_out*180/np.pi
print("Estimate using initial given values: " + str(p_out))

D = 30 #inches

C = (h+05.*D)*np.sin(beta_1)-0.5*D*np.tan(beta_1)
E = (h+0.5*D)*np.cos(beta_1)-0.5*D



equation = str(A)+"*np.sin(x)*np.cos(x)+"+str(B)+"*np.sin(x)**2-"+str(C)+"*np.cos(x)-"+str(E)+"*np.sin(x)"
derivative = str(A)+"*np.cos(2*x)+"+str(B)+"*np.sin(2*x)+"+str(C)+"*np.sin(x)-"+str(E)+"*np.cos(x)"

p_out = OVS.newton(58.5*np.pi/180,equation, derivative) #in radians
print("f(p_out) = "+ str(OVS.f_x(equation,p_out)))
p_out = p_out*180/np.pi
print("Estimate using initial given values: " + str(p_out))