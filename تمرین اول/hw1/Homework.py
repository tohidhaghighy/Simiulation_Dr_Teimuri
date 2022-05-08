from math import sqrt
import numpy as np


from itertools import chain, combinations, permutations

def get_subsets(l):
    return chain(*[combinations(l,i + 1) for i,a in enumerate(l)])

def get_k_subsets(l, k):
    s_l = sorted(l)
    return set([tuple(i) for i in combinations(get_subsets(l),k)
               if sorted(chain(*i)) == s_l])

# x_1 + x_2 + ... + x_n = k
def calc_x(k, n):
    l_k = [1] * k
    k_subsets = get_k_subsets(l_k, n)
    answers = []
    for el in k_subsets:
        for per in set(permutations(el)):
            ans = list(map(sum, per))
            answers.append(ans)
    return np.array(answers)

k = int(input("Enter value for k :"))
n = int(input("Enter value for n :"))
print("answers = {}".format(calc_x(k, n)))