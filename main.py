# all channel operations are simulated here

from KGC import *
from AA import *

E = Setup()

aa = AA()
aa.AASetup()
aa.S()

SK = aa.SecretKey(E[0])
print(SK.shape)

