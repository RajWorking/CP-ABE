import random
from algo import RTrapGen
from config import attr, q, f, d, m
from util import *
import numpy as np


class AA:
    '''
    Authority 
    '''

    def __init__(self) -> None:
        self._C = np.array([[random.randrange(0, q)
                             for _ in range(f)] for _ in range(d)])

    def AASetup(self):
        self.A, self._T = RTrapGen()

        self.b_plus = np.array([gen_multiple_polynomials(m)
                               for _ in range(attr)])
        self.b_minus = np.array([gen_multiple_polynomials(m)
                                for _ in range(attr)])

    def P(self, z):
        '''
        z is numpy array of shape (d, m)
        returns P = C * d, of shape (f * m)
        '''
        return (self.C @ z).T
