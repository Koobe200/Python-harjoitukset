import random

from yleisfunktiot import havio,clear_console
from .asema import Asema


class Helsinki(Asema):
    def __init__(self, nimi, pelaaja):
        super().__init__(nimi,pelaaja)
        
#Tason peli
    def pelaa(self):
       input("Hienoa pääsit jo oikein Leppävaaralle saakka, paina ENTER jatkaaksesi peliä")
       clear_console()
       print("Juna suuntaa kohti Helsinkiä")
       #Arvotaan aika junalle 
       print("Paina ENTER arpoaksesi junalle noepuden saapumiseen")
       input()
       clear_console()
       arvottu_aika=random.randint(1,20)
       print(f"Matka kestää {arvottu_aika} min päästä")
       self.pelaaja.aika-=int(arvottu_aika)
       if self.pelaaja.aika <= 0: 
           havio("Aika loppui kesken :(")
       self.saapuminen()


    #Annetaan pelaajalle eri vaihtoehdot vielä viimeistelemään matkaansa 
    def saapuminen(self):
        print("Juna sapuu Helsingin rautatieasemalle, onneksi olkoon!")
        if "pulla" in self.pelaaja.esinelista:
            print("Kävelessäsi juna-asemalla, kuulet kun lapsi huutaa äitilleen: ÄITI MINULLA ON NÄLKÄ!")
            print("Haluatko:\n(1) Antaa lapselle pullan\n(2)Pitää pullan")
            pulla=self.kysy(2)
            clear_console()
            if pulla == 1:
                print("Lapsi hyppii ilosta! Saat lisää ystävällisyys pisteitä")
                self.pelaaja.ystavallisuus+=2
                print(f"Sinulla on nyt {self.pelaaja.ystavallisuus} ystävällisyys pistettä")
            else: 
                print("Et anna pullaa ja jatkat matkaasi eteenpäin")

        print("Sinun tulee vielä ehtiä opiskelijatapahtumaan, valitse yksi vaihtoehdoista:")
        print("\n(1)Mene ratikalla \n(2)Pyöräile kaupunkipyörällä \n(3)Ota taksi")
        loppu_matka=self.kysy(3)
        clear_console()
        if loppu_matka == 1: 
            print("Hienoa valitsit ympäristöystävällisen vaihtoehdon! Pääset ratikalla perille 10 minuutissa")
            self.pelaaja.aika-=10
        elif loppu_matka == 2: 
            print("Hienoa valitsit ympäristöystävällisen vaihtoehdon JA kuntosi nousee! Pääset pyörällä perille 15 minuutissa")
            self.pelaaja.aika-=15
        else:
            print("Auto ei ole ympäristöystävällinen vaihtoehto ja saastuttaa hirveästi, et pääse perille")   
            havio("Yritti mennä loppuun autolla, tämä ei ole ympäristöystävällistä")   





    

