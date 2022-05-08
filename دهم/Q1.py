import random
from scipy.stats import chi

# در این تابع ما شروع به ساخت اعداد رندوم میکنیم 
# و بعد این اعداد را با شمارنده های هر قسمت شمارش میکنیم
def CounterGenerator(random_count):
    # در روی این سوال 3 مقدار داده شده است
    randN = [0,0,0]
    # به تعداد عدد ورودی عدد رندوم تولید میکنیم
    for item in range(random_count):
        # ساخت عدد رندوم
        x = random.random()
        # شروط رو بر اساس اعدادی که روی سوال داده اعمال میکنیم
        if x < 0.25:
            randN[0]+=1
        elif x < 0.75:
            randN[1]+=1
        else:
            randN[2]+=1

    return randN

def simulation(pt,Rep,probability):
    for i in range(0, Rep):
        U=[]
        U=CounterGenerator(564)
        Tt = 0
        # print(U)
        for o in range(len(U)):
            Tt += ((U[o] - 564 * probability[o]) ** 2) / (564 * probability[o])
        # print(Tt)
        if Tt > T:
           pt = pt + 1

    pt = pt / Rep
    print('p-value using simulationand 1000 Rep:  ',pt)

N_Array = [141,291,132]
probability = [0.25,0.5,0.25]
Sum_n=564

T = 0
for i in range(len(N_Array)):
    T += ((N_Array[i]-Sum_n*probability[i])**2)/(Sum_n*probability[i])


P_Value = 1-chi.cdf(T,2)
print("p-value :",P_Value)

# simulation function
simulation(0,1000,probability)
# print(T)
