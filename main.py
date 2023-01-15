# all channel operations are simulated here

from KGC import *
from AA import *
from User import *
import time


def timeit(code, title):
    st = time.time()
    res = code()
    end = time.time()
    t = round(end - st, 2)
    print(title, '-', t, '(s)')
    return res


aa = AA()
user = User()

E = timeit(lambda: Setup(), 'Setup')
timeit(lambda: aa.AASetup(), 'AASetup')
X = aa.S()

SK = timeit(lambda: aa.SecretKey(E[0]), 'KeyGen')

user.W(X)
msg = random.getrandbits(f)
phi = np.array([1 & msg >> i for i in range(f)])

cipher = timeit(lambda: user.Encrypt(phi, aa.A, aa.b_plus, aa.b_minus), 'Encryption')
