luoti = 13.3
naula = 32 * luoti
leivisk = 20 * naula

leiviskm = input('anna leiviskät: ')

naulam = input('anna naulat: ')

luotim = input('anna luodit: ')

summa = float(luoti)*float(luotim)+float(naula)*float(naulam)+float(leivisk)*float(leiviskm)

print('Massa nykymittojen mukaan:')

kilogramma = summa/1000

print(int(kilogramma), 'kilogrammaa')

gramma = summa - (int(kilogramma)*1000)
rounded_gramma = round(gramma, 3)
print(float(rounded_gramma), 'grammaa')