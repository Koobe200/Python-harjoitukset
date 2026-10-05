import os
from yleisfunktiot import age_check,kysy_valinta
from peli import aloita_peli

kansio = os.path.dirname(__file__)                  
ohjeet = os.path.join(kansio, "ohjeet.txt")


nimi=age_check()


while True: 
    print("\nTervetuloa valikkoon, valitse yksi seuraavista vaihtoehdoista valikossa:\n")
    print("(1) Uusi peli\n(2) Jatka tallennuksesta\n(3) Ohjeet \n(4)Lopeta")
    valikko_valinta=kysy_valinta(4)
    if valikko_valinta == 1:
        peli=aloita_peli(nimi)
    elif valikko_valinta == 2: 
        pass
    elif valikko_valinta == 3:
        with open(ohjeet, "r") as tiedosto:
                    ohjeet = tiedosto.read()
                    print(ohjeet)
        input()
    else:
          pass

