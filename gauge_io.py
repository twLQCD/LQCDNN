# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 14:08:59 2020

@author: Travis_Whyte
"""

import numpy as np

def return_filename_woext(mass, beta, nx, nt, filenum):
    

    filename = str(nx) + str(nt) + "b" + str(beta) + "m" + str(mass) + "_" + str(filenum)
    
    return filename

def return_filename_wext(mass, beta, nx, nt, filenum):
    

    filename = str(nx) + str(nt) + "b" + str(beta) + "m" + str(mass) + "_" + str(filenum) + ".npy"
    
    return filename

def write_gauge_to_file(theta, count, mass, beta, nx, nt):
    
    file = return_filename_woext(mass, beta, nx, nt, count)
    
    np.save(file, theta, allow_pickle=False)
    
def load_gauge_from_file(file):
    
    theta = np.load(file, allow_pickle=False)
    u = np.cos(theta) + np.sin(theta) * 1j
    
    return u, theta