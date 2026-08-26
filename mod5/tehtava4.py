import random 

arvottu=random.randint(1,10)

while True:
    arvaus= int(input('arvaa luku 1 ja 10 väliltä '))

    if 1<=arvaus<=10:
        if arvaus < arvottu:
            print('luku on liian pieni')
        elif arvaus > arvottu:
             print('luku on liian iso')
        else:
            print('löysit oikean luvun!')
            break
    elif arvaus<1:
        print('luku on alle 1')
    else:
        print('luku on yli 10 ')