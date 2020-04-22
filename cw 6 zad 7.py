import numpy as np
def macierz(n):
    macierz=[]
    for i in range(n):
        macierz.append(2)            
    obiekt = np.diag(macierz) 
    for a in range(0,n):
        for b in range(0,n):
            for c in range(1,n+1):
                if(a==b+c or b==a+c):  
                    obiekt[a,b]=2*(c+1)    
    return obiekt 
print(macierz(4))
print(macierz(5))     