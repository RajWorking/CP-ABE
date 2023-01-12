from util import *
from config import u, N


def Setup():
    g = gen_multiple_polynomials(N-1)

    def F(x):
        X = np.array([[x**i for i in range(1, N)]])
        return poly_mod(u + X @ g).flatten()

    return np.array([F(i) for i in range(1, N+1)])
