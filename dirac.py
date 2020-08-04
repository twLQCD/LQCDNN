# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 13:18:06 2020

@author: Travis_Whyte
"""


from scipy.sparse import csr_matrix, eye

def sigma_1():
    
    sigma_1 = csr_matrix([[0,1],[1,0]])
    
    return sigma_1

def sigma_2():
    
    sigma_2 = csr_matrix([[0,-1j],[1j,0]])
    
    return sigma_2

def sigma_3():
    
    sigma_3 = csr_matrix([[1,0],[0,-1]])
    
    return sigma_3

def project_ops():
    
    s1 = sigma_1()
    p1_plus = (1/2)*(eye(2) + s1)
    p1_minus = (1/2)*(eye(2) - s1)
    
    s2 = sigma_2()
    p2_plus = (1/2)*(eye(2) + s2)
    p2_minus = (1/2)*(eye(2) - s2)
    
    return p1_plus, p1_minus, p2_plus, p2_minus

