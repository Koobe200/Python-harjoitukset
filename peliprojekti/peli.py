from Asemat import Asema
from pelaaja import Pelaaja
import os




def aloita_peli(nimi):
    kansio = os.path.dirname(__file__)                  
    intro = os.path.join(kansio, "intro.txt")
    with open(intro, "r") as tiedosto:
        intro = tiedosto.read()
        print(intro)

    pelaaja1 = Pelaaja("nimi")
    asemat= Asema("kirkkonummi",pelaaja1)

    asemat.kirkkonummi()
    asemat.espoo()