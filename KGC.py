from util import *
from config import u, N


def Setup():
    G = gen_multiple_polynomials(N)

    def E(x):
        X = np.array([[x**i for i in range(0, N)]])
        return poly_add(u, (X @ G).T).flatten()

    return np.array([E(i) for i in range(1, N+1)])
