# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 12:58:32 2020

@author: twLQCD
"""

import latclasses as lc
import gauge_ferm_utils2 as gfu

if __name__ == '__main__':
    
    p = lc.Latparams(256, 256, 6.0, 0.1)
    gaugelinks = gfu.setlinks(p) #initializes the lattice
    gfu.unit_links(gaugelinks, p)   #sets links to 1
    
    field = gfu.setfield(p) #initializes field
    gfu.unit_field(field, p)   #sets field values to 1
    
    sitex = 1 # x lattice coordinate
    sitet = 3 # t lattice coordinate
    s1 = 0 # dirac index 1
    s2 = 1 # dirac index 2
    
    print("Value of gauge link at (", sitex, ",", sitet,") with Dirac index: ",s1)
    print(gaugelinks[sitex][sitet].u[s1])
    
    print("Value of field at (", sitex, ",", sitet,") with Dirac index: ",s2)
    print(field[sitex][sitet].site[s2])
    
    print("Field index at site (", sitex, ",", sitet,") is : ", field[sitex][sitet].idx(sitex, sitet))
    
    
