class Ciag:

    def __init__(self,a1,r,an,n):
        self.a1 = a1
        self.r = r
        self.an = an
        self.n = n
    def wyswietl_dane(self):
        print(self.a1,self.r,self.an,self.n)
    def pobierz_elementy(self):
        wartosci_ciagu = int(input("Podaj wartosci ciągu "))
    def pobierz_parametry(self):
        pierwsza_wartosc = int(input("Podaj  1 wartosc ciagu ")) 
        roznica = int(input("Podaj roznice ciagu ")) 
        ilosc_elementow = int(input("Podaj ilosc elementow "))
    def policz_sume(self):
        suma = (self.a1+self.an)/2 *self.n 
        return suma
    def policz_elementy(self):
        self.ciag = []
        while len(self.ciag) != int(self.n):
            self.ciag.append(self.a1)
            self.a1 += self.r
        return self.ciag
    def __del__(self):
        print("Del")
            
obiekt = Ciag(a1=2,r=3,an=5,n=10)
print(obiekt.pobierz_elementy())
print(obiekt.pobierz_parametry())
print(obiekt.policz_sume())
print(obiekt.policz_elementy())
del obiekt