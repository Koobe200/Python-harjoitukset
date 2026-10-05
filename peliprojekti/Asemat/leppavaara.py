import random
import time
from yleisfunktiot import kysy_valinta,havio
from .asema import Asema



class Leppavaara(Asema):
    def __init__(self, nimi, pelaaja):
        super().__init__(nimi,pelaaja)

    def pelaa(self):
        print("Juna jatkaa matkaansa kohti leppävaaraa")
        time.sleep(2)
        print("Huomaat yhtäkkiä, että sinua kohti kävelee lipuntarkastaja, O OUU")
        #arvotaan pelaajalle aikamäärä
        if "HSL-lippu" in self.pelaaja.esinelista:
            print("Sinullahan on lippu, hienoa!\n Tarkastaja tarkistaa lippusi ja jatkaa matkaansa")
        else: 
            self.no_lippu()
        time.sleep(3)
        self.juna_seisoo()
    
    def no_lippu(self):
        print('Sinulla ei ole lippua, koska tiputit sen varastaessasi polkupyörää :(')
        print('Lipuntarkastaja lähestyy sinua...')
        time.sleep(3)
        print('Lipun tarkastaja lähestyy sinua , Sinulla on tässä kohtaa 2 vaihtoehtoa:')
        print("(1)Osta HSL mobiili lippu, menetät 20 min ajastais\n(2)Kerro totuus lipun tarkastajalle")
        vaihtoehto=kysy_valinta(2)

        if vaihtoehto == 1: 
            print("Ostit HSL-lipun ja menetit ajastasi 20 min")
            self.pelaaja.aika=-20

            print("Lipun tarkastaja tarkastaa lippusi ja voit iloisesti jatkaa matkaa")
            print('"Mukavaa päivänjtakoa')


        else:
            print("Päätät kertoa totuuden lipun tarkastajalle")
            print("Tarkastaja miettii hetken mitä tekee")
            time.sleep(2)
            print("Paina ENTER arpoaksesi vakuuttavuusluku, jolla saat tarkastajan vakuutettua, sinun tulee saada yli 3")
            input()
            vakuuttavuus=random.randint(1,6)
            print("Ystävllisyytäsi taso vaikuttaa vahvasti tulokseen")
            vakuuttavuus=+self.pelaaja.ystavallisuus

            if vakuuttavuus > 3:
                print("Hienoa! sait tarkastajan vakuutettua")
                print("Lipun tarkastaja tarkastaa lippusi ja voit iloisesti jatkaa matkaa")
                print('"Mukavaa päivänjatkoa')

            else:
                print("Et saanut tarkastajaa vakuttettua ")
                havio("Ei saanut vakuutettua tarkastajaa ilman lippua")

            
    def juna_seisoo(self):
        print("Juna pysähtyy yhtäkkiä keran asemalle")
        time.sleep(2)
        print("Junan kuljettaja kuuluttaa, että juna on joutunut pysähtymään opastinvian takia")
        time.sleep(2)
        print("Sinulla on 3 vaihtoehtoa:")
        print("(1) Älä tee mitään, odota kunnes ongelma ratkeaa\n(2) Mene auttamaan kuljettajaa")
        if "pyörä" in self.pelaaja.esinelista:
            print("(3) Hae varastettu pyöräsi ja pyöräile seuraavalle asemalle")
        vaihtoehto=kysy_valinta(3)
        if vaihtoehto == 1:
            print("Jäit paikallesi odottamaan kunnes ongelma ratkeaa, menetät 30 min ajastasi")
            self.pelaaja.aika=-30
        elif vaihtoehto == 2:
            print("Menet auttamaan kuljettajaa")
            print("Kuljettaja sanoo, että tarvitsee apua löytämään oikea koodi, jotta voi laittaa junan taas liikkeelle")
            print("koodi koostuu kolmesta numerosta, jotka ovat kaikki 1-3 väälillä")
            num1=random.randint(1,3)
            num2=random.radint(1,3)
            num3=random.randint(1,3)
            koodi=str(num1)+str(num2)+str(num3)

            for i in range(0,9):
                print(f"sinulla on {9-i} verran kertoja arvata oikea numero")
                vastaus=input("Arvaa numero tähän:")

                if str(vastaus) == str(koodi):
                    print(f"Mahtavaa, arvasit koodin: {koodi} oikein!!!")
                    break
                else:
                    print("Nyt ei menny ihan nappiin :(")
                    print(f"Oikea koodi olisi ollut: {koodi}")

        else:
            print("Menet hakemaan pyörääsi ")
            print("Huomaat, että pyöräsi on poissa.")
            print("Siinä opetus ettei kannata varastaa toisten ihmisten pyöriä")
            print("Menetät aikaa 30 min")
            self.pelaaja.esinelista.remove("pyörä")
            self.pelaaja.aika=-30


