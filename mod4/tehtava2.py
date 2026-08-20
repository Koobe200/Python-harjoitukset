luokka = input('Valitse ykis hyttiluokista: LUX, A, B, C:')

luokkatulos = luokka.upper()

if luokkatulos == 'LUX': 
    print('LUX on parvekkeellinen hytti yläkannella.')
elif luokkatulos == 'A':
    print('A on ikkunallinen hytti autokannen yläpuolella.')
elif luokkatulos == 'B':
    print('B on ikkunaton hytti autokannen yläpuolella.')
elif luokkatulos == 'C':
    print('C on ikkunaton hytti autokannen alapuolella.')
else:
     print('Virheellinen hyttiluokka')