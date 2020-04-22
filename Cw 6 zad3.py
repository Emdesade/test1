import numpy as np
def tablica(n):
    result = np.zeros((n, n))
    result = np.array([n,n*n])
    return result
print(tablica(1))
print(tablica(2))
print(tablica(3))
print(tablica(4))
print(tablica(5))