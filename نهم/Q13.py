import math
import numpy as np
import random

# Python program to get average of a list
def Average(lst):
    return sum(lst) / len(lst)

list_num=[56,101,78,67,93,78,64,72,80,69]
print("mean is : ")
print(Average(list_num))

r = 100;
X = [56,101,78,67,93,87,64,72,80,69]
n = len(X)

def randomvecgenerator(Y):
    r = []
    for i in range(0,len(Y)):
        t = random.randrange(0,len(Y))
        r.append(X[t])
    return r

#Bootstrap
counter=0
for i in range(r):
    idx = randomvecgenerator(X);
    mean_list=Average(idx)
    if((mean_list-78.5)<5):
        if((mean_list-78.5)>-5):
            counter=counter+1

print("--------------------------")
print(counter/r)
