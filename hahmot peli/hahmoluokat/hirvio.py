from .hahmo import Hahmo

class Merihirvio(Hahmo):

    def __init__(self,nimi,repliikki):

        self.repliikki = repliikki
        super().__init__(nimi)
    def tulosta_tiedot(self):
            super().tulosta_tiedot()
            print(self.repliikki)

   