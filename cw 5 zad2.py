class Kwadrat():

    def __init__(self,x):
        self.x = x
        self.y = x
    def __add__(self,kwadrat):
        return Kwadrat(self.x + kwadrat.x)
    def __str__(self):
        return 'Kwadrat o boku {}'.format(self.x)

kw = Kwadrat(5)
print(kw) 
kw2 = Kwadrat(7)
print(kw2)
kw3 = kw + kw2
print(kw3)
