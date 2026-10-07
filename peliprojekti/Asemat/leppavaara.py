import random
import time
from yleisfunktiot import havio,clear_console
from .asema import Asema



class Leppavaara(Asema):
    def __init__(self, nimi, pelaaja):
        super().__init__(nimi,pelaaja)

    def pelaa(self):
        input("Hienoa! pysyit junassa, paina ENTER jatkaaksesi")
        clear_console()
        print("Juna jatkaa matkaansa kohti Leppävaaraa")
        time.sleep(1)
        print("Huomaat yhtäkkiä, että sinua kohti kävelee lipuntarkastaja, O OUU")
        if "HSL-lippu" in self.pelaaja.esinelista:
            time.sleep(1)
            print("Sinullahan on lippu, hienoa!\n Tarkastaja tarkistaa lippusi ja jatkaa matkaansa")
        else: 
            self.no_lippu()
        time.sleep(1)
        self.juna_seisoo()


    #Antaa pelaajalle 2 vaihtoehtoa miten selviä tilanteesta ilman lippua
    def no_lippu(self):
        print('Sinulla ei ole lippua, koska tiputit sen varastaessasi polkupyörää :(')
        time.sleep(1)
        print('Lipuntarkastaja lähestyy sinua , Sinulla on tässä kohtaa 2 vaihtoehtoa:')
        time.sleep(1)
        print("\n(1) Osta HSL mobiililippu, menetät 30 min ajastasi\n(2) Kerro totuus lipun tarkastajalle")
        vaihtoehto=self.kysy(2)
        clear_console()
        #antaa suoran vaihtoehdon päästä tilanteesta pois mutta pieni rankasu
        if vaihtoehto == 1: 
            print("Ostit HSL-lipun ja menetit ajastasi 30 min")
            self.pelaaja.aika-=30

            print("Lipun tarkastaja tarkastaa lippusi ja voit iloisesti jatkaa matkaa")
            print("Mukavaa päivänjatkoa")

        #Arpoo pääseekö pelaaja karkuun, ystävällisyys lisää todennäköisyyttä päästä karkuun
        else:
            print("Päätät kertoa totuuden lipuntarkastajalle")
            time.sleep(1)
            print("Tarkastaja miettii hetken mitä tekee")
            time.sleep(1)
            print("Paina ENTER arpoaksesi vakuuttavuusluku, jolla saat tarkastajan vakuutettua, sinun tulee saada yli 3")
            input("\n")
            vakuuttavuus=random.randint(1,6)
            print("Ystävällisyys taso vaikuttaa vahvasti tulokseen")
            vakuuttavuus+=self.pelaaja.ystavallisuus

            if vakuuttavuus > 3:
                print("Hienoa! sait tarkastajan vakuutettua")
                time.sleep(1)
                print("Lipun tarkastaja päättää antaa sinun jatkaa matkaa")

            else:
                print("Et saanut tarkastajaa vakuutettua ")
                havio("Ei saanut tarkastajaa vakuutettua, lensit junasta ulos")
                time.sleep(1)            
    def juna_seisoo(self):
        print("Juna pysähtyy yhtäkkiä keran asemalle")
        time.sleep(1)
        print("Junan kuljettaja kuuluttaa, että juna on joutunut pysähtymään opastinvian takia")
        time.sleep(1)
        print("Sinulla on 2 vaihtoehtoa:")
        print("\n(1) Älä tee mitään, odota kunnes ongelma ratkeaa\n(2) Mene auttamaan kuljettajaa")
        if "pyörä" in self.pelaaja.esinelista: #Antaa kolmannen vaihtoehdon jos on varastanut pyörän
            print("(3) Hae varastettu pyöräsi ja pyöräile seuraavalle asemalle")
            vaihtoehto=self.kysy(3)
        else:
            vaihtoehto=self.kysy(2)
        clear_console()
        if vaihtoehto == 1: #rankaisee pelaajan laiskuutta
            print("Jäit paikallesi odottamaan kunnes ongelma ratkeaa, menetät 30 min ajastasi")
            self.pelaaja.aika-=30
        elif vaihtoehto == 2:
            print("Menet auttamaan kuljettajaa")
            print("Kuljettaja sanoo, että tarvitsee apua löytämään oikea koodi, jotta voi laittaa junan taas liikkeelle")
            print("koodi koostuu kolmesta numerosta, jotka ovat kaikki 1-3 välillä, jokainen luku on eri ")
            #Pelaajan tulee arvaa koodi, sillä on 5 mahdollisuutta päästä lopputulokseen
            koodi=312
            oikein=False
            for i in range(0,5):
                print(f"sinulla on {5-i} verran kertoja arvata oikea numero")
                vastaus=input("Arvaa numero tähän:")

                if str(vastaus) == str(koodi):
                    print(f"Mahtavaa, arvasit koodin: {koodi} oikein!!!")
                    oikein=True
                    break
                else:
                    print("Nyt ei menny ihan nappiin :(")
            if oikein == False:
                print(f"Oikea koodi olisi ollut: {koodi}")
                self.pelaaja.aika-=30
            else:
                self.pelaaja.aika-=10
        # Rankaistaan pelaajaa pyörän varastamisesta
        else:
            print("Menet hakemaan pyörääsi ")
            time.sleep(1)
            print("Huomaat, että pyöräsi on poissa.")
            time.sleep(1)
            print("Siinä opetus ettei kannata varastaa toisten ihmisten pyöriä")
            time.sleep(1)
            print("Menetät aikaa 30 min")
            time.sleep(1)
            self.pelaaja.esinelista.remove("pyörä")
            self.pelaaja.aika-=30


