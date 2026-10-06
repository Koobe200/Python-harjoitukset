import random
import time
from yleisfunktiot import havio
from .asema import Asema


class Espoo(Asema):
    def __init__(self, nimi, pelaaja):
        super().__init__(nimi,pelaaja)
        

    def pelaa(self):
        
        print("Tervetuloa U junaan! Juna suuntaa tällä hetkellä kohti helsinkiä seuraava asema: Espoo")
        time.sleep(2)
        #arvotaan pelaajalle aikamäärä
        if "pyörä" in self.pelaaja.esinelista:
            self.pyora_paikka()
        else: 
            self.mummo()
        time.sleep(3)
        print("Tervetuloa Espoon asemalle!")


    def pyora_paikka(self):
        print('Olet päättänyt varastaa pyörän, joten sinun pitää löytää sille paikka junasta')
        print('Etsitään paikkoja...')
        time.sleep(3)
        print('O ou, tilaa ei tunnu löytyvän, sinulla on 2 vaihtoehtoa: \n (1)Pyydä pyörä paikkaa muilta \n (2) Et halua kysyä, joten sysäset vain pyörän johonkin')
        vaihtoehto=self.kysy(2)

        if vaihtoehto == 1: 
            print("Hienoa! haluat olla sosiallinen")
            print("Pyydät erästä miestä antamaan pyörällesi tilaa, valitse yksi seuraavista vaihtoehdoista:")
            print("(1) Saanko paikan\n (2) Anna mulle paikka vanha ukko\n (3)Voisisinko saada ystävällisesti paikan ")
            vastaus=self.kysy(3)
            if vastaus == 1: 
                ystavallisyys=random.randint(1,4)
                if ystavallisyys == 1: 
                    havio("Ei riittänyt ihan paikan saamiseen")
                else: 
                    print("Hienoa! sait pyöräpaikan!")
                    
            elif vastaus == 2:
                print("Olipa töykeä tapa, et ollut ystävällinen, joten sinut heitetään junasta ulos")
                havio("Ei osannu pyytää pyöräpaikkaa ystävällisesti.")
            else:
                print("Hienoa! sait pyöräpaikan!")
             

        
        else: 
            print("Nyt on erikoinen päätös")
            time.sleep(2)
            print("Tunget pyöräsi pyörien keskelle, samalla kaadat, yhden miejhen pyörän")
            time.sleep(2)
            print("Mies huomaa tämän ja suuttuu sinulle")
            print("Joudut juoksemaan karkuun, mies jahtaa sinua")
            self.pelaaja.esinelista.remove("pyörä")
            print("päästäksesi karkuun sinun tulee avata ovi toiseen vaunuun. \n\nOvella on 5 napia yritä arvata oikean nappi oven avaamiseen")
            numero=random.randint(1,5)
            karkuun=False
            for i in range(0,3):
                print(f"Sinulla on {3-i} yritystä, arvaa numero 1-5 välillä:")
                arvaus=self.kysy(5)
                time.sleep(3)
                if arvaus == numero: 
                    print("Hyvä! Sait oven auki, pääsit karkuun!")

                    karkuun=True
                    break
            if karkuun == False:    
                havio("jäi vihaiselle miehelle kiinni jaa heitettiin ulos")
            
            
    def mummo(self):
        print("Olet saapunut junaan ja sinun tulee löytää istumapaikka")
        print("Paina ENTER istuaksesi")
        input()
        print("Hieoa! Olet istahtanut alas")
        print("Huomaat, että kauklahden pysäkillä junaan astuu vanha mummeli")
        print("Junassa ei ole tilaa istua, joten mummeli joutuu seistä")
        print("Mitä aijot tehdä?")
        print("(1) Istua paikallasi\n (2) Anna oma paikkasi mummelille \n (3) Pyydä jotakuta muuta antamaan paikkansa")
        vaihtoehto=self.kysy(3)

        if vaihtoehto == 1:
            print("Et välittänyt mummon tilanteesta, menetät 2 ystävällisyys pistettä")
            self.pelaaja.ystavallisuus-=2
            print(f"sinun ystävällisyys tällä hetkellä:{self.pelaaja.ystavallisuus} pistettä")
        elif vaihtoehto == 2:
            print("Hienoa annoit mummollesi paikan, saat 2 ystävällisyys pistettä ja mummo haluaa antaa sinulle pullan")
            print("Saat yhden pullan")
            self.pelaaja.esinelista.append("pulla")
            self.pelaaja.ystavallisuus+=2
            print(f"sinun ystävällisyys tällä hetkellä:{self.pelaaja.ystavallisuus} pistettä")
        else:
            arpa=random.randint(1,2)

            if arpa == 1: 
                print("Kukaan ei antanut paikkaa")
                print("Vaikka yritit saada mummolle paikan, et antanut omaa paikkaasi, menetät 1 ystävällisyys pisteen")
                self.pelaaja.ystavallisuus-=1
                print(f"sinun ystävällisyys tällä hetkellä:{self.pelaaja.ystavallisuus} pistettä")
            else:
                print("Sait toisen herran antamaan paikan, Hienoa! Saat yhden ystävällisyys pisteen!")
                self.pelaaja.ystavallisuus+=1
                print(f"sinun ystävällisyys tällä hetkellä:{self.pelaaja.ystavallisuus} pistettä")



