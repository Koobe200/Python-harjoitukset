nimi = input('Mikä on hahmon nimi: ')

print('Olipa kerran',nimi,',joka lähti avaruuteen seikkailee.')
print(nimi, 'pitää valita joko raketti tai vene matkustamiseen,')
ajoneuvo= input('kumman hän valitsee? ')
ajoneuvo=ajoneuvo.upper()
if ajoneuvo == 'RAKETTI':
    print(nimi,'pääsee kovaa vauhtia kuuhun saakka')
elif ajoneuvo == 'VENE':
    print(nimi,'pääsee soutamaan Talinnaan')
else: 
     print(nimi,'ei pysty tänään kulkea tuolla ajoneuvolla')