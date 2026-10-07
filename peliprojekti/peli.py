from Asemat import Kirkkonummi, Espoo, Leppavaara, Helsinki
from yleisfunktiot import havio, clear_console
import os
import sys
kansio = os.path.dirname(__file__)    


# Peli aloitetaan tästä
def aloita_peli(pelaaja):
   
    pelaaja = pelaaja 
    # Intron polun määritys     
    intro = os.path.join(kansio, "intro.txt")
    with open(intro, "r", encoding="utf-8") as tiedosto:
        intro = tiedosto.read()
        print(intro.format(pelaaja_nimi=pelaaja.nimi))
    # Määritetään asema oliot
    kirkkonummi=Kirkkonummi("Kirkkonummi", pelaaja)
    espoo=Espoo("Espoo", pelaaja)
    leppavaara=Leppavaara("Leppävaara", pelaaja)
    helsinki=Helsinki("Helsinki", pelaaja)

    # Tehdään lista olioista 
    asemat=[kirkkonummi,espoo,leppavaara,helsinki]


    # Käy asemat läpi yksitellen
    for asema in asemat[pelaaja.sijainti:]:
        
        asema.pelaa()
        print(f"aikaa on jäljellä {pelaaja.aika} - minuuttia")
        if pelaaja.aika <= 0:
                clear_console()
                havio("Aika loppui kesken :(")
        pelaaja.sijainti+=1
    peli_loppu(pelaaja)


# Kertoo tulokset ja lopettaa pelin
def peli_loppu(pelaaja):
    print("Hienoa! pääsit perille ajoissa!!")
    input("Paina ENTER näyttääksesi tuloksesi")
    clear_console()
    tulokset={"Aikaa jäljellä":pelaaja.aika,"Ystävällisyys":pelaaja.ystavallisuus}
    for slotti, arvo in tulokset.items():
             print(f"{slotti}: {arvo}")
    print("Esineet:")
    for i in pelaaja.esinelista:
                    print(i)
    #Laskee pelaajalle pisteet
    pisteet=pelaaja.aika+pelaaja.ystavallisuus*10
    pelaaja_tulokset=(f"nimi:{pelaaja.nimi}\npisteet:{pisteet}\n")
    tulokset = os.path.join(kansio, "tulokset.txt")
    #Lisää tiedostoon tulokset
    with open(tulokset, "a",encoding="utf-8") as tiedosto:
             tiedosto.write(pelaaja_tulokset)
    with open(tulokset, "r",encoding="utf-8") as tiedosto:
         data = tiedosto.read()
    print("\nTulokset\n")
    print(data)
    
    sys.exit()