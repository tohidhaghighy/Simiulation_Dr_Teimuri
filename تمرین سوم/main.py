import random
import math

p = float(input("enter p:"))

# انقدر این عملیات را تکرار میکنیم که از احتمال ورودی رو اعمال میکنیم
# تا زمانی که رو بیاید 
def playonetime(p):
    winner = 'none'
    wina = 0
    winb = 0
    dif = 0
    x =[]
    points = 0
    firsttime =  random.random()
    if (firsttime > p):
        x.append('h')
        f=0
        while f != 1:
            if random.random() > p:
                f = 0
                x.append('h')
            else:
                f = 1
                x.append('t')
                winner = 't'
            points += 1

    elif(firsttime < p):
        x.append('t')
        f = 0
        while f != 1:
            if random.random() < p:
                f = 0
                x.append('t')
            else:
                f = 1
                x.append('h')
                winner = 'h'
            points += 1

    return x,points+1,winner

print(playonetime(p))
