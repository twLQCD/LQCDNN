# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 15:28:51 2020

@author: Travis_Whyte
"""

# if you are looking for bicg, bicgstab, cg, cgs, gmres,  or minres
# see the documentation at https://docs.scipy.org/doc/scipy/reference/sparse.linalg.html
# they are built in to the scipy package

import params, dirac_ops
import numpy as np
import scipy.sparse.linalg as LA
from scipy.sparse import csr_matrix, lil_matrix, tocsr

def gmresdr(u, b, m, k, tol, cyclim):
    
    nx, nt, N, vol, beta, mass = params.lattice_params()
    n = b.shape[0]
    cycle = 1
    j = 1
    mvps = []
    mvp = 0
    
    v = lil_matrix((n,m))
    c = lil_matrix((m+1,1))
    
    rninit = np.linalg.norm(b)
    rn = rninit
    r = b
    v[:,0] = (1/rninit)*b
    c[0,0] = rninit
    c = tocsr(c)
    
    while ( rn > tol and cycle <= cyclim):
        
        while j <= m:
            
            wv = dirac_ops.wilson(mass, N, vol, u).dot(b)
            mvp += 1
            mvps = np.append(mvps, mvp)
            
            vnf = np.linalg.norm(wv)
            
            for i in range(j):
                
    
    