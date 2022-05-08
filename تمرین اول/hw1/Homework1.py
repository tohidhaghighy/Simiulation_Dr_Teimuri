from math import sqrt
import numpy as np

def calc_hamming_distancce(a, b):
    a.reshape(b.shape)
    return np.count_nonzero(a != b)

def input_matrix(m, n,msg="Please enter value for M_{},{} : "):
    l_mat=[]
    for i in range(m):
        r = []
        for j in range(n):
            e = int(input(msg.format(i, j)))
            r.append(e)
        l_mat.append(r)
    return np.array(l_mat)

m = int(input("Please input m :"))
n = int(input("Please input n :"))
C = input_matrix(m, n, msg="Please enter value for C_{},{} : ")
print("*"*10)
c = input_matrix(1, n, msg="Please enter value for c_{},{} : ")
print("*"*10)
nni = np.argmin(np.apply_along_axis(lambda x:calc_hamming_distancce(x, c), axis=1, arr=C))
print("Nearest Neighbour Index : {}".format(nni))
