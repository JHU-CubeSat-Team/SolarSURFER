#-----------
#Useful Funtions
#----------


#This will define planet parameters
def planet():
    R = 6.371*10**6 #Meters
    M = 5.972*10**24 #kg
    G = 6.67*10**(-11) #Gravitational Constant (SI)
    mu = G*M

    return R,M,G,mu
