kuukaudet = ("Talvi", "Talvi", "Kevät", "Kevät", "Kevät", "Kesä", "Kesä", "Kesä", "Syksy", "Syksy", "Syksy", "Talvi")
jarjestysnumero = int(input("Anna Kuukauden järjestysnumero (1-12): "))
kuukausi = kuukaudet[jarjestysnumero - 1]
print('kuukauden',jarjestysnumero,'vuodenaika on', kuukausi)