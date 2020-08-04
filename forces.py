# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 13:12:59 2020

@author: Travis_Whyte
"""

# to do: staggered fermion force

import dirac_algebra, gauge_ferm_utils
import numpy as np

def wilson_force(N, vol, eta, chi, u):
    
    eta = np.reshape(eta, (2,vol), order='F')
    chi = np.reshape(chi, (2,vol), order='F')
    
    p1p, p1m, p2p, p2m = dirac_algebra.project_ops()
    
    eta_s1 = np.zeros((vol,2)) + np.zeros((vol,2)) * 1j 
    eta_s2 = np.zeros((vol,2)) + np.zeros((vol,2)) * 1j
    chi_s1 = np.zeros((vol,2)) + np.zeros((vol,2)) * 1j
    chi_s2 = np.zeros((vol,2)) + np.zeros((vol,2)) * 1j
    tmp1 = np.zeros((2,vol)) + np.zeros((2,vol)) * 1j
    tmp2 = np.zeros((2,vol)) + np.zeros((2,vol)) * 1j
    tmp3 = np.zeros((2,vol)) + np.zeros((2,vol)) * 1j
    tmp4 = np.zeros((2,vol)) + np.zeros((2,vol)) * 1j
    p1 = np.zeros((2,vol)) + np.zeros((2,vol)) * 1j
    p2 = np.zeros((2,vol)) + np.zeros((2,vol)) * 1j
    ff = np.zeros((vol,2)) + np.zeros((vol,2)) * 1j
    
    for i in range(vol):
        tmp1[:,i] = p1p.dot(eta[:,i])
        tmp2[:,i] = p2p.dot(eta[:,i])
        tmp3[:,i] = p1m.dot(chi[:,i])
        tmp4[:,i] = p2m.dot(chi[:,i])
        
    eta_s1[:,0] = u[:,0]
    eta_s1[:,1] = u[:,0]
    eta_s1 = np.matrix.getH(eta_s1)
    eta_s1 = np.multiply(eta_s1, tmp1)
       
    eta_s2[:,0] = u[:,1]
    eta_s2[:,1] = u[:,1]
    eta_s2 = np.matrix.getH(eta_s2)
    eta_s2 = np.multiply(eta_s2, tmp2)
    
    chi_s1[:,0] = u[:,0]
    chi_s1[:,1] = u[:,0]
    chi_s1 = np.matrix.getH(chi_s1)
    chi_s1 = np.multiply(chi_s1, tmp3)
    
    chi_s2[:,0] = u[:,1]
    chi_s2[:,1] = u[:,1]
    chi_s2 = np.matrix.getH(chi_s2)
    chi_s2 = np.multiply(chi_s2, tmp4)
    
    kp, km = gauge_ferm_utils.nearest_neighbor(N, vol)
    
    for i in range(2):
        p1[i,:] = np.multiply(np.conj(eta[i, kp[:, 0]]), chi_s1[i, :]) + np.multiply(np.conj(chi[i, kp[:, 0]]), eta_s1[i, :])
        p2[i,:] = np.multiply(np.conj(eta[i, kp[:, 1]]), chi_s2[i, :]) + np.multiply(np.conj(chi[i, kp[:, 1]]), eta_s2[i, :])
    
    ff[:,0] =  2 * np.real(np.matrix.getH(1j * p1[0,:] + p1[1,:] * 1j))
    ff[:,1] =  2 * np.real(np.matrix.getH(1j * p2[0,:] + p2[1,:] * 1j))

    return ff

def gauge_force(N, vol, theta):
    
    kp, km = gauge_ferm_utils.nearest_neighbor(N, vol)
    a1 = np.zeros((vol,2))
    a2 = np.zeros((vol,2))
    gf = np.zeros((vol,2)) + np.zeros((vol,2)) * 1j
    
    for mu in range(2):
        if mu == 0:
            nu = 1
        else:
            nu = 0
        a1 = theta[kp[:,mu], nu] - theta[kp[:,nu], mu] - theta[:,nu]
        a2 = theta[km[:,nu], nu] - theta[km[:,nu], mu] - theta[kp[km[:,nu], mu], nu]
        gf[:,mu] = np.sin(theta[:,mu] + a1) + np.sin(theta[:,mu] + a2)
    
    return gf
            
        
        