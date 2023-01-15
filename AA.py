import random
from algo import RTrapGen
from config import attr, q, f, V, m
from util import *
import numpy as np


class AA:
    '''
    Authority 
    '''

    def __init__(self) -> None:
        self._C = np.array([[[random.randrange(0, q)
                            for _ in range(V)]
                            for _ in range(f)]
                            for _ in range(m)])

    def AASetup(self):
        self.A, self._T = RTrapGen()

        self.b_plus = np.array([gen_multiple_polynomials(m)
                               for _ in range(attr)])
        self.b_minus = np.array([gen_multiple_polynomials(m)
                                for _ in range(attr)])

    def _P(self, z):
        '''
        z has shape (V, 1)
        C has shape (m, f, V)
        returns P = C @ z, of shape (m * f)
        '''
        return (self._C @ z)

    def S(self):
        '''
        attributes given to the user
        '''
        X = random.getrandbits(attr)
        self.X = np.array([1 & X >> i for i in range(attr)])
        return self.X

    def SecretKey(self, E):
        delta = E
        self._SK = np.zeros((attr + 1, m, f))

        for i in range(attr):
            z = np.array([random.randrange(0, q) for _ in range(V)])
            y = self._P(z)
            self._SK[i] = y

            n = poly_dotprod(self.b_plus[i], y) if self.X[i] == 1 else poly_dotprod(
                self.b_minus[i], y)

            delta = poly_add(E, -1 * n)

        self._SK[attr] = gen_multiple_polynomials(m)

    def Decrypt(self, cipher, F, W):
        g = random.getrandbits(attr)
        g = np.array([1 & g >> i for i in range(attr)])

        L = poly_dotprod(cipher['c_A'], self._SK[attr])

        for i in range(attr):
            L = poly_add(L, g[i]*cipher['c_{0}_2'.format(i)])
            
            if W[i] == 1:
                L1 = poly_dotprod(cipher['c_{0}_1'.format(i)], self._SK[i])
                L = poly_add(L, L1)
            elif self.X[i] == 1:
                L1 = poly_dotprod(cipher['c_plus_{0}_1'.format(i)], self._SK[i])
                L = poly_add(L, L1)
            else:
                L1 = poly_dotprod(cipher['c_minus_{0}_1'.format(i)], self._SK[i])
                L = poly_add(L, L1)
        
        phi = cipher['c_0']
        phi -= Lagrange(1) * L
        phi = [1 if x>=(q//4) else 0 for x in phi]
        
        return phi
