import itertools

liczby = [1,2,3,4,5,6,7,8,9,10]

wynik = itertools.combinations(liczby,3)

for i in wynik:
    print(i)