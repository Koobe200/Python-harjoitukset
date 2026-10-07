from yleisfunktiot import age_check
from pelaaja import Pelaaja
from paavalikko import paavalikko


# Peli käynnistetään tästä tiedostosta


#Tarkistetaan pelaajan nimi ja ikä
nimi=age_check()

#Luodaan pelaaja olio
pelaaja=Pelaaja(nimi)

#Käynnistetään päävalikko
paavalikko(pelaaja)