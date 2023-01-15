import random
import numpy as np
from config import q, f, N

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


def poly_dotprod(s1, s2):
    """
        t = s1[0]*s2[0] + s1[1]*s2[1] ... + s1[m-1]*s2[m-1]
    """
    n_poly = np.array([poly_mul(np.array(poly)[0], np.array(poly)[1])
             for poly in zip(s1, s2)])
    n = [0]
    for j in n_poly:
        n = poly_add(n, j)
    
    return n


def poly_op(a, s1, s2):
    """
        t = a * s1 + s2
    """
    return poly_mod(np.polyadd(np.convolve(s1, a), s2))

####################################

# Lagrange Polynomial

def Lagrange(theta):
    f = 1
    for i in range(1, N+1):
        if i != theta:
            f = f * (-i) / (theta - i)
    
    return f