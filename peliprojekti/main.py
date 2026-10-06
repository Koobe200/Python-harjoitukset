import os
from yleisfunktiot import age_check,kysy_valinta, tallenna
from peli import aloita_peli
import sys

kansio = os.path.dirname(__file__)                  
ohjeet_file = os.path.join(kansio, "ohjeet.txt")


nimi=age_check()


while True: 
    print("\nTervetuloa pää-valikkoon, valitse yksi seuraavista vaihtoehdoista valikossa:\n")
    print("(1) Uusi peli\n(2) Jatka tallennuksesta\n(3) Ohjeet \n(4)Lopeta")
    valikko_valinta=kysy_valinta(4)
    if valikko_valinta == 1:
        peli=aloita_peli(nimi)
    elif valikko_valinta == 2: 
        print("Valitse t")
    elif valikko_valinta == 3:
        with open(ohjeet_file, "r") as tiedosto:
                    ohjeet = tiedosto.read()
                    print(ohjeet)
        input()
    else:
          sys.exit()

