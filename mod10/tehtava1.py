class Hissi: 
    def __init__(self, ylin_kerros, alin_kerros):
        self.alin_kerros=alin_kerros
        self.ylin_kerros=ylin_kerros
        self.kerros=self.alin_kerros

    def siirry_kerrokseen(self,tavoite_kerros):
        while True: 
            if self.kerros == tavoite_kerros:
                break
            if self.kerros < tavoite_kerros:
                self.kerros_ylos()
                
            else:
                self.kerros_alas()
            
    def kerros_ylos(self):
            self.kerros+=1
            print('tämänhetkinen kerros on', self.kerros)

    def kerros_alas(self):
            self.kerros-=1
            print('tämänhetkinen kerros on', self.kerros)
          
class Talo:
    def __init__(self,ylin_kerros, alin_kerros, hissien_maara):
        self.alin_kerros=alin_kerros
        self.ylin_kerros=ylin_kerros
        self.hissien_maara=hissien_maara
        self.hissilista=[]
        self.hissinumero=0
        for i in range (0,self.hissien_maara):
            self.hissi_lisaa()

    def hissi_lisaa(self):
        self.hissinumero+=1
        hissi=Hissi(self.ylin_kerros,self.alin_kerros)
        self.hissilista.append(hissi)
        print('hissi lisätty',self.hissinumero)

    def aja_hissia(self,hissinumero,kohde_kerros):
        print('hissi: ',hissinumero)
        hissi=self.hissilista[hissinumero-1]
        hissi.siirry_kerrokseen(kohde_kerros)
        print('---------------------------')

    def palohalytys(self): 
        print('PALOHÄLYTYS, kaikki alas ')
        for hissi in self.hissilista:
             print('---------------------------')
             hissi.siirry_kerrokseen(self.alin_kerros)
       
        
    
        

kotitalo=Talo(5,1,3)



        
kotitalo.aja_hissia(3,5)
kotitalo.aja_hissia(1,4)
kotitalo.aja_hissia(2,5)
kotitalo.palohalytys()


