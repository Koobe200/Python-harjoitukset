pituus = int(input('kuinka pitkä olet (cm): '))
ika = int(input('kuinka vanha olet: '))
if pituus < 195:
    if pituus > 140 and ika > 8: 
        print('Voit mennä kaikkiin laitteisiin!')
    elif pituus > 140 and ika < 8: 
        print('Voit mennä melkein kaikkiin laitteisiin, mutta harmillisesti et Tulirekeen')
    elif pituus > 100:
        print('saat mennä lasten laitteisiin, Yippee!')
    else:
        print('olet liian lyhyt :( et pääse mihinkään laitteisiin')
else:
    print('HUH! pitkä tyyppi, et pääse Kirnuun, mutta muihin laitteisiin, mee vaa!')
