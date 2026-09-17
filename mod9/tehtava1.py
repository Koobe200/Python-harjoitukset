class Auto:
    def __init__(self,rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinen_nopeus = 0
        self.kuljettu_matka = 2000
    def kiihdyta(self, muutos):
        if self.tamanhetkinen_nopeus + muutos <=0:
            self.tamanhetkinen_nopeus=0
        elif self.tamanhetkinen_nopeus + muutos > self.huippunopeus:
            self.tamanhetkinen_nopeus=self.huippunopeus
        else: 
            self.tamanhetkinen_nopeus += muutos

    def kulje(self, aika):
        self.kuljettu_matka+=aika*self.tamanhetkinen_nopeus
    

        
        

        

auto1 = Auto("ABC-123", 142)

print(f"reskisteritunnus {auto1.rekisteritunnus} nopeus {auto1.huippunopeus} tämänhetkinen nopeus {auto1.tamanhetkinen_nopeus} Kuljettu matka {auto1.kuljettu_matka}")

auto1.kiihdyta(30)
auto1.kiihdyta(70)
auto1.kiihdyta(50)

print('auton nopeus tällä hetkellä:',auto1.tamanhetkinen_nopeus,'km/h')

auto1.kiihdyta(-200)
print('JARRUTUS')
print('auton nopeus tällä hetkellä:',auto1.tamanhetkinen_nopeus,'km/h')


auto1.kiihdyta(60)
auto1.kulje(1.5)

print('auto on kulkenut',auto1.kuljettu_matka,'km')