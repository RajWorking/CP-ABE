import numpy as np
import random
from config import attr, q, f, u, m
from util import *


class User:
    '''
    User class
    '''

    def W(self, X):
        '''
        define access structure using attributes
        '''
        mask = random.getrandbits(attr)
        self.W_plus = np.array([X[i] & mask >> i for i in range(attr)])
        self.W_minus = np.array([X[i] & (1 ^ self.W_plus[i])
                                for i in range(attr)])

    def Encrypt(self, phi, A, b_plus, b_minus):
        '''
        encrypting data
        '''
        F = np.array([[[random.randrange(0, q)
                        for _ in range(f)]
                       for _ in range(m)]
                      for _ in range(attr)])

        Sigma = np.array([[random.randrange(0, q)
                           for _ in range(f)]
                          for _ in range(m)])

        d = Sigma[0]

        e = random.getrandbits(f)
        e = np.array([1 & e >> i for i in range(f)])

        ud = poly_mul(u, d)
        c0 = poly_add(poly_add(2 * ud, e), q//2 * phi)

        e_A = gen_multiple_polynomials(m)
        c_A = np.array([poly_add(poly_mul(A[i], d), e_A[i]) for i in range(m)])

        out = {'c0': c0, 'c_A': c_A}

        for i in range(attr):
            c_2 = poly_dotprod(F[i][1:], Sigma[1:])
            c_2 = poly_add(c_2, poly_mul(F[i][0], ud))
            c_2 = poly_add(c_2, gen_polynomial())
            out['c_{0}_2'.format(i)] = c_2

            e_1 = gen_multiple_polynomials(m)

            if self.W_plus[i] == 1:
                c_1 = np.array([poly_add(poly_mul(b_plus[i][j], d), e_1[j])
                               for j in range(m)])
                out['c_{0}_1'.format(i)] = c_1

            elif self.W_minus[i] == 1:
                c_1 = np.array([poly_add(poly_mul(b_minus[i][j], d), e_1[j])
                               for j in range(m)])
                out['c_{0}_1'.format(i)] = c_1

            else:
                c_1_plus = np.array([poly_add(poly_mul(b_plus[i][j], d), e_1[j])
                                     for j in range(m)])
                c_1_minus = np.array([poly_add(poly_mul(b_minus[i][j], d), e_1[j])
                                      for j in range(m)])

                out['c_plus_{0}_1'.format(i)] = c_1_plus
                out['c_minus_{0}_1'.format(i)] = c_1_minus

        return out
