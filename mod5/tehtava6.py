import random


pisteet = int(input('anna pisteiden määrä'))
testattu = 0
n = 0
while pisteet > testattu:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x ** 2 + y ** 2 < 1:
        n+=1
   

    testattu+=1
 
pii=4*n/pisteet

print(pii)
