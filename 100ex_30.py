"""define a function that can accpet an integer number as input and print the "It is an even number" if the number is even, otherwise print
"It is an odd number" """

def even_or_odd(i):
    if(i%2==0):
        print i,": It is an even number"
    else:
        print i,": It is an odd number"

even_or_odd(22)
even_or_odd(21)
even_or_odd(20)

