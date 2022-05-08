import random
import math
from scipy.stats import uniform

N = 1000

def Calculate(N):
    s=0.0
    x = []
    for i in range(N):
        r = random.uniform(0,1)
        x.append(-math.log(1-r*(1-math.exp(-0.05)),math.exp(1)))
    for j in x:
        s = s + j

    return s/N

print(Calculate(N))