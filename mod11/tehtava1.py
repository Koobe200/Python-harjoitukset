class Julkaisu:
    def __init__ (self, nimi):
        self.nimi=nimi

         

class Kirja(Julkaisu):
    def __init__ (self, nimi, kirjoittaja, sivu_maara):
            self.kirjoittaja=kirjoittaja
            self.sivu_maara=sivu_maara
            super().__init__(nimi)
    def tulosta_tiedot(self):
         print(f"Kirjan nimi:{self.nimi}")
         print(f"Kirjoittaja: {self.kirjoittaja} ja sivumäärä: {self.sivu_maara}")

class Lehti(Julkaisu):
    def __init__ (self, nimi,paatoimittaja):
        self.paatoimittaja=paatoimittaja
        super().__init__(nimi)
    def tulosta_tiedot(self):
         print(f"Lehden nimi: {self.nimi}")
         print(f"Päätoimittaja on: {self.paatoimittaja}")


aku_ankka=Lehti("Aku Ankka","Aki Hyyppä")
hytti_6=Kirja("Hytti n:o 6","Rosa Liksom", 200)


aku_ankka.tulosta_tiedot()
hytti_6.tulosta_tiedot()