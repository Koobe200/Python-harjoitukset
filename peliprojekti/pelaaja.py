class Pelaaja:
    def __init__(self,nimi):
        self.nimi=nimi #pelaajan nimi
        self.sijainti=0  # Kertoo millä asemalla mennään
        self.esinelista=[] #Kertoo mitä esineitä pelaajalla on
        self.aika=120 #Kertoo kuinka paljon aikaa pelaajalla on 
        self.ystavallisuus=0 #Lisää pisteitä lopusssa huomattavasti
        
