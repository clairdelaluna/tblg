import numpy as np
import matplotlib.pyplot as plt

a = 1.0
xi = 1.0
l = 1.1*xi
t_0 = 1.0

a_1 = np.array([np.sqrt(3.0)*a , 0.0*a , 0.0*a ])
a_2 = np.array([np.sqrt(3.0)/2*a , 3.0/2.0*a , 0.0*a ])

atom_pos = [np.array([np.sqrt(3.0)/2.0*a , 1.0/2.0*a , 0.0*a ]), \
            np.array([np.sqrt(3.0)*a , 1.0*a , 0.0*a ])]

counter = 0

def tunneling(dist):
    if dist < l:
        return t_0*np.exp(-dist/xi)
    else:
        return 0.0

def relative_dist(left,right):
    if left == right:
        return np.array([0.0,0.0,0.0])
    elif left == 0 and right == 1:
        return atom_pos[1] - atom_pos[0]
    elif left == 1 and right == 0:
        return atom_pos[0] - atom_pos[1]

n_1_max = int(np.ceil(l/(np.sqrt(3)*a))) + 1
n_2_max = int(np.ceil(l/(3.0/2.0*a))) + 1

couplings = [] #(X,Y,t(r),n,m)

for left in [0,1]:
    for right in [0,1]:
        for x in range(0,n_1_max):
            for y in range(0,n_2_max):
                if x == 0 and y == 0 and left == right:
                    pass
                elif x == 0 and y == 0 and left == 1:
                    pass
                else:
                    dist = np.linalg.norm( relative_dist(left,right) + \
                                           x*a_1 + y*a_2 )
                    t_r = tunneling(dist)
                    if t_r != 0.0:
                        couplings.append([left,right,t_r,x,y])
                    else:
                        pass

for x in range(0,n_1_max):
    for y in range(0,n_2_max):
        plt.scatter( (atom_pos[0] + x*a_1 + y*a_2)[0], \
                     (atom_pos[0] + x*a_1 + y*a_2)[1] )
        plt.scatter( (atom_pos[1] + x*a_1 + y*a_2)[0], \
                     (atom_pos[1] + x*a_1 + y*a_2)[1] )

tunnelings = []

for c in couplings:
    tunnelings.append(c[2])

max_tunnel = max(tunnelings)

cmap = plt.get_cmap('seismic')
for c in couplings:
    col = cmap(c[2]/max_tunnel)
    plt.plot( [ atom_pos[c[0]][0] , (atom_pos[c[1]]+c[3]*a_1+c[4]*a_2)[0] ] , \
              [ atom_pos[c[0]][1] , (atom_pos[c[1]]+c[3]*a_1+c[4]*a_2)[1] ], \
              color = col, alpha=0.5)

plt.axes().set_aspect('equal')
plt.show()


