

def intro():
    jatka=True
    nimi = input('Mikä nimesi on? ')    
    age = int(input('Mikä ikäsi on vuosina? '))

    if age < 12:
        print('olet vain',age,', eli alaikäinen, et voi pelata tätä peliä.' )
        print('Sinun tulee olla vähintään 12v' )
        jatka=False
        return jatka
    else:
        print('Hei!, Nimesi on ', nimi, ' ja ikäsi on ',age,'v' )
        return jatka
        

        