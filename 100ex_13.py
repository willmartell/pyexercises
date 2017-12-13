import re

input = raw_input("enter sentences of words and digits.: ")

l = re.findall('[a-zA-Z]',input)
d = re.findall('[0-9]',input)

print 'LETTERS:', len(l)
print 'DIGITS:',  len(d)

