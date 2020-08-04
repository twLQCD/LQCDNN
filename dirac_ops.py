# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 12:16:26 2020

@author: Travis_Whyte
"""

import numpy as np
import dirac_algebra
from scipy.sparse import csr_matrix, diags, lil_matrix, kron, eye

def wilson(mass,N,vol,u):
    
    p1p, p1m, p2p, p2m = dirac_algebra.project_ops()
    
    v1 = np.reshape(u[:,0], (N,N), order='F') #fortran ordering
    v2 = np.reshape(u[:,1], (N,N), order='F') #fortran ordering
    
    up = csr_matrix((2*vol, 2*vol))
    low = csr_matrix((2*vol, 2*vol))
    
    p = np.arange(-1,N-1) #need to work on indexing, python starts with 0 as first index
    p[0] = N-1
    
    for i in range(N):

        I = lil_matrix((N,N))
        I[i, i] = 1
        T = I[:,p] # this works, the problem is with p
        
        up = up + kron(diags(v1[i,:], 0), kron(T, p1p))
        up = up + kron(T, kron(diags(v2[:,i],0), p2p))
        
        low = low + kron(diags(v1[i,:],0), kron(T, p1m))
        low = low + kron(T, kron(diags(v2[:,i],0), p2m))
        
    A = (mass + 2)*eye(2*vol) - (csr_matrix.getH(low) + up)
        
    return A

def staggered(mass,N,vol,u):
    
    v1 = np.reshape(u[:,0], (N,N), order='F') #fortran ordering
    v2 = np.reshape(u[:,1], (N,N), order='F') #fortran ordering

    up = csr_matrix((vol, vol))
    
    p = np.arange(-1,N-1) #need to work on indexing, python starts with 0 as first index
    p[0] = N-1

    eta = lil_matrix((N,1))
    eta = diags(np.power(-1*np.ones(N), np.arange(0,N)), 0) #check this
         
    for i in range(N):
        
        I = lil_matrix((N,N))
        I[i, i] = 1
        T = I[:,p] # this works, the problem is with p

        up = up + kron(diags(v1[i,:], 0), T)
        up = up + kron(T, (diags(v2[:,i], 0) * eta))
    

    A = mass*eye(vol) + (up - csr_matrix.getH(up))
    
    return A


                   