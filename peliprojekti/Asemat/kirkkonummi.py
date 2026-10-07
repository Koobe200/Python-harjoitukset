import random
import time
from yleisfunktiot import havio, clear_console
from .asema import Asema

class Kirkkonummi(Asema):
    def __init__(self, nimi, pelaaja):
        super().__init__(nimi,pelaaja)
#Tason peli  
    def pelaa(self):
        input("Paina ENTER aloittaaksesi ensimmäisen tason")
        clear_console()
        if "HSL-lippu" not in self.pelaaja.esinelista:
            self.pelaaja.esinelista.append("HSL-lippu")
        print("Tervetuloa Kirkkonummen asemalle!")
        time.sleep(3)
        #arvotaan pelaajalle aikamäärä
        aika=random.randint(5,30)
        print(f"U- Juna lähtee {aika} minuutin päästä")
        time.sleep(1)
        if aika > 23: 
            print("sinulla ei ole kiire, voit kävellä rauhassa junalle")
            self.pelaaja.aika-=15
            kiirre=False
        else:
            print("Sinulla on kiire, et voi vain kävellä")
            kiirre=True
        time.sleep(1)
        
        if kiirre==True:
            print("Jos haluat ehtiä junaan sinun tulee valita seuraavista vaihtoehdoista:")
            print('\n(1) Varasta jonkun pyörä\n(2) Pummi kyyti')
            vaihtoehto=self.kysy(2)

            #Pelaaja valitsee vaihtoehdon jotka määrittää myös jatkossa pelin kulkua
            if vaihtoehto == 1:
                clear_console()
                self.pyora_varas()
            else: 
                clear_console()
                self.pummi()


    def pyora_varas(self):
        print('\nHuhhuh mikä varas')
        time.sleep(3)
        self.pelaaja.esinelista.append("pyörä")
        print('Nappasit pyörän niin isossa kiireessä, että sinulta tippui HSL-Lippu')
        self.pelaaja.ystavallisuus-=1
        print(f"Sinun ystävällisyys tällä hetkellä:{self.pelaaja.ystavallisuus} pistettä")
        time.sleep(3)
        self.pelaaja.esinelista.remove("HSL-lippu")
        print('Joudut menemään junaan ilman lippua')
        self.pelaaja.aika-=15

        
    def pummi(self):
        print('Katsotaanpa onko sulla onnea')
        jarjestys="Onnistuukohan ekalla kerralla, paina ENTER jatkaaksesi"
        kyyti=False
        # arpoo pääsekö pelaaja junaan vai ei
        for i in range(3):
            print("Auto tulossa... vruuuuum")
            time.sleep(3)
            print(jarjestys)
            self.pelaaja.aika-=10
            input()
            onnistuminen=random.randint(0,3)
            if onnistuminen == 1: 
                print("Hyvä! Sait kyydin ja ehdit junaan")
                kyyti=True
                break
            
            if i == 0:
                jarjestys="Ajaii Onnistuukohan toisella kerralla, paina ENTER jatkaaksesi"
            elif i == 1:
                jarjestys="Kolmas kerta toden sanoo!"
        if kyyti == False:
            havio("Ei saanu kyytiä junalle")
            
            





