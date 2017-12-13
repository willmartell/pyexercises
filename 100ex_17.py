import re
class Account:
    balance = 0.0

    def withdrawal(self,n):
        self.balance = self.balance - float(n)

    def deposit(self,n):
        self.balance = self.balance + float(n)

    def print_balance(self):
        print "%.2f" % self.balance


f_in = open("bank.log","r")
lines = (line.rstrip() for line in f_in) # All lines including the blank ones
lines = (line for line in lines if line) # Non-blank lines

a = Account()

print "before reading bank.log"
a.print_balance()

for l in lines:

    words = l.split(" ")

    action = words[0]
    amount = words[1]
    if( action == "D" ):
            a.deposit(amount)
    else:
        if( action == "W" ):
            a.withdrawal(amount)

print "after reading bank.log"
a.print_balance()

