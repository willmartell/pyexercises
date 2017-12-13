import math

l = []
c = 50
h = 30
input_sequence = 100,150,180

for d in input_sequence:
	q = math.sqrt( (2*c*d)/h )
	l.append(int(round(q)))

print l
