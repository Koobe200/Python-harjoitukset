from yleisfunktiot import kysy_valinta


class Asema:
    def __init__(self,nimi, pelaaja):
        self.nimi=nimi #Aseman nimi
        self.pelaaja=pelaaja #Määrittää pelaajan kaikille asemille
        
#erikseen kysy valinta peliin, joka ottaa pelaaja parametrin mukaan 
    def kysy(self,vaihtoehdot):
        return kysy_valinta(vaihtoehdot, self.pelaaja) 