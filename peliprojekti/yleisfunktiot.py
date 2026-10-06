import sys
import os
import json


def age_check():
    nimi = input('Mikä nimesi on? ')    
    age = int(input('Mikä ikäsi on vuosina? '))

    if age < 12:
        print('olet vain',age,', eli alaikäinen, et voi pelata tätä peliä.' )
        print('Sinun tulee olla vähintään 12v' )
        print('Et voi valitettavasti pelata peliä :(')
        sys.exit()
    else:
        print('Hei!, Nimesi on ', nimi, ' ja ikäsi on ',age,'v' )
        return nimi
        

def kysy_valinta(vaihtoehdot,pelaaja=None):

    while True:
        valinta= input()
        if valinta == "valikko":
            pikku_valikko(pelaaja)
            continue
        try:
            valinta=int(valinta)
            if 1 <= valinta <= vaihtoehdot:
                return valinta
            else:
                print (f"Valitse numero väliltä 1 ja {vaihtoehdot} ")
        except ValueError:
            print("Anna kelpaava arvo")

def havio(syy):
    print(f"Syy:{syy}")
    print("Hävisit pelin :(")
    sys.exit()


def tallenna(pelaaja):
  print("Valitse yksi talennus sloteista:")
  talennus_lista={"[1]":"tyhjä","[2]":"tyhjä","[3]":"tyhjä","[4]":"tyhjä"}
  for slotti, arvo in talennus_lista.items():
    print(f"{slotti}: {arvo}")
  talennus=kysy_valinta(4)
  if talennus == 1: 
     number=1
  elif talennus == 2:
     number=2 
  elif talennus == 3:
     number=3
  else: 
     number=4
  peli_tallennus={
      "nimi": pelaaja.nimi,
      "Sijainti": pelaaja.sijainti,
      "esinelista": pelaaja.esinelista,
      "aika": pelaaja.aika,
      "ystavallisyys": pelaaja.ystavallisuus
  }
  with open(f"save{number}.json", "w") as tiedosto:
    json.dump(peli_tallennus, tiedosto)
  pikku_valikko(pelaaja)

def avaa_tallennus(pelaaja):
  print("Valitse yksi talennus sloteista:")
  talennus_lista={"[1]":"tyhjä","[2]":"tyhjä","[3]":"tyhjä","[4]":"tyhjä"}
  for slotti, arvo in talennus_lista.items():
    print(f"{slotti}: {arvo}")
  talennus=kysy_valinta(4)
  if talennus == 1: 
     number=1
  elif talennus == 2:
     number=2 
  elif talennus == 3:
     number=3
  else: 
     number=4
  peli_tallennus={
      "nimi": pelaaja.nimi,
      "Sijainti": pelaaja.sijainti,
      "esinelista": pelaaja.esinelista,
      "aika": pelaaja.aika,
      "ystavallisyys": pelaaja.ystavallisuus
  }
  with open(f"save{number}.json", "r") as tiedosto:
    talennus=json.load(tiedosto) 

  pelaaja.nimi=talennus['nimi']
  pelaaja.sijainti=talennus['sijainti']
  pelaaja.esinelista=talennus['esinelista']
  pelaaja.aika=talennus['aika']
  pelaaja.ystavallisuus=talennus['ystavallisyys']

    




def pikku_valikko(pelaaja):
    print("Tervetuloa pikkuvalikkoon, valitse yksi vaihtoehdoista")
    print("(1) jatka\n(2) Talenna\n(3)palaa pää valikkoon ")
    valikko_valinta=kysy_valinta(3)
    if valikko_valinta == 1: 
       return
    elif valikko_valinta == 2:
       tallenna(pelaaja)
    elif valikko_valinta == 3:
       pass