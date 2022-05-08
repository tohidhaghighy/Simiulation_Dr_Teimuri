from math import sqrt
import numpy as np

def find_factors(N):
    factors = {1,N}
    for i in range(2,int(sqrt(N))+1):
        if N%i == 0:
            factors.update((i,N//i))
    return factors

N = int(input("Please enter value for N : "))
print("Factors of {} = {}".format(N, find_factors(N)))