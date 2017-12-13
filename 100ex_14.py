import re

input = raw_input("enter upper case and lower case words, press enter when done.\n")

letters = re.findall('[a-zA-Z]',input)
cnt_upper = 0
cnt_lower = 0

for l in letters:
    if ( l.isupper() ):
        cnt_upper += 1
    else:
        cnt_lower += 1


print "UPPER CASE: ",cnt_upper
print "LOWER CASE: ",cnt_lower




