import math 
import numpy
import pandas
import random

#------------ Homework 1 ----------------------
print("---------------------------- homework 1 --------------------------------------")

n_count=int(input(" Get Count Simulation From User : "))

# تابعی که تعداد دو عدد رندوم 
# را محاسبه میکند 
def mass_function(n):
    #تعداد کوچک تر از 0.3
    count_1=0
    # تعداد بین 0.3 و 1
    count_2=0
    for i in range(n):
        #تولید عدد تصادفی 
        rand_n = random.random()
        if(rand_n<0.3333):
            # افزودن تعداد 
            count_1=count_1+1
        else:
            count_2=count_2+1

    return count_1,count_2


num_1_100,num_2_100=mass_function(100)
num_1_1000,num_2_1000=mass_function(1000)
num_1_10000,num_2_10000=mass_function(10000)
print("with n = 100 ,proportaion of 1:",num_1_100/100,"proportion of 2:" ,num_2_100/100 )
print("with n = 1000 ,proportaion of 1:",num_1_1000/1000,"proportion of 2:" ,num_2_1000/1000 )
print("with n = 10000 ,proportaion of 1:",num_1_10000/10000,"proportion of 2:" ,num_2_10000/10000 )
        

