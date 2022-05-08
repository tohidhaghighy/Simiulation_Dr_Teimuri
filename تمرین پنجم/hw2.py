import math 
import numpy as np
import pandas
import random

#-------------  Homework 2  -------------------
print("-------------------------- homework 2 ----------------------------------------")

# گرفتن لیست احتمالات از ورودی 
def input_dis():
    dis_table = []
    n = int(input("Enter value of n:"))
    for i in range(n):
        x = float(input("probability for spesific value: "))
        dis_table.append(x)
    return dis_table

#درست کردن لیست محدوده بازه ها که از 0 شروع و با جمع هر عدد تا 1 میرود
def find_sum_array(array):
    list_probability=[]
    list_count=[]
    # اولی رو 0 میگیریم
    sum_probability=0.0
    #به لیست بازه اضافه میکنیم 
    list_probability.append(sum_probability)
    # شروع به پیمایش کل اعداد ورودی میکنیم و هر کدام را با جمع مقدار قبلی جمع میکنیم 
    for probability in array:
        sum_probability=float(sum_probability + probability)
        list_probability.append(sum_probability)
        list_count.append(0)
    return list_probability,list_count

def mass_function(list_array,list_count,n):
    print(n)
    count_list=[]
    for i in range(n):
        rand=float(random.random())
        #5print(rand)
        for j in range(1,len(list_array)):
            #print(list_array[j-1])
            if(rand>float(list_array[j-1])):
                #print(list_array[j])
                if(rand<float(list_array[j])):
                    #print("is ok")
                    #print(list_count)
                    list_count[j-1]=list_count[j-1]+1
    return list_count

if __name__ == "__main__":
    input_list=input_dis()
    probability_list,list_count=find_sum_array(input_list)
    print(probability_list)
    print(list_count)
    count_l=mass_function(probability_list,list_count,100)
    print(count_l)
    results=[]
    for k in count_l:
        results.append(k/100)
    print(results)

    
