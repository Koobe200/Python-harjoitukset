import sys
import os
import json

# Määritellään tallennusten polku
kansio = os.path.dirname(os.path.abspath(__file__))    
talennus_kansio=os.path.join(kansio, "talennukset")
os.makedirs(talennus_kansio, exist_ok=True)

# Pyydetään pelaajan nimi ja tarkistetaan ikä
def age_check():
    nimi = input('Mikä nimesi on? ')    
    while True:
        syote=input('Mikä ikäsi on vuosina? ')
        try:
            age = int(syote)
            break
        except ValueError:
            print("Anna kelpaava arvo")
    

    if age < 12:
        print('olet vain',age,', eli alaikäinen, et voi pelata tätä peliä.' )
        print('Sinun tulee olla vähintään 12v' )
        print('Et voi valitettavasti pelata peliä :(')
        sys.exit()
    else:
        print('Hei!, Nimesi on ', nimi, ' ja ikäsi on ',age,'v' )
        clear_console()
        return nimi


#Pelin kaikkia input tilanteita varten tehty funktio, joka tarkistaa syötteen numeroksi ja onko se vaihtoehtojen sisällä. 
# Lisäksi sallii pikku valikon avaamisen    
def kysy_valinta(vaihtoehdot,pelaaja=None):

    while True:
        valinta= input()
        if valinta == "valikko":
            if pelaaja != None:
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


# Käytetäään pelissä aina häviöiden sattuessa
def havio(syy):
    print(f"Syy:{syy}")
    print("Hävisit pelin :(")
    sys.exit()

# Pelin talennus, toimii vain pikku-valikossa 
def tallenna(pelaaja):
  print("Valitse yksi tallennus sloteista:")
  talennus_lista={"[1]":check_slot(1),"[2]":check_slot(2),"[3]":check_slot(3),"[4]":check_slot(4)}
  for slotti, arvo in talennus_lista.items():
    print(f"{slotti}: {arvo}")
  number=kysy_valinta(4)

# Tarkistaa onko slotti jo käytössä ja varoittaa pelaajaa ennen sen ylikirjaamista
  if check_slot(number) == "Käytössä":
     print("slotti on jo käytössä, haluatko ylikirjoittaa sen")
     print("(1) Kyllä\n(2) Ei")
     yli_kirjoitus=kysy_valinta(2)
     if yli_kirjoitus== 2:
        return


  peli_tallennus={
      "nimi": pelaaja.nimi,
      "sijainti": pelaaja.sijainti,
      "esinelista": pelaaja.esinelista,
      "aika": pelaaja.aika,
      "ystavallisyys": pelaaja.ystavallisuus
  }
  
  talennus=os.path.join(talennus_kansio, f"save{number}.json")
  with open(talennus, "w",encoding="utf-8") as tiedosto:
    json.dump(peli_tallennus, tiedosto, ensure_ascii=False)
  print("tallennettu")
  pikku_valikko(pelaaja)



# Päävalikossa toimiva talennusten avaus funktio
def avaa_tallennus(pelaaja):
  print("Valitse yksi talennus sloteista:")
  talennus_lista={"[1]":check_slot(1),"[2]":check_slot(2),"[3]":check_slot(3),"[4]":check_slot(4)}
  for slotti, arvo in talennus_lista.items():
    print(f"{slotti}: {arvo}")
  number=kysy_valinta(4)
  talennus = os.path.join(talennus_kansio, f"save{number}.json")
  try:
    with open(talennus, "r", encoding="utf-8") as tiedosto:
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


# Valikko jonka voi avata milloin vain pelin aikana, sallii talennuksen ja päävalikkoon siirtymisen
def pikku_valikko(pelaaja):
    print("Tervetuloa pikkuvalikkoon, valitse yksi vaihtoehdoista")
    print("(1) jatka\n(2) Tallenna\n(3)palaa pää valikkoon ")
    valikko_valinta=kysy_valinta(3)
    if valikko_valinta == 1: 
       return 
    elif valikko_valinta == 2:
       tallenna(pelaaja)
    elif valikko_valinta == 3:
       from paavalikko import paavalikko
       paavalikko(pelaaja)

# Tarkistaa onko talennus slotti käytössä
def check_slot(number):
   talennuspath=os.path.join(talennus_kansio, f"save{number}.json")
   if os.path.exists(talennuspath):
      talennuslista="Käytössä"
   else:
      talennuslista="tyhjä"
   return talennuslista


#Käytetään monesti tyhjentämään konsoolia, jotta näkymä ei täyty liialisilla riveillä tekstiä
def clear_console():
   os.system('cls' if os.name=='nt' else 'clear')

    