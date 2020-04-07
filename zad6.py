class Slowa:

    def __init__(self,slowo1,slowo2):
        self.slowo1 = slowo1
        self.slowo2 = slowo2
    def sprawdz_czy_palindrom(self):
        rev = ''.join(reversed(self.slowo1))
        if (self.slowo1 == rev):
            return True
        return False
    def sprawdz_czy_metagramy(self):
        a = self.slowo1
        b = self.slowo2
        a_1 = len(a)
        b_1 = len(b)
        test = 0
        liczenie = 0
        if(a_1 == b_1):
            for n in a:
                if (a[test] == b[test]):
                    liczenie += 1
                else:
                    pass
                test += 1
        else:
            return "Nie metagramy"
        if(liczenie == a_1-1):
            return "Metagramy"
        else:
            return "Nie metagramy"
    def sprawdz_czy_anagramy(self):
        a = self.slowo1
        b = self.slowo2
        c = []
        d = []
        for m in a:
            if(m in a and m not in c):
                c.append(m)
        for m in b:
            if(m in b and m not in d):
                d.append(m)
        c.sort()
        d.sort()
        if c == d:
            return "Anagramy"
        else:
            return "Nie Anagramy"
    def wyswietl_wyrazy(self):
        return self.slowo1,self.slowo2 
obiekt = Slowa("kajak","kajek")
ans = (obiekt.sprawdz_czy_palindrom())
if ans ==1:
    print("tak to palindrom")
else:
    print("nie to nie palindrom")    
print(obiekt.sprawdz_czy_metagramy())
print(obiekt.sprawdz_czy_anagramy())
print(obiekt.wyswietl_wyrazy())