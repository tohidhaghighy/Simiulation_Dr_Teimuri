import random
from scipy.stats import chi2



N = [158,172,164,181,160,165]
n = sum(N)

p = [1/6,1/6,1/6,1/6,1/6,1/6];
k = len(p);
T = 0
for i in range(len(N)):
    T += ((N[i]-n*p[i])**2)/(n*p[i])
def rangenerator(n):
    randN = [0,0,0,0,0,0]
    for i in range(n):
        x = random.random()
        for k in range(6):
            if x < (k+1)/6:
                randN[k]+=1
                break

    return randN

P = 1-chi2.cdf(T,k-1)
print('p-value using chi-square approximation:',P)

# simulation
Rep = 1000
pt = 0
# print(T)
for i in range(0, Rep):
    U=[]
    U=rangenerator(1000)
    Tt = 0
    # print(U)
    for o in range(len(U)):
        Tt += ((U[o] - n * p[o]) ** 2) / (n * p[o])
    # print(Tt)
    if Tt > T:
        pt = pt + 1

pt = pt / Rep
print('p-value using simulationand 1000 Rep:  ',pt)