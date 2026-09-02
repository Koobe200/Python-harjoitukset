import random
arpakuutio=int(input('mikä on arpakuutioiden määrä? '))
summa=[]
for heittokerrat in range(arpakuutio):
    tulos= random.randint(1, 6)
    heittokerrat += 1 
    summa.append(tulos)
    print('tämän heiton tulos on:',tulos)

print('Arpakuutioiden summa on',sum(summa))