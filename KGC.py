from util import *
from config import u, N


def Setup():
    G = gen_multiple_polynomials(N-1)

    def E(x):
        X = np.array([[x**i for i in range(1, N)]])
        return poly_mod(u + X @ G).flatten()

    return np.array([E(i) for i in range(1, N+1)])
