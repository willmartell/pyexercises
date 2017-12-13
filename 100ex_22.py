#write a program to compute the frequency fo the words from the input
#the output should output after sorting the key alphanumberically

text="New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."
text = text.rstrip("\n")
print text 


unique = []

for word in text.split(" "):
    if(word not in unique):
        unique.append(word) 

print "after"
for u in sorted(unique):
    c = 0
    for w in sorted(text.split(" ")):
        if(u == w):
            c = c + 1
    
    print u+':'+str(c)


