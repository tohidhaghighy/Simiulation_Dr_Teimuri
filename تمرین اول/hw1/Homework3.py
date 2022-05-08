from math import sqrt
import numpy as np

def is_prime(a):
    if((a<=1) or (a%1>0)):
        return False
    for i in range(2, a//2):
        if(a%i==0):
            return False
    return True

N = int(input("Please enter value for N : "))
prime_set = set()
i = 0
while(N>0):
    if(is_prime(i)):
        prime_set.add(i)
        N -= 1
    i += 1
print("{} first prime numbers = {}".format(len(prime_set), prime_set))

def get(a=2, b=3):
    '''
    :param a:
    :param b:
    :return:
    '''