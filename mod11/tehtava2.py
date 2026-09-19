import random


class Auto:
    def __init__(self,nimi,huippunopeus):
        self.nimi=nimi
        self.nopeus=100
        self.automatka=0
        self.huippunopeus=huippunopeus

    def tulosta(self):
        print(f"Nimi: {self.nimi} | Huippunopeus: {self.huippunopeus}km/h | Automatka:{self.automatka}km")
    def kiihdyta(self):
        self.nopeus+=random.randint(-10,15)
        if self.nopeus > self.huippunopeus:
            self.nopeus=self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus=0

    def kulje(self):
        self.automatka+=self.nopeus

class Sahkoauto(Auto):
    def __init__(self,nimi,huippunopeus,akku_kapasiteetti):
        self.akku_kapasiteetti=akku_kapasiteetti
        super().__init__(nimi,huippunopeus)
    def tulosta(self):
        super().tulosta()
        print(f"Akkukapasiteetti: {self.akku_kapasiteetti} kw/h")   
        print("-------------------------------------------------------")
        
        
class Polttomoottoriauto(Auto):
      def __init__(self,nimi,huippunopeus,tankin_koko):
            self.tankin_koko=tankin_koko
            super().__init__(nimi,huippunopeus)
      def tulosta(self):
            super().tulosta()
            print(f"Tankin litra koko: {self.tankin_koko} l")
            print("-------------------------------------------------------")
             

tesla=Sahkoauto("ABC-15",180,52.5,)
volvo=Polttomoottoriauto("ABC-123",165,32.3)

for i in range(3):
    tesla.kiihdyta()
    tesla.kulje()

for i in range(3):
    volvo.kiihdyta()
    volvo.kulje()

tesla.tulosta()
volvo.tulosta()








    
    



