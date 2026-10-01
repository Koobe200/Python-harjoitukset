from .hahmo import Hahmo

class Pelaajahahmo(Hahmo):

    def __init__(self,nimi, tavaralista):
        self.tavaralista=tavaralista
        super().__init__(nimi)
    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        for i in self.tavaralista:
            print(f'-{i}')
      