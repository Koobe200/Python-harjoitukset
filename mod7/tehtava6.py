import math

def pizzahinta(halkaisija,hinta):
    sade=halkaisija/2
    pintala=sade**2*math.pi
    hintapernelio=pintala/hinta

    return hintapernelio



piza1halk=float(input('anna ensimmäisen pitsan halkaisija sentteinä: '))
piza1hinta=float(input('anna ensimmäisen pitsan hinta euroina: '))


piza2halk=float(input('anna toisen pitsan halkaisija  sentteinä: '))
piza2hinta=float(input('anna toisen pitsan hinta euroina: '))

piza1=pizzahinta(piza1halk,piza1hinta)
print('Ensimmäisen pitsan hinta neliömetreiltä on',piza1, 'euroa')
piza2=pizzahinta(piza2halk,piza2hinta)
print('toisen pitsan hinta neliömetreiltä on',piza2, 'euroa')

if piza1 < piza2:
    print('Ensimmäisellä pitsalla on parempi hinta laatu suhde')
else:
    print('Toisella pitsalla on parempi hinta laatu suhde')