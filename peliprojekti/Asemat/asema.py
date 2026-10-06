from yleisfunktiot import kysy_valinta


class Asema:
    def __init__(self,nimi, pelaaja):
        self.nimi=nimi
        self.pelaaja=pelaaja

    def pelaa(self):
        pass

    def kysy(self,vaihtoehdot):
        return kysy_valinta(vaihtoehdot, self.pelaaja)