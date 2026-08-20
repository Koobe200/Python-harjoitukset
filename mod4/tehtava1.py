
while True:
    pituus = input('kuinka pitkä on kuha: ')
    lyhyt= 37 - float(pituus)
    if float(pituus) > 37: 
        print('kuha on sopiva')
        break
    else:
        print('Kuha on',lyhyt, 'cm liian lyhyt, heitä veteen')
    

