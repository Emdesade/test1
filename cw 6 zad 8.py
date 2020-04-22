import numpy as np
def ruch_tablicy(tab,kierunek):
    if kierunek == 1:
        if len(tab)%2==0:
            print(tab[:len(tab)//2])
            print(tab[2:len(tab)])
    if kierunek == 2:
        if len(tab[0])%2==0:
            pionowa = np.array([[x[0:len(tab) // 2] for x in tab], [x[len(tab) // 2: len(tab)] for x in tab]])
            print(pionowa[0],"\n", pionowa[1])
a = np.array([[1,2,3,4],[5,6,7,8],[1,2,3,4],[5,6,7,8]])
print(ruch_tablicy(a,2))