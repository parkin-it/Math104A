#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 16:11:24 2016

@author: Nathan A Cheadle
"""

import math
import numpy as np

def bisection(bound_down, bound_up, function, Tol=1e-3, MaxIter=20):
    error = 1
    
    f_x_down = f_x(function, bound_down)    
    
    i = 1
    
    while error >= Tol and i <= MaxIter:
        
        p_n = (bound_up + bound_down)/2
        f_x_p = f_x(function, p_n)
        print("P_"+str(i)+ " = " + str(p_n))
        print("F(p_"+str(i)+ ") = " + str(f_x_p))
        error = abs(bound_up-bound_down)/2
        print("Error at iteration " + str(i) + " = " + str(error))
        
        if f_x_p == 0:
            error = 0
        elif f_x_down*f_x_p > 0:
            bound_down = p_n
            f_x_down = f_x_p
        else:
            bound_up = p_n
        i = i + 1
        
    return p_n
            
# Input function in terms of x and give a value of x to evaluate at 
def f_x(function, x):
    
    f_x_pn = eval(function)
    
    return f_x_pn
    
def fixedpoint(guess, function, Tol=1e-3, MaxIter=20):
    error = 1
    
    p_n = guess
    
    i = 1
    
    while error >= Tol and i <= MaxIter:
        p = f_x(function,p_n)
        i = i+1
        error = abs(p-p_n)
        print("P_"+str(i)+ " = " + str(p_n))
        print("F(p_"+str(i)+ ") = " + str(p))
        print("Error at iteration " + str(i) + " = " + str(error))
        
        p_n = p
        
    return p_n