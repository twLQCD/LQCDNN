# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 16:44:44 2020

@author: twLQCD
"""
import numpy as np
import math

def norm(psi, chi, p):
    tmp = 0.0
    for i in range(p.nt):
        for j in range(p.nx):
            for k in range(2):
                tmp = tmp + np.real(psi[j][i].site[k])*np.real(chi[j][i].site[k])
                tmp = tmp - np.imag(psi[j][i].site[k])*np.imag(chi[j][i].site[k])
    
    return tmp

def normalize(a, psi, p):
    for i in range(p.nt):
        for j in range(p.nx):
            for k in range(2):
                psi[j][i].site[k] = (1.0/ math.sqrt(a))*psi[j][i].site[k]
    
    return psi
