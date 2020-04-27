import numpy as np
a = np.arange(81).reshape(9,9)
print(a)
print(a.shape)
b = a.reshape(3,27)
print(b)
print(b.shape)
c = b.reshape(27,3)
print(c)
print(c.shape)
d = b.T
print(d)
print(d.shape)
# Odp możemy zmienić kształt gdy iloczyn dwóch liczb naturalnych da 81 