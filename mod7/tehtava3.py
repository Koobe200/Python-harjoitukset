#Laskee Gallonit litroiksi
def gallontolitra(gallon):
    litra=float(gallon)*3.785
    return litra

#While silmukka, joka toistaa kunnes luku on negatiivinen
while True:
    alkugallon=float(input('Anna bensiinin määrä Yhdysvaltain nestegalloneina '))
    if alkugallon < 0:
        print('Annoit negatiivisen luvun, ohjelma loppuu')
        break 
    else: 
        #käyttää funktiota ja antaa tuloksen 
        litrat=gallontolitra(alkugallon)
        print(alkugallon,'Gallonia on ', litrat, 'litraa')