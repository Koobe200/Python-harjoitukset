import sys



def age_check():
    nimi = input('Mikä nimesi on? ')    
    age = int(input('Mikä ikäsi on vuosina? '))

    if age < 12:
        print('olet vain',age,', eli alaikäinen, et voi pelata tätä peliä.' )
        print('Sinun tulee olla vähintään 12v' )
        print('Et voi valitettavasti pelata peliä :(')
        sys.exit()
    else:
        print('Hei!, Nimesi on ', nimi, ' ja ikäsi on ',age,'v' )
        return nimi
        

def kysy_valinta(vaihtoehdot):

    while True:
        try:
            valinta= int(input())
            if 1 <= valinta <= vaihtoehdot:
                return valinta
            else:
                print (f"Valitse numero väliltä 1 ja {vaihtoehdot} ")
        except ValueError:
            print("Anna kelpaava arvo")

def havio(syy):
    print("Jouduit junasta ulos")
    print(f"Syy:{syy}")
    print("Hävisit pelin :(")
    sys.exit()
