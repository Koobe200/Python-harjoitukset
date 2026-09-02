
lista=[]

while True:
    luku=input('anna luku: ')
    if luku == "":
        break
    lista.append(int(luku))

lista.sort(reverse=True)



print(lista[0:5])
