# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 11:51:25 2020

@author: Travis_Whyte
"""

import params, gauge_ferm_utils, dirac_ops
import numpy as np
from scipy.sparse.linalg import eigs

if __name__ == '__main__':
    
    nx, nt, N, vol, beta, mass = params.lattice_params()
    #print out params
    """
    nmd, tau = params.moldyn_params()
    nmc, warmup, num_warmup = params.HMC_params()
    """
    
    #u = gauge_ferm_utils.random_gauge(vol)
    
    #M = dirac_ops.wilson(mass,N,vol,u)
    
    #evals, evecs = eigs(M,10)
    
    #print(np.sort(evals, axis=None))
    
    kp, km = gauge_ferm_utils.nearest_neighbor(N, vol)
    print(kp)
    print(km)
    
    