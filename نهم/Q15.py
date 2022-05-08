import math
import numpy as np
import random

r = 100;
X = [5,4,9,6,21,17,11,20,7,10,21,15,13,16,8]
n = len(X)
def randomvecgenerator(Y):
    r = []
    for i in range(0,len(Y)):
        t = random.randrange(0,len(Y))
        r.append(X[t])
    return r

# Estimator g
theta = np.var(X) * (len(X)/(len(X)-1))

#Bootstrap
MSE = 0;
for i in range(r):
    idx = randomvecgenerator(X);
    Yi = (np.var(idx) * len(idx)/(len(idx)-1) - theta) ** 2;
    MSE = MSE + Yi;


MSE = MSE/r

print('MSE for 100 simulations is:',MSE)