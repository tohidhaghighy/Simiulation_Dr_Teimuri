import random
import math

def f_cg(x):
    return (1/3)*(1+x)*math.exp(-x/3)

def specfic_rand_generator():
    while(1):
        U1 = random.uniform(0,1);
        U2 = random.uniform(0,1);

        if U2 < f_cg(U1):
            return U1;
            break;

print(specfic_rand_generator())