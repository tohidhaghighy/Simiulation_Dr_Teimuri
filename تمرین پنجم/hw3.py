import random
cards = []
sum = 0
ssum = 0

for i in range(100):
    cards.append(i+1)
numofsim = int(input("Enter number of simulations you want:"))
def play():
    hit = 0
    random.shuffle(cards)
    r = random.randrange(0,100)
    # print(len(cards))
    for i in range(len(cards)):
        if cards[i] == i+1:
            hit += 1
    return hit

for i in range(numofsim):
    t = play()
    sum = sum + t
    ssum = ssum + t**2

e = sum/numofsim;
v = ssum/numofsim - e**2;

print("Estimated value is: " ,e)
print("variance is: ",v)
