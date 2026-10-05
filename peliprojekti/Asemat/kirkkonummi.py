import random
import time
from yleisfunktiot import kysy_valinta


def kirkkonummi_taso(pelaaja_import):
    pelaaja=pelaaja_import
    pelaaja.esinelista.append("HSL-lippu")
    print("Tervetuloa kirkkonummen asemalle!")
    time.sleep(3)
    #arvotaan pelaajalle aikamäärä
    aika=random.randint(5,30)
    print(f"U- Juna lähtee {aika} minuutin päästä")
    time.sleep(3)
    if aika > 23: 
        print("sinulla ei ole kiirre, voit kävellä rauhassa junalle")
        kiirre=False
    else:
        print("Sinulla on kiirre, et voi vain kävellä")
        kiirre=True 
    time.sleep(3)
    if kiirre==True:
        print("Jos haluat ehtiä junaan sinun tulee valita seuraavista vaihtoehtoista:")
        print('(1) Varasta jonkun pyörä\n(2) Pummi kyyti')
        vaihtoehto=kysy_valinta(2)
        ehtii=False
        if vaihtoehto == 1:
            pyora_varas(pelaaja)
        else: 
            pummi(pelaaja)


def pyora_varas(pelaaja_import):
    pelaaja=pelaaja_import
    print('Huhhuh mikä varas')
    time.sleep(3)
    pelaaja.esinelista.append("pyörä")
    print('Nappasit pyörän niin isossa kiirressä, että sinulta tippui HSL-Lippu')
    time.sleep(3)
    pelaaja.esinelista.remove("HSL-lippu")
    print('Joudut menemään junaan ilman lippua,LOL')
    pelaaja.aika = pelaaja.aika - 10
    
def pummi(pelaaja_import):
    pelaaja=pelaaja_import
    print('Katsotaanpan onko sulla onnea')
    jarjestys="Onnistuukohan ekalla kerralla, paina ENTER jatkaaksesi"
    
    for i in range(3):
        print("Auto tulosaa... vruuuuum")
        time.sleep(3)
        print(jarjestys)
        input()
        onnistuminen=random.randint(0,3)
        if onnistuminen == 1: 
            print("Hyvä! Sait kyydin ja ehdit junaan")
            ehtii=True
            pelaaja.aika= pelaaja.aika - 5
            break
        
        if i == 0:
            jarjestys="Ajaii Onnistuukohan toisella kerralla, paina ENTER jatkaaksesi"
        elif i == 1:
            jarjestys="Kolmas kerta toden sanoo!"

        print("ei ottanut kyytiin")
        





