class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

    def repr(self):
        print((self.r, self.i))


complex_number = Complex(3.0, -4.5)
print('complex_number =', (complex_number.r, complex_number.i))
complex_number.repr()
