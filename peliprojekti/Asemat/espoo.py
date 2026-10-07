import random
import time
from yleisfunktiot import havio, clear_console
from .asema import Asema


class Espoo(Asema):
    def __init__(self, nimi, pelaaja):
        super().__init__(nimi,pelaaja)
        
#Tason peli
    def pelaa(self):
        input("Pääsit junaan, paina ENTER jatkaaksesi")
        clear_console()

        print("Tervetuloa U junaan! Juna suuntaa tällä hetkellä kohti Helsinkiä seuraava asema: Espoo")
        time.sleep(1)
        #Tarkistaa onko pelaajalle pyörää, jos on joutuu eri polulle, kuin jos ei olisi
        if "pyörä" in self.pelaaja.esinelista:
            self.pyora_paikka()
        else: 
            self.mummo()
        time.sleep(1)
        print("Tervetuloa Espoon asemalle!")

#Pelaajan pitää löytää pyöräpaikka
    def pyora_paikka(self):
        print('Olet päättänyt varastaa pyörän, joten sinun pitää löytää sille paikka junasta')
        print('Etsitään paikkoja...')
        time.sleep(3)
        print('O ou, tilaa ei tunnu löytyvän, sinulla on 2 vaihtoehtoa:')
        print('\n(1)Pyydä pyöräpaikkaa muilta \n(2) Et halua kysyä, joten sysäset vain pyörän johonkin')
        vaihtoehto=self.kysy(2)
        clear_console()
        if vaihtoehto == 1: 
            print("Hienoa! haluat olla sosiaalinen")
            print("Pyydät erästä miestä antamaan pyörällesi tilaa, valitse yksi seuraavista vaihtoehdoista:")
            print("\n(1) Saanko paikan\n(2) Anna mulle paikka vanha ukko\n(3) Voisinko saada ystävällisesti paikan")
            vastaus=self.kysy(3)
            if vastaus == 1: 
                ystavallisyys=random.randint(0,3)
                if ystavallisyys == 1: 
                    havio("Ei riittänyt ihan paikan saamiseen")
                else: 
                    print("Hienoa! sait pyöräpaikan!")
                    self.pelaaja.ystavallisuus+=1
                    print(f"Sinun ystävällisyys tällä hetkellä:{self.pelaaja.ystavallisuus} pistettä")
                    self.pelaaja.aika-=20
            elif vastaus == 2:
                print("Olipa töykeä tapa, et ollut ystävällinen, joten sinut heitetään junasta ulos")
                havio("Ei osannu pyytää pyöräpaikkaa ystävällisesti.")
            else:
                print("Hienoa! sait pyöräpaikan!")
                self.pelaaja.aika-=10
                self.pelaaja.ystavallisuus+=2
                print(f"Sinun ystävällisyys tällä hetkellä:{self.pelaaja.ystavallisuus} pistettä")
             

        
        else: 
            print("Nyt on erikoinen päätös")
            time.sleep(1)
            print("Tunget pyöräsi pyörien keskelle, samalla kaadat yhden miehen pyörän")
            time.sleep(1)
            print("Mies huomaa tämän ja suuttuu sinulle")
            self.pelaaja.ystavallisuus-=2
            print(f"Sinun ystävällisyys tällä hetkellä:{self.pelaaja.ystavallisuus} pistettä")
            time.sleep(1)
            print("Joudut juoksemaan karkuun, mies jahtaa sinua")
            self.pelaaja.esinelista.remove("pyörä")
            # Arpoo numeron, josta pitää löytää oikea
            print("päästäksesi karkuun sinun tulee avata ovi toiseen vaunuun. \nOvella on 5 napia yritä arvata oikean nappi oven avaamiseen")
            numero=random.randint(1,5)
            karkuun=False
            for i in range(0,3):
                print(f"Sinulla on {3-i} yritystä, arvaa numero 1-5 välillä:")
                arvaus=self.kysy(5)
                clear_console()
                if arvaus == numero: 
                    print("Hyvä! Sait oven auki, pääsit karkuun!")
                    karkuun=True
                    break
            if karkuun == False:    
                havio("jäi vihaiselle miehelle kiinni jaa heitettiin ulos")
            
#Pelaajan pitää päättää antaako mummolle paikan 
    def mummo(self):
        print("Olet saapunut junaan ja sinun tulee löytää istumapaikka")
        time.sleep(1)
        print("Paina ENTER istuaksesi")
        input()
        clear_console()
        print("Olet istahtanut alas")
        time.sleep(1)
        print("Huomaat, että kauklahden pysäkillä junaan astuu vanha mummeli")
        time.sleep(1)
        print("Junassa ei ole tilaa istua, joten mummeli joutuu seistä")
        time.sleep(1)
        print("Mitä aijot tehdä?")
        time.sleep(1)
        print("\n(1) Istua paikallasi\n(2) Anna oma paikkasi mummelille\n(3) Pyydä jotakuta muuta antamaan paikkansa")
        vaihtoehto=self.kysy(3)
        clear_console()
        #Tarkistaa pelaajan päätöksen ja antaa tai vähentää pisteitä sen mukaan
        if vaihtoehto == 1:
            print("Et välittänyt mummon tilanteesta, menetät 2 ystävällisyys pistettä")
            self.pelaaja.ystavallisuus-=2
            self.pelaaja.aika-=20
            print(f"Sinun ystävällisyys tällä hetkellä:{self.pelaaja.ystavallisuus} pistettä")
        elif vaihtoehto == 2:
            print("Hienoa annoit mummolle paikan, saat 2 ystävällisyys pistettä ja mummo haluaa antaa sinulle pullan")
            time.sleep(3)
            print("Saat yhden pullan")
            self.pelaaja.esinelista.append("pulla")
            self.pelaaja.ystavallisuus+=2
            self.pelaaja.aika-=10
            print(f"Sinun ystävällisyys tällä hetkellä:{self.pelaaja.ystavallisuus} pistettä")
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
                print(f"Sinun ystävällisyys tällä hetkellä:{self.pelaaja.ystavallisuus} pistettä")
            self.pelaaja.aika-=15

            



