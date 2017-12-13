
def createdict(n):
    d = {}
    for i in range(1,n+1):
        d[i] = i*i
    return d


x = createdict(8)
print type(x)
print x

