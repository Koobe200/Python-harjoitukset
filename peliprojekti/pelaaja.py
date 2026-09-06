nimi = input('Mikä nimesi on? ')    
age = int(input('Mikä ikäsi on vuosina? '))



if age < 12:
    print('olet vain',age,', eli alaikäinen, et voi pelata tätä peliä.' )
    print('Sinun tulee olla vähintään 12v' )
    
else:
    print('Hei!, Nimesi on ', nimi, ' ja ikäsi on ',age,'v' )
    while True:
        valikko = "Valitse yksi komennoista:\n1. Vuosiluku\n2. paras metropolia kampus \n3. osta haalarimerkkejä \n0 LOPETUS'\n"
        valinta_main= int(input(valikko))

        if valinta_main == 1:
            print('nyt on 2026')
        elif valinta_main == 2:
                print('Karamalmin kampus')
        elif valinta_main == 3:
                    print('https://hoopee.fi/collections/haalarimerkit')
        elif valinta_main == 0:
            print('ohjelma lopetetaan')
            break
        else:
            print('Tämä ei tainnut olla vaihtoehto')
