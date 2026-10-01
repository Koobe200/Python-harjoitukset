#with open("ostoslista.txt", "a") as tiedosto:
 #   tiedosto.write("\nmaito\n")
   # tiedosto.write("leipä\n")
  #  tiedosto.write("kanamunat\n")
  #  tiedosto.write("omenat\n")


while True:
   try:
    tiedosto_user=input('Anna tiedosto:')
    with open(tiedosto_user, "r") as tiedosto:
        data = tiedosto.read()
        print(data)
        break
   except FileNotFoundError:
        print("Tiedostoa ei löydy, yritä uudelleen")
   except IOError:
        print("Tiedoston käsittelyssä tapahtui virhe.")