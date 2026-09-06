def listalasku(lista):
    parillinenlista=[]
    for plus in lista:
        lasku = plus % 2 
        if lasku == 0:
            parillinenlista.append(plus)


    return  parillinenlista

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


print('Koko lista:')

for tulokset in listanumerot:
    print(tulokset)


print('parillinen lista koostuu:')

for tulokset in listatulos:
    print(tulokset)