#Zad 1
plik = open("zad1.txt","w+")
lista = []
for i in range(20):
   if i%4==0:
       lista+=[i]
plik.write(str(lista))
plik.close()
#Zad 2
plik = open("zad1.txt","r")
wiersze = plik.readlines()
print(wiersze)
print("\n")
#Zad 3
with open("zad1.txt", "w") as plik:
    for a in range(10):
        plik.write("cokolwiek\n")
with open("zad1.txt", "r") as plik:
    for linia in plik:
        print(linia, end="")