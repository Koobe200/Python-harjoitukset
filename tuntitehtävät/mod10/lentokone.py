class Lentokone:
    def __init__(self,nimi,bensa_maks):
        self.nimi= nimi
        self.bensa_maks=bensa_maks
        self.bensa_nyky=0

    def tankkaa(self):

        print(self.bensa_maks-self.bensa_nyky)
        self.bensa_nyky=self.bensa_maks

    def tulosta(self):
        print(f"Nimi: {self.nimi}\nMaksimi bensa: {self.bensa_maks}\nNykyinen bensa:{self.bensa_nyky}")

class Lentokentta:
    def __init__(self,nimi):
            self.nimi = nimi
            self.lentokonelista = []

    def lisaa_lentokone(self, lentokone):
        self.lentokonelista.append(lentokone)

    def tulosta_koneet(self):
         for lentokone in self.lentokonelista:
              lentokone.tulosta()
         
  
lentokentta = Lentokentta("Vantaa")
lentokone1 = Lentokone("Airbus 320", 100)
lentokone1.tankkaa()
lentokone2 = Lentokone("Airbus 350", 400)
lentokone3 = Lentokone("Boeing 747", 1000)
lentokone4 = Lentokone("Embrear 190", 100)

lentokentta.lisaa_lentokone(lentokone1)
lentokentta.lisaa_lentokone(lentokone2)
lentokentta.lisaa_lentokone(lentokone3)
lentokentta.lisaa_lentokone(lentokone4)

lentokentta.tulosta_koneet()
