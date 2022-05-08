import random
#--------------------------------------- homework 4 -----------------------------------------
print("-------------------------- homework 4 ----------------------------------------")

dices = [2,3,4,5,6,7,8,9,10,11,12]
dices_is_exist=[0,0,0,0,0,0,0,0,0,0,0]

def check_array():
    for dices in dices_is_exist:
        if(dices==0):
            return True
    return False

def find_count_dices():
    counter=0
    while(1==1):
        counter=counter+1
        if(check_array()):
            rand_1=random.randint(1,6)
            rand_2=random.randint(1,6)
            final_rand=rand_1 + rand_2
            for i in range(len(dices)):
                if(final_rand==dices[i]):
                    dices_is_exist[i]=1
        else:
           break
    return counter

count_of_simulation=100
sum_of_simulation=0
for i in range(count_of_simulation):
    dices_is_exist=[0,0,0,0,0,0,0,0,0,0,0]
    count_dice=int(find_count_dices())
    print(count_dice)
    sum_of_simulation=sum_of_simulation+count_dice

print(sum_of_simulation/count_of_simulation)
