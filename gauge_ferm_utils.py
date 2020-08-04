# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 11:29:46 2020

@author: Travis_Whyte
"""

import numpy as np

def random_gauge(vol):
    
    theta = 2 * np.pi * np.random.uniform(0, 1, (vol,2))
    u = np.cos(theta) + np.sin(theta) * 1j
  
    return u, theta

def unit_gauge(vol):
    
    theta = 2 * np.pi * np.ones((vol,2))
    u = np.cos(theta) + np.sin(theta) * 1j
    
    return u, theta

def create_gauge(theta):
    
    u = np.cos(theta) + np.sin(theta) * 1j
    
    return u

def random_pseudoferm_wilson(vol):
    
    psi = np.random.uniform(0, 1, (2*vol,1)) + np.random.uniform(0, 1, (2*vol,1)) * 1j
    
    return psi

def unit_pseudoferm_wilson(vol):
    
    psi = np.ones((2*vol,1))
    
    return psi


def random_pseudoferm_stagg(vol):
    
    psi = np.random.uniform(0, 1, (vol,1)) + np.random.uniform(0, 1, (vol,1)) * 1j
    
    return psi

def unit_pseudoferm_stagg(vol):
    
    psi = np.ones((vol,1))
    
    return psi

def generate_momenta(vol):
    
    mom = np.random.normal(0, 1, (vol,2))
    
    return mom

def generate_test_momenta(vol):
    
    mom = np.ones((vol,2))
    
    return mom

def nearest_neighbor(N,vol):
    
    kp = np.zeros((vol,2)).astype(np.int8)
    km = np.zeros((vol,2)).astype(np.int8)
    
    for i in range(N):
        for j in range(N):
            
            k = i + j*N
            kp[k,0] = np.remainder(i+1, N) + j*N
            kp[k,1] = i + np.remainder(j+1,N)*N
            km[k,0] = np.remainder(i-1+N,N) + j*N
            km[k,1] = i + np.remainder(j-1+N,N)*N
            
    return kp, km


