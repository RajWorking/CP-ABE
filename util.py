# helpers
import random
import numpy as np
from config import *

def gen_random_polynomial():
    """
    generate a random polynomial with
    - degree: f
    - Range: [0, q-1]
    """
    # return np.random.randint(lb, ub+1, n)
    return np.array([random.randrange(0, q) for _ in range(f)])


def RTrapGen(l ,f, k, sigma):
    pass
