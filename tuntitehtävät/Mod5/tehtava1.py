print('Tervetuloa laskimeen!')
valinta_main=""
while True:
    menu_list = "select option:\n1. PLUS\n2. MIINUS \n3. KERTOLASKU \n0 LOPETUS'\n"
    valinta_main= int(input(menu_list))
    if valinta_main == 0:
        break
    else:
        lasku1= float(input('valitse ensimmäinen numero: '))
        lasku2= float(input('valitse toinen numero: '))
        if valinta_main == 1:
            print('valitsit pluslaskun')
            print('summa on',lasku1+lasku2)
        elif valinta_main == 2:
            print('valitsit miinuslaskun')
            print('summa on',lasku1 - lasku2)
        elif valinta_main == 3:
            print('valitsit kertolaskun')
            print('Tulos on',lasku1 ** lasku2)
        else:
            print('tämä ei ole vaihtoehto')