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
        returns P = C @ z, of shape (f * m)
        '''
        return (self._C @ z).T

    def S(self):
        '''
        attributes given to the user
        '''
        X = random.getrandbits(attr)
        self.X = np.array([1 & X >> i for i in range(attr)])
        return self.X

    def SecretKey(self, E):
        delta = E
        SK = np.zeros((attr + 1, f, m))

        for i in range(attr):
            z = np.array([random.randrange(0, q) for _ in range(V)])
            y = self._P(z)
            SK[i] = y

            n = poly_dotprod(self.b_plus[i], y.T) if self.X[i] == 1 else poly_dotprod(self.b_minus[i], y.T)

            delta = poly_add(E, -1 * n)

        SK[attr] = gen_multiple_polynomials(m).T

        return SK
