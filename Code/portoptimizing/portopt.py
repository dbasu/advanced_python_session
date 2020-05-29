# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 20:18:13 2018

@author: debs_
"""
from cvxpy import *
#from cvxpy import Variable, Problem, Maximize, norm
import numpy as np
import scipy.optimize as opt

            
        
class PortOpt:
    def __init__(self, alp, cov, risk_aversion, h_init, tc_param):
        self._alpha         = alp.reshape((1,len(alp)))
        self._V             = cov
        self._risk_aversion = risk_aversion
        self._n_asset       = len(self._alpha)        
        self._tc_param      = tc_param
        self._constraints   = None
        self._asset_bounds  = None
        self._debug         = False
        self._message       = "Not Set"
        self._success       = False
        _sz                 = self._V.shape        
        if _sz != (self._n_asset, self._n_asset):
            raise AttributeError('Dimensions of Alpha and Covariance do not match')
        if h_init is not None:
            if len(h_init) != self._n_asset:
                raise AttributeError('initial holdings provided but dimensions do not match')
            else:
                self._h_init = h_init.reshape((1,self._n_asset))
#        if self._tc_param is not None:
#            self._tc_param.setdefault('tcaf', 0)
#            self._tc_param.setdefault('k0', np.zeros((1,self._n_asset)))
#            self._tc_param.setdefault('k1', np.zeros((1,self._n_asset)))

    
    def addConstraint(self, constraint_type='eq', A, b):
        _nx, _ny = A.shape
        _nxb     = len(b)
        if not ((_ny == self._n_asset) and (_nxb == _nx)):
            raise AttributeError('Dimensions of Constraint  do not match')  
        self._constraints.append({'type':constraint_type, 'A':A, 'b':b})
        
    def setBounds(self, bnd_type='min', h_bnd):
        self._asset_bounds[bnd_type]= h_bnd
        
    def setDebugMode(self):
        """Check inputs are OK"""
        self._debug = True
        
class CVXPortOpt(PortOpt):
    def __init__(self, alp, cov, risk_aversion, h_init, tc_param):
        super().__init__(alp, cov, risk_aversion, h_init, tc_param)
        self._h_opt = Variable(1,self._n_asset)
       
    def optimize(self):
        _constr = []
        for c in self._constraints:
            if c['type'] == 'eq':
                _constr.append(c['A']*self._h_opt == c['b'])
            elif c['type'] == 'ineq':
                _constr.append(c['A']*self._h_opt <= c['b'])
        if self._asset_bounds is not None:
            if 'max' in self._asset_bounds.keys():
                _constr.append(self._h_opt <= self._asset_bounds['max'])
            if 'min' in self._asset_bounds.keys():
                _constr.append(self._asset_bounds['min'] <= self._h_opt)            
                
        _ret = self._alpha.T*self._h_opt
        _risk = quad_form(self._h_opt, self._V)
        _tc = None
        if (self._tc_param is not None) and (self._h_init is not None):
            if (self._tc_param['tcaf'] != 0):
                _tc   = self._tc_param['tcaf'] * norm(self._h_opt - self._h_init, 1)
        if (_tc is None) and ('ineq' not in self.__constraints.keys()) and (self._asset_bounds is None):
            return  AnalPortOpt(self._alpha, self._V, self._risk_aversion, None, None, self._constraints['A'], self._constraints['b']).optimize()                
        else:
            _prob = Problem(Maximize(_ret - self._risk_aversion * _risk - _tc), self._constraints)
        try:
            _solution = _prob.solve()
        except Exception as e:
            if self._debug:
                print(e)
            _p = QPPortOpt(alp, cov, risk_aversion, h_init, tc_param)
            for c in self._constraints:
                if c['type'] == 'eq':
                    for row in range(c['A'].shape[0]):
                        _p.addConstraint({'type':'eq', 'A':c['A'][row], 'b':c['b'][row]})
                elif c['type'] == 'ineq':
                    for row in range(c['A'].shape[0]):
                        _p.addConstraint({'type':'ineq', 'A':c['A'][row], 'b':c['b'][row]})
            _p.setBounds()
            return _p.optimize()
            
    
class AnalPortOpt(PortOpt):
    def __init__(self, alp, cov, risk_aversion, h_init, tc_param, Aeq, beq):
        super().__init__(alp, cov, risk_aversion, h_init, tc_param)        
    def optimize(self):
        return np.dot(np.linalg.inv(self._V) , self._alpha)/(2*self._risk_aversion)
class QPPortOpt(PortOpt):
    """Mean Variance Optimization"""

    
    #self.method = 'Nelder-Mead'
    def __init__(self, alp, cov, risk_aversion=1, h_init=None, tc_param=None):
        super().__init__(alp, cov, risk_aversion, h_init, tc_param)
        self._method = 'SLSQP'

    
    def _utility(self, h):
        _mean     = np.dot(self._alpha, np.transpose(h))
        _variance = np.dot(np.dot(h, self._V), np.transpose(h))
        _dh       = abs(h- self._h_init)
        if self._tc_param is not None:
            _tcost    = self._tc_param['tcaf']*np.dot( (self._tc_param['k0'] + self._tc_param['k1'] * np.power(dh, 0.5)), np.transpose(dh))
        else:
            _tcost    = 0
        _util     = _mean - self._risk_aversion * _variance - _tcost
        return -_util[0,0]

    def optimize(self):
        _constr = ({'type': c['type'],   'fun': lambda h: np.dot(h, c['A']) - c['b']} for c in self._constraints)
        _bnds   = zip(self._asset_bounds['min'], self._asset_bounds['max'])

        _out = opt.minimize(self._utility, self._h_init, 
                           method      = self._method,
                           bounds      = _bnds,
                           constraints = _constr,
                           options     = {'ftol': 1e-12, 'disp': self._debug})
        self._message = out.message
        self._success = out.success
        if (self.success):
            _h_opt = out.x
        else:
            _h_opt = h_init
            if self._debug:
                print (self._message)
        return _h_opt
    