# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 07:59:39 2020

@author: twQCD
"""

class Latparams:
    def __init__(self, xdim, tdim, coupling, mass):
        self.nx = xdim
        self.nt = tdim
        self.beta = coupling
        self.m = mass
    
    def N(self, xdim, tdim):
        return (xdim * tdim)
        
class HMCparams:
    def __init__(self, mc, w, nw, si):
        self.nmc = mc
        self.warmup = w
        self.num_warmup = nw
        self.save_interval = si
        
class MDparams:
    def __init__(self, md, sep):
        self.nmd = md
        self.tau = sep
        
    def traj(self, num_steps, size_step):
        return (num_steps * size_step)


class Gauge:
    def __init__(self, xi, ti, val, nx, nt):
        self.x = xi
        self.t = ti
        self.u = val
        self.nx = nx
        self.nt = nt
        
    def idx(self, xi, ti):
        return (xi + self.nx*ti)
    
class Field:
    def __init__(self, xi, ti, val, nx, nt):
        self.x = xi
        self.t = ti
        self.site = val
        self.nx = nx
        self.nt = nt
        
    def idx(self, xi, ti):
        return (xi + self.nx*ti)