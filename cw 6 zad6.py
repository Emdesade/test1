import numpy as np
words = ['pies','kot','olsztyn','samochod','pole','orkiestra']
s =[[],[],[],[],[],[]]
for i in range(0,6,1):
    s[i] = np.array(list(words[i]))
    s[i] = np.fromiter(words[i], dtype='U1')
    print(s[i])
