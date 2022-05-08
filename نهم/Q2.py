import random
import math

lmbda = float(input("Enter lambda"))

T = float(input("Enter T(total simulation time):"))

def poisson_gereator(lmbda,T):
    res = []
    t = 0
    i = 0

    while(t<T):
        r = random.uniform(0,1)
        x = (-1/lmbda)*math.log(r,math.exp(1))
        i = i+1
        t = t + x
        res.append(t)
    return res
    
print(poisson_gereator(lmbda,T))

