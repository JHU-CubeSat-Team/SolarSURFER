#---------
#Imports
#---------

import matplotlib.pyplot as plt
from ADCSsimInit import *
from scipy.integrate import solve_ivp
import math
import numpy as np
import Satellite

#PIE (Yummy)
pi = math.pi

#---------
#Simulation
#---------

print("Simulation Started")

#Get Planet Parameters
R,M,G,mu = planet()

#Initial Conditions
altitude = 254*1.6*1000 #meters

x0 = R+altitude
y0 = 0
z0 = 0
xdot0 = 0
ydot0 = vcircular*math.sin(inclination)
zdot0 = vcircular*math.cos(inclination)
stateinitial = [x0,y0,z0,xdot0,ydot0,zdot0]

#Need time window
semi_major = np.linalg.norm(np.array([x0,y0,z0]))
period = 2*pi/(mu)**(1/2)*(semi_major)**(3/2)
number_of_orbits = 1
tspan = range(number_of_orbits*period)

#Integrate equations of motion
[tout,stateout] = solve_ivp(Satellite,tspan,stateinitial)



