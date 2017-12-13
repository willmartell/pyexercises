"""define a function that can accept two strings as input and print the string with the maximum length in console.  if two strings have the
same length then the function should print all strings line by line"""

def check_str_len(s1,s2):
    l1 = len(s1)
    l2 = len(s2)
    if(l1 == l2):
        print s1
        print s2
    if(l1>l2):
        print "string one is longer:",l1,"characters"
    else:
        print "string two is longer:",l2,"characters"

string1 = "There is currently a plane flying over Germany drawing a xmas tree (flightradar24.com)"
string2 = "Some go to car production hell. I went to production production heaven (dailykanban.com)"

check_str_len(string1,string2)

