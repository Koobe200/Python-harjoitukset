lukujono=[]

while True: 
    luku = input('Anna luku: ')
    if luku == "": 
        break 
    else:
        lukujono.append(float(luku))


print('Pienin luku', min(lukujono))
print('Suurin luku', max(lukujono))