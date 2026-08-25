sukupuoli = input('Mikä on sukupuolesi? ')
sukupuoliarv= sukupuoli.upper()
hemoglobiini= int(input('Mikä on hemoglobiiniarvo '))


if sukupuoliarv == 'NAINEN':
    if hemoglobiini < 117:
        print('arvo on liian alhainen')
    elif hemoglobiini > 175:
        print('arvo on liian korkea')
    else:
        print('arvo on sopiva')
    
elif sukupuoliarv == 'MIES':
    if hemoglobiini < 134:
        print('arvo on liian alhainen')
    elif hemoglobiini > 195:
        print('arvo on liian korkea')
    else:
        print('arvo on sopiva')
else:
    print('ei ole valitettavasti vaihtoehtoinen sukupuoli tässä ohjelmassa')