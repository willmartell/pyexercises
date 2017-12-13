
def makearray(x,y):
    a = []
    #y is columns
    for i in range(0,x):
        b = []
        for j in range(0,y):
            b.append(i*j)
        a.append(b)
    return a

print makearray(3,5)            
