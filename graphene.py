import numpy as np
import matplotlib as plt

a = 1.0
xi = 3.0
t_0 = 1.0

a_1 = np.array([np.sqrt(3.0)*a , 0.0*a , 0.0*a ])
a_2 = np.array([np.sqrt(3.0)/2*a.0 , 3.0/2.0*a , 0.0*a ])

atom_1 = np.array([np.sqrt(3.0)/2.0*a , 1.0/2.0*a , 0.0*a ])
atom_2 = np.array([np.sqrt(3.0)*a , 1.0*a , 0.0*a ])

counter = 0

def tunneling(dist):
    if dist < 5.0*xi:
        return t_0*exp(-dist/xi)
    else:
        return 0.0

n_1 = 0
n_2 = 0

while counter < 1:
    
