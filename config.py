import math
from util import gen_random_polynomial

# number of authorities
N = 1000

# f is degree of polynomial
v = 9
f = 1 << v

# large prime number
q = 1461501637330902918203684832716283019655932564481

b = 17  # TODO: base of h^T
k = math.floor(math.log(q, b) + 1)

h = [1 << (i-1) for i in range(1, k+1)]

u = gen_random_polynomial()
sigma = 2
sigma_s = 3

print(h)
