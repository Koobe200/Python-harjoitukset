
kerta= 1
oikein=False
while True:
    kayttajatunnus=input('anna käyttäjunnus ')
    salasana= input('anna salasana ')

    if kerta == 5:
        break
    elif kayttajatunnus== 'python' and salasana == 'rules':
        oikein=True
        break
    else:
        kerta=kerta+1
        print('Väärä käyttätunnus tai salasana, sinulla on enään',6-kerta,'yritystä')



if oikein==True:
     print('Tervetuloa tyhjään sovellukseen, hehe')
elif oikein==False:
     print('Pääsy evätty')
        
        