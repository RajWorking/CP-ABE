import random
import numpy as np
from config import q, f

####################################

# Generate random polnomials


def gen_polynomial():
    """
    generate a random polynomial with
    - degree: f
    - range: [0, q-1]

    belongs to R_q
    """
    return np.array([random.randrange(0, q) for _ in range(f)])


def gen_multiple_polynomials(m):
    return np.array([gen_polynomial() for _ in range(m)])

####################################

# Polynomial operations


def poly_mod(exp):
    """
    expression (mod (x^f + 1))
    """
    m = len(exp)
    res = exp % q
    for i in range(0, m-f):
        d = res[i]
        res[i] -= d
        res[i + f] -= d
    res = res[-f:] % q
    return res

def poly_add(s1, s2):
    """
        t = s1 + s2
    """
    return poly_mod(np.polyadd(s1, s2))

def poly_mul(s1, s2):
    """
    t = s1 * s2
    """
    return poly_mod(np.convolve(s1, s2))


def poly_op(a, s1, s2):
    """
    t = a * s1 + s2
    """
    return poly_mod(np.polyadd(np.convolve(s1, a), s2))
