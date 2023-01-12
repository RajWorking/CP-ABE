# helpers
import numpy as np
from config import *
from util import *


def RTrapGen():
    a = gen_polynomial()
    r = gen_multiple_polynomials(k) # TODO: gaussian distribution
    e = gen_multiple_polynomials(k)
    
    A = np.array([[0]*(f-1) + [1], a])
    b = np.array([(np.array([0]*(f-1) + [h[i]]) - poly_op(a, r[i], e[i])) for i in range(k)])
    
    A = np.concatenate((A, b))
    T = (r, e)
    
    return A, T
