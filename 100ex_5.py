
class MyClass:

	def getString(self):
		self.s = raw_input('>')	
	
	def printString(self):
		print self.s.upper()


i = MyClass()
i.getString()
i.printString()

print ':' + i.s + ':'

