vuosiluku= int(input('Anna vuosiluku '))
if vuosiluku > 2026:
    print('vuosi on tulevaisuudessa')
elif vuosiluku == 2020: 
    print('Ei ollut olymppiavuosi koronan takia')
elif vuosiluku % 4 == 0: 
    print('Vuosi oli olymppiavuosi')
elif vuosiluku == 2021: 
    print('Vuosi oli poikeuksellisesti olymppiavuosi')
else:
    print('Ei ollut olymppiavuosi')
