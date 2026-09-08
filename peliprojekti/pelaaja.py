nimi = input('Mikä nimesi on? ')    
age = int(input('Mikä ikäsi on vuosina? '))

esinelista=[]
def lisalista():
      
    while True:
        asia=input('Lisää esine listaan, jos haluat lopettaa lisäämisen kirjoita "Lopeta" ')
        asiatod=asia.upper()
        if asiatod == 'LOPETA':
            print('lopetetaan listaan lisääminen')
            break
        esinelista.append(asia)

    
def printlista():
     print('Lista sisältää:')
     for i in esinelista:
          print(i)

def jarjestyslista():
     esinelista.sort(reverse=True)
     print('Lista sisältää väärinpäin katottuna:')
     for i in esinelista:
          print(i)







if age < 12:
    print('olet vain',age,', eli alaikäinen, et voi pelata tätä peliä.' )
    print('Sinun tulee olla vähintään 12v' )
    
else:
    print('Hei!, Nimesi on ', nimi, ' ja ikäsi on ',age,'v' )
    while True:
        valikko = "Valitse yksi komennoista:\n1. Listalisäys\n2. Listan tulostus \n3. Lista väärinpäin ja tulostus \n0 LOPETUS'\n"
        valinta_main= int(input(valikko))

        if valinta_main == 1:
            lisalista()
        elif valinta_main == 2:
                printlista()
        elif valinta_main == 3:
                    jarjestyslista()
        elif valinta_main == 0:
            print('ohjelma lopetetaan')
            break
        else:
            print('Tämä ei tainnut olla vaihtoehto')
