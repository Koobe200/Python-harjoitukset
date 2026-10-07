import sys
import os
import json




kansio = os.path.dirname(os.path.abspath(__file__))    
talennus_kansio=os.path.join(kansio, "talennukset")
os.makedirs(talennus_kansio, exist_ok=True)


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
  talennus_lista={"[1]":check_slot(1),"[2]":check_slot(2),"[3]":check_slot(3),"[4]":check_slot(4)}
  for slotti, arvo in talennus_lista.items():
    print(f"{slotti}: {arvo}")
  number=kysy_valinta(4)
  peli_tallennus={
      "nimi": pelaaja.nimi,
      "sijainti": pelaaja.sijainti,
      "esinelista": pelaaja.esinelista,
      "aika": pelaaja.aika,
      "ystavallisyys": pelaaja.ystavallisuus
  }
  talennus=os.path.join(talennus_kansio, f"save{number}.json")
  with open(talennus, "w") as tiedosto:
    json.dump(peli_tallennus, tiedosto)
  pikku_valikko(pelaaja)

def avaa_tallennus(pelaaja):
  print("Valitse yksi talennus sloteista:")
  talennus_lista={"[1]":check_slot(1),"[2]":check_slot(2),"[3]":check_slot(3),"[4]":check_slot(4)}
  for slotti, arvo in talennus_lista.items():
    print(f"{slotti}: {arvo}")
  number=kysy_valinta(4)
  talennus = os.path.join(talennus_kansio, f"save{number}.json")
  try:
    with open(talennus, "r") as tiedosto:
        talennus=json.load(tiedosto) 
  except FileNotFoundError:
     print("Tyhjä slotti")
     return False

  pelaaja.nimi=talennus['nimi']
  pelaaja.sijainti=talennus['sijainti']
  pelaaja.esinelista=talennus['esinelista']
  pelaaja.aika=talennus['aika']
  pelaaja.ystavallisuus=talennus['ystavallisyys']

  return True



def pikku_valikko(pelaaja):
    print("Tervetuloa pikkuvalikkoon, valitse yksi vaihtoehdoista")
    print("(1) jatka\n(2) Talenna\n(3)palaa pää valikkoon ")
    valikko_valinta=kysy_valinta(3)
    if valikko_valinta == 1: 
       return 
    elif valikko_valinta == 2:
       tallenna(pelaaja)
    elif valikko_valinta == 3:
       from paavalikko import paavalikko
       paavalikko(pelaaja)

def check_slot(number):
   talennuspath=os.path.join(talennus_kansio, f"save{number}.json")
   print(talennuspath)
   if os.path.exists(talennuspath):
      talennuslista="Käytössä"
   else:
      talennuslista="tyhjä"
   return talennuslista