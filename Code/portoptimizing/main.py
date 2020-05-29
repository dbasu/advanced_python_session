# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 14:49:49 2015

@author: db
"""
import meanvaropt
import numpy as np
import dotdict

alp = np.array([[1.1, 3.2, 2.1, 3.2]])
cov = np.matrix([[1, 0, 0, 0],[0, 1, 0, 0],[0, 0, 1, 0],[0, 0, 0, 1]])
h0 = np.array([[0, 0.5, 0, 0.5]])
tc      = dotdict
tc.tcaf = 10
tc.k0   = 0.05
tc.k1   = np.array([[0.1, 0.1, 0.1, 0.1]])
mvo   = meanvaropt.meanvaropt()
minmax = [(0, 1), (0,1), (0,1), (0,1)]
constr = ({'type': 'eq',   'fun': lambda h: np.dot(h, np.transpose(np.ones(h.shape))) - 1},
          {'type': 'ineq', 'fun': lambda h: np.dot(h, np.transpose(np.array([1, 0, 0, 0]))) - 0.9})
h1 =  mvo.optimize(alp, cov, 0.5, h0, tc, minmax, constr)
