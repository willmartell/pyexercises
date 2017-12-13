
bins = '0100','0011','1010','1001'

l = []
for b in bins:
    d = int(b,2)
    if(d%5==0):
        l.append(b)
print ','.join(l)
