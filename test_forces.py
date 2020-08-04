# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 10:16:50 2020

@author: Travis_Whyte
"""

import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import spsolve
import params, gauge_ferm_utils, dirac_algebra, dirac_ops, forces

nx, nt, N, vol, beta, mass = params.lattice_params()
u, theta0 = gauge_ferm_utils.unit_gauge(vol) 

#print(u)

psi = gauge_ferm_utils.unit_pseudoferm_wilson(vol)
M = dirac_ops.wilson(mass, N, vol, u)
phi = csr_matrix.getH(M).dot(psi)


eta = spsolve(dirac_ops.wilson(mass, N, vol, u), phi)
chi = spsolve(csr_matrix.getH(dirac_ops.wilson(mass, N, vol, u)), eta)

#ff = forces.wilson_force(N, vol, eta, chi, u)

#print(ff.shape)

#gf = forces.gauge_force(N, vol, th)

#print(gf.shape)

kp, km = gauge_ferm_utils.nearest_neighbor(N, vol)

theta = theta0[:, 0] + theta0[kp[:,0], 1] - theta0[:, 1] - theta0[kp[:,1], 1]

#print(theta)

p = gauge_ferm_utils.generate_momenta(vol)
print(p)



