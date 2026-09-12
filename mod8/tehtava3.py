
koodilista={}
while True: 
    print('Valitse yksi seuraavista vaaihtoehtoista:')
    lentoas = int(input(' (1) Uuden lentoaseman syöttäminen \n (2) hae jo syötetyn lentoaseman tiedot \n (3) Lopeta ohjelma \n  '))

    if lentoas == 3:
        print('Ohjelma lopetetaan')
        break
    elif lentoas == 1:
       Lkoodi = input('Anna lentoaseman ICAO-koodi: ')
       Lnimi = input('Anna lentoaseman nimi: ')
       koodilista[Lkoodi]=Lnimi
    elif lentoas == 2:
     
        Lkoodi = input('Anna lentoaseman ICAO-koodi: ')
        if Lkoodi in koodilista:
            print(f'koodilla {Lkoodi} kyseessä on {koodilista[Lkoodi]}')
        else:
            print('Koodia ei löytynyt')


