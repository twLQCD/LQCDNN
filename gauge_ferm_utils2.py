# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 07:59:36 2020

@author: Admin
"""
import numpy as np
import latclasses as lc


def setlinks(p):
    gaugelinks = list()
    for i in range(p.N(p.nx, p.nt)):
        gaugelinks.append(lc.Gauge(i, []))

    return gaugelinks

def setfield(p):
    field = list()
    for i in range(p.N(p.nx, p.nt)):
        field.append(lc.Field(i, []))
        
    return field

def random_field(field):
    for sites in field:
        sites.site = np.random.uniform(0, 1, (2,1)) + np.random.uniform(0, 1, (2,1)) * 1j

def random_gauge(gaugelinks):
    for links in gaugelinks:
        links.u = 2 * np.pi * np.random.uniform(0, 1, (1,1))
        links.u = np.cos(links.u) + np.sin(links.u) * 1j

def unit_links(gaugelinks):
    for links in gaugelinks:
        links.u = 1
        
def unit_field(field):
    for sites in field:
        sites.site = 1
