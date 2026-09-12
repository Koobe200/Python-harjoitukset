nimilista=set()
while True:
    nimi=input('Kerro nimi ')

    if nimi == '':
        print('Et antanut nimeä, ohjelma loppuu')
        break
    
    if nimi in nimilista: 
        print('Aiemmin syötetty nimi')
    else:
        print('Uusi nimi')
        
    nimilista.add(nimi)

for i in nimilista:
    print(i)
