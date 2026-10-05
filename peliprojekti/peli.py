from Asemat import Asema, Kirkkonummi, Espoo, Leppavaara
from pelaaja import Pelaaja
from yleisfunktiot import havio
import os




def aloita_peli(nimi):
    kansio = os.path.dirname(__file__)                  
    intro = os.path.join(kansio, "intro.txt")
    with open(intro, "r") as tiedosto:
        intro = tiedosto.read()
        print(intro)
    pelaaja1 = Pelaaja(nimi)
    kirkkonummi=Kirkkonummi("Kirkkonummi", pelaaja1)
    espoo=Espoo("Espoo", pelaaja1)
    leppavaara=Leppavaara("Leppävaara", pelaaja1)
    #pasila=Pasila("Pasila", pelaaja1)
    #helsinki=Helsinki("Helsinki", pelaaja1)

    
    asemat=[kirkkonummi,espoo,leppavaara]

    for asema in asemat:
        
        asema.pelaa()
        print(f"aikaa on jäljellä {pelaaja1.aika} - minuuttia")
        if pelaaja1.aika <= 0:
                havio("Aika loppui kesken :(")
        pelaaja1.sijainti+=1