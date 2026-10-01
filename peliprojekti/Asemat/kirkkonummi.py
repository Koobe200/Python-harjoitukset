import random
import time



class Kirkkonummi:
    def __init__(self):
        self.nimi="Kirkkonummen asema"
       

#kirkkonummi osion pelikulku
    def peli(self,pelaaja):
        self.pelaaja=pelaaja
        self.pelaaja.esinelista.append("HSL-lippu")
        print("Tervetuloa kirkkonummen asemalle!")
        time.sleep(3)
        #arvotaan pelaajalle aikamäärä
        self.aika=random.randint(5,30)
        print(f"U- Juna lähtee {self.aika} minuutin päästä")
        time.sleep(3)
        if self.aika > 23: 
            print("sinulla ei ole kiirre, voit kävellä rauhassa junalle")
            self.kiirre=False
        else:
            print("Sinulla on kiirre, et voi vain kävellä")
            self.kiirre=True 
        time.sleep(3)
        if self.kiirre==True:
            print("Jos haluat ehtiä junaan sinun tulee valita seuraavista vaihtoehtoista:")
            print('(1) Varasta jonkun pyörä\n(2) Pummi kyyti')
            self.vaihtoehto=int(input())
            self.ehtii=False
            if self.vaihtoehto == 1:
                self.pyora_varas()
            else: 
                self.pummi()


    def pyora_varas(self):
        print('Huhhuh mikä varas')
        time.sleep(3)
        self.pelaaja.esinelista.append("pyörä")
        print('Nappasit pyörän niin isossa kiirressä, että sinulta tippui HSL-Lippu')
        time.sleep(3)
        self.pelaaja.esinelista.remove("HSL-lippu")
        print('Joudut menemään junaan ilman lippua,LOL')
        
    def pummi(self,):
        print('Katsotaanpan onko sulla onnea')
        self.jarjestys="Onnistuukohan ekalla kerralla, paina ENTER jatkaaksesi"
        
        for i in range(3):
            print(self.jarjestys)
            input()
            self.onnistuminen=random.randint(0,3)
            print(self.onnistuminen)
            if self.onnistuminen == 1: 
                print("Hyvä! Sait kyydin ja ehdit junaan")
                self.ehtii=True
                break
            
            if i == 0:
                self.jarjestys="Ajaii Onnistuukohan toisella kerralla, paina ENTER jatkaaksesi"
            elif i == 1:
                self.jarjestys="Kolmas kerta toden sanoo!"
            





