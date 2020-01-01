# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 20:15:48 2019
timeDilator calculates the relativistic time dilation between two reference
frames. This is an application of Einstein's special relativity and can be used
to compute the time passed in either frame of reference, moving or stationary.
No units necessarry for the time input. The velocity input must be in meters
per second to give correct answers.
@author: Erik Larsen
"""
import numpy as np
import scipy.constants

def timeDilator():
    t=float(input("Please input the time passed: "))
    framer=str(input("Is this time the proper time? Y/N: "))
    c=scipy.constants.c
    v=float(input("What is the speed, v(m/s)? "))
    if v>=c:
        v=0
        print('Einstien shames you. You must choose a value lower than',c)
        v=float(input("Please enter your speed: "))
        if v>=c:
            quit()
    
    gamma=np.round(1/np.sqrt(1-(v/c)**2),3)
    print("The Lorentz transformation factor \u03B3=",gamma)
    if framer=='Y':
        temp=np.round(gamma*t,6)
        print("t'=",temp,"\nThe stationary frame's clock shows more time passed.")
    else:
        temp=np.round(t/gamma,6)
        print("tproper=",temp,"\nThe moving clock shows less time passed.")
    
    
    