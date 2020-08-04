# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 14:38:48 2020

@author: Travis_Whyte
"""
import numpy as np
from numpy.linalg import eig
import gauge_io, params, dirac_ops
from matplotlib.pyplot import scatter 


nx, nt, N, vol, beta, mass = params.lattice_params()

file = gauge_io.return_filename_wext(mass, beta, nx, nt, 0)

u, theta = gauge_io.load_gauge_from_file(file)

M = dirac_ops.wilson(mass, N, vol, u).toarray()

evals, evecs = eig(M)

scatter(np.real(evals), np.imag(evals))
