def diviso():
	l = []
	for i in range(2000,3201):
		if (i%7==0) and (not (i%5==0)):
			l.append(i)

	print ','.join([str(l)])

diviso()
