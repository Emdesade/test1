class Parzyste:
    def __init__(self,data):
        self.data = data
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index>=len(self.data):
            raise StopIteration
        if self.index %2 == 0:
            value = self.data[self.index]
            self.index += 2
            print(value)
obiekt = Parzyste([1,2,3,4])
for element in obiekt:
    element
