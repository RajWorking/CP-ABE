import math
import numpy as np
import random

# number of authorities
N = 3

# f is degree of polynomial
v = 9
f = 1 << v

# large prime number
q = 1461501637330902918203684832716283019655932564481

b = 17
k = math.floor(math.log(q, b) + 1)
m = k + 2

h = [b << (i-1) for i in range(1, k+1)]

# Gaussian Params
# sigma = 2
# sigma_s = 3

u = np.array([random.randrange(0, q) for _ in range(f)])

# total number of attributes
# [10, 15, 20, 25]
attr = 10

V = 10
