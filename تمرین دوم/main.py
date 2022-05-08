import math 
import pandas 
import numpy 
import random

#گرفتن احتمال از ورودی
propbability=float(input("Vared kardan Ehtemal P : "))
#گرفتن تعداد کل بازی ها از بازی 
TotalPlay=int(input("Total Play n :"))

def playonetime(p):
    #برد اولی
    wina = 0
    #برد دومی
    winb = 0
    #تفاوت اولی از دومی در تعداد برد
    dif = 0
    #تعداد کل بازی ها 
    points = 0
    while abs(dif) < 2:
        dif = wina - winb
        # print(dif)
        if(random.random() > p):
            wina +=1
        else:
            winb +=1
        points += 1
        if dif == 2:
            return 1,points,wina
        elif dif == -2:
            return 0,points,winb

p=propbability
twina=0
twinb=0
temp=0

for i in range(TotalPlay):
    whowin,pointc,c = playonetime(p)
    temp += (p ** 2) * ((2 * (1 - p) * p) ** (int(c / 2) - 1))
    if(whowin == 1):
        twina += 1
    else:
        twinb += 1

print("probability of winning A in all rounds:" ,' ',twina/TotalPlay)
print("probability of winning B in all rounds:" ,' ',twinb/TotalPlay)
print("average of Estimated probability of winning A in each round based on played points:", temp/TotalPlay)

