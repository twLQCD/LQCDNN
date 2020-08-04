# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 14:41:44 2020

@author: Travis_Whyte
"""

import numpy as np
from scipy.sparse.linalg import eigsh

def plaquette(theta):
    
    plaq = np.mean(np.cos(theta))
    
    return plaq

def lowest_eig_symm(M):
    
    evals, evecs = eigsh(M, 10, sigma=0)
    evals = np.sort(evals)
    lam = evals[0]
    return lam
    
    
    