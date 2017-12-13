"""define a function that can receive two integral numbers in string form and compute their sum and then print it in console"""
def sum_two_str(s1,s2):
    return int(s1)+int(s2)

string1 = '11'
string2 = '22'

print "what is sum of string ",string1,"and",string2
print sum_two_str(string1,string2)
