# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 16:44:44 2020

@author: twLQCD
"""
import numpy as np
import math

def dot(psi, chi, p):
    scalar = 0.0
    for i in range(p.nt):
        for j in range(p.nx):
            for k in range(2):
                scalar += np.conj(psi[j][i].site[k]) * chi[j][i].site[k]
    
    return scalar

def normalize(scalar, psi, p):
    for i in range(p.nt):
        for j in range(p.nx):
            for k in range(2):
                psi[j][i].site[k] /= math.sqrt(scalar)