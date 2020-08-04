# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 11:52:46 2020

@author: Travis_Whyte
"""

import params, gauge_ferm_utils, dirac_ops, forces, meas, gauge_io
import numpy as np
import time
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import spsolve
from matplotlib.pyplot import plot


if __name__ == '__main__':
    
    nx, nt, N, vol, beta, mass = params.lattice_params()
    nmd, tau = params.moldyn_params()
    nmc, warmup, num_warmup, save_interval = params.HMC_params()
    kp, km = gauge_ferm_utils.nearest_neighbor(N, vol)
    u0, theta0 = gauge_ferm_utils.random_gauge(vol) #hot start
    #u0, theta0 = gauge_ferm_utils.unit_gauge(vol) #cold start
    accepted = 0
    acc = 0
    Plaq = []
    evals = []
    save_count = 0
    
    for mc in range(nmc):
        
        t = time.time()
        
        u0 = gauge_ferm_utils.create_gauge(theta0)

        #M = dirac_ops.wilson(mass, N, vol, u)
        
        eta0 = gauge_ferm_utils.random_pseudoferm_wilson(vol)
        #eta0 = gauge_ferm_utils.unit_pseudoferm_wilson(vol)
        
        mom = gauge_ferm_utils.generate_momenta(vol)
        #mom = gauge_ferm_utils.generate_test_momenta(vol)
        
        #phi = M.dot(eta)
        phi = dirac_ops.wilson(mass, N, vol, u0).dot(eta0)
        theta = theta0[:, 0] + theta0[kp[:,0], 1] - theta0[:, 1] - theta0[kp[:,1], 0]
        
        h1 = (1/2) * np.power(np.linalg.norm(mom), 2) - beta * np.sum(np.cos(theta)) + np.power(np.linalg.norm(eta0), 2)
        
        #replace below in future with other solvers
        #here is where we will use MG and train the DNN on the coarse grid solve
        
        chi = spsolve(csr_matrix.getH(dirac_ops.wilson(mass, N, vol, u0)), eta0)
        

        theta1 = theta0
        
        #here is where the forces need to be computed, both gauge (gf) and fermion (ff)
        
        ff = forces.wilson_force(N, vol, eta0, chi, u0)
        

        gf = forces.gauge_force(N, vol, theta1)

        pdot = -1*beta*gf + ff
        #print(pdot)
        mom = mom + pdot*tau*(1/2)

        #moldyn loop here
        for md in range(nmd-1):

            theta1 = theta1 + mom * tau

            u = gauge_ferm_utils.create_gauge(theta1)

            #will train on this eta solve as well
            
            eta = spsolve(dirac_ops.wilson(mass, N, vol, u), phi)
            
            chi = spsolve(csr_matrix.getH(dirac_ops.wilson(mass, N, vol, u)), eta)
            

            ff = forces.wilson_force(N, vol, eta, chi, u) 
            
            gf = forces.gauge_force(N, vol, theta1)

            
            pdot = -1*beta*gf + ff

            mom = mom + pdot * tau
        

        theta1 = theta1 + mom * tau
        u = gauge_ferm_utils.create_gauge(theta1)
        eta = spsolve(dirac_ops.wilson(mass, N, vol, u), phi)
        chi = spsolve(csr_matrix.getH(dirac_ops.wilson(mass, N, vol, u)), eta)
        
        ff = forces.wilson_force(N, vol, eta, chi, u)
        gf = forces.gauge_force(N, vol, theta1)
        
        pdot = -1*beta*gf + ff
        mom = mom + pdot * tau * (1/2)
        
        theta = theta1[:, 0] + theta1[kp[:,0], 1] - theta1[:, 1] - theta1[kp[:,1], 0]
        
        h2 = (1/2) * np.power(np.linalg.norm(mom), 2) - beta * np.sum(np.cos(theta)) + np.power(np.linalg.norm(spsolve(dirac_ops.wilson(mass, N, vol, u), eta0)), 2)


        #metropolis test here
        tmp = [1.0, np.exp(-(h2-h1))]
        print(h2-h1)

        plaq = meas.plaquette(theta)
        Plaq = np.append(Plaq, plaq)
        R = np.minimum(1, np.exp(-(h2-h1)))
        test = np.random.random(1)
        print("Monte Carlo iteration is ")
        print(mc)
        if mc < num_warmup:
            theta0 = theta1
            #plaq = meas.plaquette(theta)
            #Plaq = np.append(Plaq, plaq)
        elif mc > num_warmup:
            acc = 0
            if test < R:
                acc = 1
            if acc == 1:
                accepted += 1
                print("Configuration accepted")
                print("Number of accepted configurations")
                print(accepted)
                theta0 = theta1
                theta = theta0[:, 0] + theta0[kp[:,0], 1] - theta0[:, 1] - theta0[kp[:,1], 0]
                #plaq = meas.plaquette(theta)
                #Plaq = np.append(Plaq, plaq)
                
                if np.remainder(accepted, save_interval) == 0:
                    gauge_io.write_gauge_to_file(theta0, save_count, mass, beta, nx, nt)
                    save_count += 1
    
        print(time.time() - t, "secs for MC iter")
    tmp = np.arange(1,len(Plaq)+1)
    plot(tmp,Plaq)
    #tmp = np.arange(1,len(evals)+1)
    #plot(tmp,evals)
            
            
            
            