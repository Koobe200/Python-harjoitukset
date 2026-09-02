import math
alkuluku = int(input('anna jokin alkuluku '))

onkoalkuluku=True

if alkuluku < 2:
    onkoalkuluku=False
else: 
    for i in range(2, int(math.sqrt(alkuluku)+1)):
        if alkuluku % i == 0:
            onkoalkuluku=False
            break

if onkoalkuluku == True:
    print('luku',alkuluku,'on alkuluku')
else:
    print('luku',alkuluku,'ei ole alkuluku')