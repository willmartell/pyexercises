l = []
def is_divisible(i):
    """
    check each digit of the number is evenly divisible by 2
    ex. integer number 10 check character 1 % 2 == 0 and check character 0 % 2 == 0
    if so, then return 1 meaning yes
    """
    s = str(i).split() #list of chars
    for x in s:
        if ( int(x) % 2 != 0 ): #number is not divisible by 2
            return 0
    return 1

for i in range(1000,3001):
    if( is_divisible(i) ):
        l.append(i)

print l


