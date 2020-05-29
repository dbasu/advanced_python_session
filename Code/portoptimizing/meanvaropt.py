# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 21:18:01 2015

@author: db
"""

import numpy as np
import scipy.optimize as opt

class QPPortOpt:
    """Mean Variance Optimization"""
    debug = True
    message = "Not Set"
    success = False
    method = 'SLSQP'
    #self.method = 'Nelder-Mead'
    def __init__(self):
        self.debug = False
    def setDebugMode(self):
        """Check inputs are OK"""
        self.debug = True
    def utility(self, h, alp, cov, l, tcaf, h0, k1, k0):
        mean     = np.dot(alp, np.transpose(h))
        variance = np.dot(np.dot(h, cov), np.transpose(h))
        dh   = abs(h- h0)
        tcost    = tcaf*np.dot( (k0 + k1 * np.power(dh, 0.5)), np.transpose(dh))
        util = mean -l * variance - tcost
        return -util[0,0]
    def plot(self):
        ''''''
    def optimize(self, alp, cov, risk_aversion, h_init, tc, bnds, constr):
        out = opt.minimize(self.utility, h_init, 
                           args=(alp, cov, risk_aversion, tc.tcaf, h_init, tc.k1, tc.k0), 
                           method=self.method,
                           bounds = bnds,
                           constraints = constr,
                           options={'ftol': 1e-12, 'disp': self.debug})
        self.message = out.message
        self.success = out.success
        if (self.success):
            h1 = out.x
        else:
            h1 = h_init
            if self.debug:
                print self.message
        return h1

