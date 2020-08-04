# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 11:15:39 2020

@author: Travis_Whyte
"""

#import numpy as np

def lattice_params():
    nx = 64
    nt = 64
    N = 64
    vol = nx*nt
    beta = 6.0
    mass = 0.35
    #action = 0 # 0 for wilson action, 1 for staggered
    
    return nx, nt, N, vol, beta, mass
    
def moldyn_params():
    nmd = 5
    tau = 0.1
    
    return nmd, tau
    
def HMC_params():
    nmc = 100
    warmup = 0 # 0 for num_warmup mc iters, 1 for no warmup
    num_warmup = 20
    save_interval = 20
    
    
    return nmc, warmup, num_warmup, save_interval
    
    