import math 
import numpy
import pandas
from statistics import mode

#------------ Homework 1 ----------------------
print("---------------------------- homework 1 --------------------------------------")
m=150
a=3
x0=5
for i in range(10):
    x0=a*x0%m
    print(" {}  -------------- rand_x : {}".format(x0,x0/m))

#-------------  Homework 2  -------------------
print("-------------------------- homework 2 ----------------------------------------")

m=200
a=5
x0=3
for i in range(10):
    x0=(a*x0+7)%m
    print(" {}  -------------- rand_x : {}".format(x0,x0/m))

#----------------------- homework 3  ------------------------
print("-------------------------- homework 3 ----------------------------------------")

import math
import random

def find_n():
    counter=0
    sumation=0
    while(sumation<=1):
        r=random.random()
        sumation+=r
        counter+=1

    return counter

def find_EN(n):
    sumation=0
    for i in range(n):
        sumation+=find_n()
    return sumation/n

print("find 100 counter --------------- E(N)  --->  {}".format(find_EN(100)))

print("find 1000 counter --------------- E(N)  --->  {}".format(find_EN(1000)))

print("find 10000 counter --------------- E(N)  --->  {}".format(find_EN(10000)))


#--------------------------------------- homework 4 -----------------------------------------
print("-------------------------- homework 4 ----------------------------------------")

import math
import random

def find_exp_n():
    counter=0
    sumation=1
    while(sumation>=math.exp(-3)):
        r=random.random()
        sumation*=r
        counter+=1

    return counter

def find_exp_EN(n):
    sumation=0
    for i in range(n):
        sumation+=find_exp_n()
    return sumation/n

def find_p_n_is(n,t):
    counter=0
    for i in range(t):
        if(find_exp_n()==n):
            counter+=1
    return counter/t


print("find 1000 counter --------------- E(N)  --->  {}".format(find_exp_EN(1000)))

for i in range(1,8):
    print(" i is {} -- find p of is in n ---- {}".format(i,find_p_n_is(i,1000)))




