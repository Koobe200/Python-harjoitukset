import sys

def kysy_valinta(vaihtoehdot):

    while True:
        try:
            valinta= int(input())
            if 1 <= valinta <= vaihtoehdot:
                return valinta
            else:
                print (f"Valitse numero väliltä 1 ja {vaihtoehdot} ")
        except ValueError:
            print("Anna kelpaava arvo")

def havio(syy):
    print("Jouduit junasta ulos")
    print(f"Syy:{syy}")
    print("Hävisit pelin :(")
    sys.exit()
