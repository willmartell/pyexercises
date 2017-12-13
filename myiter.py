class MyIter:
    def __init__(self,max=0):
#        print "going up to value:",max
        self.n = 0
        self.max = max

    def __iter__(self):
#        print "iter method called"
        return self

    def next(self):
#        print "next method called"
        if(self.n <= self.max):
            x = self.n
            self.n += 1
            if(x%7==0):
                return x
        else:
            raise StopIteration

x = 100
m = MyIter(x)

try:
    for i in range(0,x):
        a = next(m)
        if(a is not None):
            print a
    print 
    print 
except any as error:
    print "crap:",error


class Fib:
     def __init__(self):
         self.a, self.b = 0, 1
     def __iter__(self):
         while True:
             yield self.a
             self.a, self.b = self.b, self.a+self.b
a = Fib()
print type(a)
f = iter(a)
print type(f)
for i in range(30):
    print(next(f))

