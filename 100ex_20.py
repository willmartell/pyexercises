class PowTwo:
    """Class to implement an iterator
    of powers of two"""

    def __init__(self, max = 0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def next(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration




class MyClass:

    def __init__(self,max=0):
        self.n = 0
        self.max = max
        self.numbers = range(self.n,self.max)

    def __iter__(self):
        return self

    def next(self):
        return (n for n in self.numbers if n % 7 == 0)





a = PowTwo(4)
i = iter(a)

for x in i:
    print x

m = MyClass(10)
print next(m)
print a
