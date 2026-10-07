from Asemat import Kirkkonummi, Espoo, Leppavaara, Helsinki
from yleisfunktiot import havio
import os




def aloita_peli(pelaaja):
    kansio = os.path.dirname(__file__)                  
    intro = os.path.join(kansio, "intro.txt")
    with open(intro, "r") as tiedosto:
        intro = tiedosto.read()
        print(intro)
    pelaaja = pelaaja
    kirkkonummi=Kirkkonummi("Kirkkonummi", pelaaja)
    espoo=Espoo("Espoo", pelaaja)
    leppavaara=Leppavaara("Leppävaara", pelaaja)
    helsinki=Helsinki("Helsinki", pelaaja)

    
    asemat=[kirkkonummi,espoo,leppavaara,helsinki]

    for asema in asemat[pelaaja.sijainti:]:
        
        asema.pelaa()
        print(f"aikaa on jäljellä {pelaaja.aika} - minuuttia")
        if pelaaja.aika <= 0:
                havio("Aika loppui kesken :(")
        pelaaja.sijainti+=1
    peli_loppu(pelaaja)

def peli_loppu(pelaaja):
    print("Hienoa! pääsit perille ajoissa!!")
    tulokset={"Aikaa jäljellä":pelaaja.aika,"Ystävällisyys":pelaaja.ystavallisuus,"Esineet":pelaaja.esinelista}
    for slotti, arvo in tulokset.items():
         print(f"{slotti}: {arvo}")