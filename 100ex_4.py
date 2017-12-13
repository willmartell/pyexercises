
def getInput():
	prompt = "enter a sequence of comma-seperated numbers: "
	x = input(prompt)
	print type(x), x
	y = list(x[:])
	print type(y), y

getInput()

