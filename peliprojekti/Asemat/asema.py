from .kirkkonummi import kirkkonummi_taso
from .espoo import Espoo_taso


class Asema:
    def __init__(self,nimi,pelaaja):
        self.nimi=nimi
        self.pelaaja=pelaaja

    def kirkkonummi(self):
        print(f"sinulla on {self.pelaaja.aika} min aikaa päästä määränpäähän")
        kirkkonummi_taso(self.pelaaja)
    def espoo(self):
        print(f"sinulla on {self.pelaaja.aika} min aikaa päästä määränpäähän")
        Espoo_taso(self.pelaaja)
    
