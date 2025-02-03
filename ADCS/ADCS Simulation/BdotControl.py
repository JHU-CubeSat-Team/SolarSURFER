import numpy as np
import matplotlib.pyplot as plt

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


#-----------
#TESTING (COMMENT OUT LATER)
#------------

#Constants and initial conditions
omega = [0.1,0.1,0.1]
B = [-10**(-5),10**(-5),-10**(-5)]
i1 = [865,0,0]
i2 = [0,433,0]
i3 = [0,0,433]
I = np.array([i1,i2,i3])



#Simple test of simulation and B-dot algorithm
def runSim(dt,omega0,B,I,time):
    #Define initial velocity, get moment of inertia
    omega = omega0
    omega_hist = [[],[],[]]
    Iinv = np.linalg.inv(I)

    #Loop for each timestep
    for time in range(int(time/dt)):

        #Calculate current necessary using algorithim
        current = bDotControl(B,omega)

        #Calculate dipole from current
        muB = current*n*A

        #Calculate torque from dipole in magnetic field
        torque = np.cross(muB,B)

        #Calculate angular acceleration
        acc = Iinv @ torque

        #Add old angular velocities to history
        omega_hist[0].append(omega[0])
        omega_hist[1].append(omega[1])
        omega_hist[2].append(omega[2])

        #Update angular velocity with angular acceleration and timestep
        omega = np.add(omega,acc*dt)
    
    return omega_hist

data = runSim(1,omega,B,I,1000)

#Plot the things
plt.plot(data[0],label='Wx')
plt.plot(data[1],label='Wy')
plt.plot(data[2],label='Wz')
plt.xlabel("Time (s)")
plt.ylabel("Angular Velocity (rad/s)")
plt.title("Bdot detumbing test")
plt.legend()
plt.show()