import os
from yleisfunktiot import kysy_valinta, avaa_tallennus
from peli import aloita_peli
import sys

kansio = os.path.dirname(__file__)                  
ohjeet_file = os.path.join(kansio, "ohjeet.txt")

def paavalikko(pelaaja):
    while True: 
        print("\nTervetuloa päävalikkoon, valitse yksi seuraavista vaihtoehdoista valikossa:\n")
        print("(1) Uusi peli\n(2) Jatka tallennuksesta\n(3) Ohjeet \n(4)Lopeta")
        valikko_valinta=kysy_valinta(4)
        if valikko_valinta == 1:
            aloita_peli(pelaaja)
        elif valikko_valinta == 2: 
            peli_jatkuu=avaa_tallennus(pelaaja)
            if peli_jatkuu == True:
                 aloita_peli(pelaaja)

        elif valikko_valinta == 3:
            with open(ohjeet_file, "r") as tiedosto:
                        ohjeet = tiedosto.read()
                        print(ohjeet)
            input()
        else:
            sys.exit()

