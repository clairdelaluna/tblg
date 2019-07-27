import numpy as np
import matplotlib as plt

a = 1.0
xi = 1.0
l = 5.0*xi
t_0 = 1.0

a_1 = np.array([np.sqrt(3.0)*a , 0.0*a , 0.0*a ])
a_2 = np.array([np.sqrt(3.0)/2*a , 3.0/2.0*a , 0.0*a ])

atom_pos = [  np.array([np.sqrt(3.0)/2.0*a , 1.0/2.0*a , 0.0*a ]), \
           np.array([np.sqrt(3.0)*a , 1.0*a , 0.0*a ])  ]

counter = 0

def tunneling(dist):
    if dist < l:
        return t_0*np.exp(-dist/xi)
    else:
        return 0.0

n_1_max = int(np.ceil(l/(np.sqrt(3)*a))) + 1
n_2_max = int(np.ceil(l/(3.0/2.0*a))) + 1

couplings = [] #(X,Y,t(r),n,m)

for left in [0,1]:
    for right in [0,1]:
        for x in range(0,n_1_max):
            for y in range(0,n_2_max):
                dist = np.linalg.norm( atom_pos[left] + atom_pos[right] + \
                                       x*a_1 + y*a_2 )
                t_r = tunneling(dist)
                if t_r != 0.0:
                    couplings.append([left,right,t_r,x,y])
                else:
                    pass

print(couplings)
    
    
