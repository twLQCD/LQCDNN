# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 07:59:36 2020

@author: twLQCD
"""
import numpy as np
import latclasses as lc


def setlinks(p):
    gaugelinks = np.empty([p.nx,p.nt], dtype=object)
    for i in range(p.nt):
        for j in range(p.nx):
            gaugelinks[j][i] = lc.Gauge(j, i, [], p.nx, p.nt)
            
    return gaugelinks

def setfield(p):
    field = np.empty([p.nx,p.nt], dtype=object)
    for i in range(p.nt):
        for j in range(p.nx):
            field[j][i] = lc.Field(j, i, [], p.nx, p.nt)
            
    return field
       
def random_gauge(gaugelinks, p):
    for i in range(p.nt):
        for j in range(p.nx):
            gaugelinks[j][i].u = 2 * np.pi * np.random.uniform(0, 1, (2,1))
            gaugelinks[j][i].u = np.cos(gaugelinks[j][i].u) + np.sin(gaugelinks[j][i].u) * 1j

def random_field(field, p):
    for i in range(p.nt):
        for j in range(p.nx):
           field[j][i].site = np.random.uniform(0, 1, (2,1)) + np.random.uniform(0, 1, (2,1)) * 1j
      
def unit_links(gaugelinks, p):
    for i in range(p.nt):
        for j in range(p.nx):
            gaugelinks[j][i].u = [1.0, 1.0]
            
def unit_field(field, p):
    for i in range(p.nt):
        for j in range(p.nx):
            field[j][i].site = [1.0, 1.0]
            
