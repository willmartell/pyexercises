# use a list comprehension to square each odd number in a list.  the list of input by a sequnce of comma seperated numbers.
# suppose the following input is supplied to the program:  1,2,3,4,5,6,7,8,9 then the output should be 1,3,5,7,9

t = input("enter a sequence of comma seperated numbers.  I will square the odd numbers.\n")

def is_odd(n):
    if (n % 2 != 0 ):
        return 1
    return 0

l = []
for x in t:
    if ( isinstance(x,int) ):
        n_is_odd = is_odd(x)
        if ( n_is_odd == 1 ):
            l.append(x*x)

print l
