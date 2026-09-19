import random



class Auto:
    def __init__(self,nimi):
        self.nimi=nimi
        self.nopeus=0
        self.automatka=0
        self.huippunopeus=0


    def alkuperainen_nopeus(self):
        self.huippunopeus=random.randint(100,200)

    def tulosta(self):
    

        print(f"Nimi: {self.nimi} | Huippunopeus: {self.huippunopeus}km/h | Automatka:{self.automatka}km")
        print("-------------------------------------------------------")

    def kiihdyta(self):
        self.nopeus+=random.randint(-10,15)
        if self.nopeus > self.huippunopeus:
            self.nopeus=self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus=0


    def kulje(self):
        self.automatka+=self.nopeus



def autolista():

    for i in range(0,10):
        auto=Auto("ABC-"+str(i+1))
        auto.alkuperainen_nopeus()
        autot.append(auto)

class Kilpailu:

    def __init__(self, nimi, km_maara, autot):
        self.nimi=nimi
        self.km_maara=km_maara
        self.autot=autot
        self.matka_yli=False

    def tunti_kulunut(self):
        for auto in self.autot:
            auto.kiihdyta()
            auto.kulje()
    def tulosta_tilanne(self):
        for auto in self.autot:
            auto.tulosta()
    def kilpailu_ohi(self):
        for auto in self.autot:
                if auto.automatka >= self.km_maara:
                     self.matka_yli=True


            
autot=[]
autolista()
suuri_romuralli=Kilpailu("Suuri romuralli",8000,autot)

for auto in autot:
    auto.tulosta()


print('                                ')
print('-------------------------------------------------------')


while True:

    for i in range(0,10):
        suuri_romuralli.tunti_kulunut()
        suuri_romuralli.kilpailu_ohi()
    suuri_romuralli.tulosta_tilanne()

    if suuri_romuralli.matka_yli == True:
        print('kilpailu on päättynyt. Tulokset: ')
        suuri_romuralli.tulosta_tilanne()
        break

    
    



