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



autot = []

autolista()


for auto in autot:
    auto.tulosta()


print('                                ')
print('-------------------------------------------------------')

matka_yli=False
while True:
    for auto in autot:
        auto.kiihdyta()
        auto.kulje()
 
    
    for auto in autot:
        if auto.automatka >= 10000:
             matka_yli=True

    if matka_yli:
        break
for auto in autot:
    auto.tulosta()

