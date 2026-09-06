def listalasku(lista):
    summa=0
    for plus in lista:
        summa=summa+plus

    return summa




listanumerot=[]

while True:
    print('Haluatko lisätä Kokonaisluvun listaan?')
    lisaehto=input('kyllä: (K), Ei (E):')
    lisaehto=lisaehto.upper()

    if lisaehto == 'E':
        break
    elif lisaehto == 'K':
        luku=int(input('minkä luvun haluat lisätä listaan? '))
        listanumerot.append(luku)
        print('luku lisätty listaan')
    else:
        print('Tämä ei ole vaihtoehto')
listatulos=listalasku(listanumerot)

print('summa on', listatulos)