class Robaczek:
    
    def __init__(self,x,y,krok):
        self.x = x
        self.y = y
        self.krok = krok
    def idz_w_gore(self, krok):
        self.x += krok
    def idz_w_dol(self, krok):
        self.x -= krok
    def idz_w_lewo(self, krok):
        self.y -= krok
    def idz_w_prawo(self, krok):
        self.y += krok         
    def pokaz_gdzie_jestes(self):
        return (self.x,self.y)

obiekt = Robaczek(1,1,1)
obiekt.idz_w_dol(1)
obiekt.idz_w_gore(2)
obiekt.idz_w_prawo(3)
obiekt.idz_w_lewo(4)
print(obiekt.pokaz_gdzie_jestes())    