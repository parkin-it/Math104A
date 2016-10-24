#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 16:11:24 2016

@author: Nathan A Cheadle
"""

import math
import numpy as np

def bisection(bound_down, bound_up, function, Tol=1e-3, MaxIter=20):
    
    #Set initial values and evaluate the value at the lower bound
    error = Tol*2
    f_x_down = f_x(function, bound_down)    
    i = 1
    
    #Run while the error is less than the tolerance, and i is less than i_max
    while error >= Tol and i <= MaxIter:
        
        #find p_n and evaluate at it's value inside of the function
        p_n = bound_down + (bound_up - bound_down)/2
        f_x_p = f_x(function, p_n)
        
        print("P_"+str(i)+ " = " + str(p_n))
        print("F(p_"+str(i)+ ") = " + str(f_x_p))
        #Find the error of p_n
        error = abs(bound_up-bound_down)/2
        print("Error at iteration " + str(i) + " = " + str(error))
        
        #Decide whether to replace the upper or lower bound
        if f_x_p == 0:
            error = 0
        elif f_x_down*f_x_p > 0:
            bound_down = p_n
            f_x_down = f_x_p
        else:
            bound_up = p_n
        i = i + 1
    
    #Return the final value to the function
    return p_n
            
# Input function in terms of x and give a value of x to evaluate at 
def f_x(function, x):
    
    f_x_pn = eval(function)
    
    return f_x_pn

#Use the fixed point method using an initial guess and a given function
def fixedpoint(guess, function, Tol=1e-3, MaxIter=20):
    
    #Set initial Values to Variables
    error = Tol*2
    p_n = guess
    i = 1
    
    #Run while the error is less than the tolerance, and the value of p_n is less than 10e4
    while error >= Tol and i <= MaxIter and abs(p_n) <= 10e4:
        #Evaluate p at the next value and find error between previous value
        p = f_x(function,p_n)
        error = abs(p-p_n)
        print("P_"+str(i)+ " = " + str(p_n))
        #print("F(p_"+str(i)+ ") = " + str(p))
        print("Error at iteration " + str(i) + " = " + str(error))
        
        #Set next value of p_n and increment i
        p_n = p
        i = i+1
     
    #return final value of function
    return p_n

#Use Newton's method to evaluate zero of function
def newton(p_0, function, derivative, Tol=1e-3, MaxIter=20):
    #Set initial valuables to variables
    i = 1
    error = Tol*2
    print("p_0 = " + str(p_0))
    
    while i <= MaxIter and error >= Tol:
        p = p_0 - f_x(function,p_0)/f_x(derivative,p_0)
        
        print("p_"+str(i)+" = " + str(p))
        #print("f(p_"+str(i)+") = " + str(f_x(function,p_0)))
        #print("f_prime(p_"+str(i)+") = " + str(f_x(derivative,p_0)))
        error = abs(p-p_0)
        print("Error at iteration " + str(i) + " = " + str(error))
        i = i+1
        p_0 = p
    
    return p
    

#Use Newton-Secant method to evaluate zero of function
def newtonSecant(p_0, p_1, function, Tol=1e-3, MaxIter=20):
    
    #Set initial values to variables
    error = Tol*2
    i = 2
    print("p_0 = " + str(p_0))
    print("p_1 = " + str(p_1))
    q_0 = f_x(function, p_0)
    q_1 = f_x(function, p_1)
    #print("q_0 = " + str(q_0))
    #print("q_1 = " + str(q_1))
    
    #Run Newton-Secant method until error is less than desired, and i doesn't 
    #exceed the max number of iterations
    while i <= MaxIter and error >= Tol:
        p = p_1 - q_1*(p_1-p_0)/(q_1-q_0)
        error = abs(p-p_1)
        i = i+1
        p_0 = p_1
        p_1 = p
        q_0 = q_1
        q_1 = f_x(function, p)
        print("p_"+str(i)+ " = " + str(p))
        #print("q_"+str(i)+ " = " + str(q_1))
        print("Error at iteration " + str(i) + " = " + str(error))
    
    return p
    
#Use False Proposition method to evaluate zero of a function
def newtonFalse(p_0, p_1, function, Tol=1e-3, MaxIter=50):
    
    #Set initial values of variables
    error = Tol*2
    i = 2
    print("p_0 = " + str(p_0))
    print("p_1 = " + str(p_1))
    q_0 = f_x(function, p_0)
    q_1 = f_x(function, p_1)
    #print("q_0 = " + str(q_0))
    #print("q_1 = " + str(q_1))
    
    #Run False Prop method until error is less than desired, and i doesn't 
    #exceed the max number of iterations
    while i <= MaxIter and error >= Tol:
        p = p_1 - q_1*(p_1-p_0)/(q_1-q_0)
        error = abs(p-p_1)
        i = i+1
        q = f_x(function,p)
        
        if q*q_1 < 0:
            p_0 = p_1
            q_0 = q_1
        
        p_1 = p
        q_1 = q
        print("p_"+str(i)+ " = " + str(p))
        #print("q_"+str(i)+ " = " + str(q_1))
        print("Error at iteration " + str(i) + " = " + str(error))
        
    return p