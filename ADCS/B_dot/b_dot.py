import numpy as np

#----------------------
#Magnetorquer Parameters (THIS CAN MOVE ELSEWHERE (GLOBAL))
n = 84 #Number of coils
A = 0.02 #Area of magnetorquer
#-----------------------

def bDotControl(BfieldNav,omegaNav): #Returns current that should be outputted to magnetorquers
    
    #-------------------
    #k is gain constant
    #CHANGE THIS LATER
    k = 5*10**9

    #BfieldNav in Teslas
    #omegaNav is in rad/s
    #muB = n*I*A
    #----------------------

    #The only actual code
    current = k*np.cross(omegaNav,BfieldNav)/(n*A)

    return current