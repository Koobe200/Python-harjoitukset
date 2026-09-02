import random

def nopanheitto(tahko_amount):
    tulos=random.randint(1,tahko_amount)
    return tulos

tahkoja=int(input('mikä on tahkojen määrä? '))
while True:
    Heitto=nopanheitto(tahkoja)
  
    if Heitto == tahkoja:
        print('jee saatiin suurin mahdollinen tulos, eli:',Heitto)
        break
    print('heitetty numero:',Heitto)



    