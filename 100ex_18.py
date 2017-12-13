import re 

class word:
    lower = 0
    upper = 0
    digit = 0
    punct = 0
    name = ''
    length_ok = 0

    def __init__(self,s):
        self.name = s
        print "creating word object named ",self.name
        #print self.lower print self.upper print self.digit print self.punct 
        
    def check_lower(self):
        chars = list(self.name)
        for c in chars:
            if(self.lower == 1):
               continue 
            #print "checking lower:",c,
            if(re.search('[a-z]',c)):
                #print "turning self.lower on"
                self.lower = 1
            else:
                #print "nope"
                self.lower = 0


    def check_upper(self):
        chars = list(self.name)
        for c in chars:
            if (self.upper == 1): 
                return
            #print "checking upper:",c,
            if (re.search('[A-Z]',c)):
                #print "turning self.upper on"
                self.upper = 1
            else:
                #print "nope"
                self.upper = 0


    def check_digit(self):
        chars = list(self.name)
        for c in chars:
            if( self.digit == 1 ):
                return
            if (re.search('[0-9]',c) ):
                self.digit = 1
            else:
                self.digit = 0


    def check_punct(self):
        chars = list(self.name)
        for c in chars:
            if(self.punct == 1):
                return
            if (re.search('[$#@]',c)):
                self.punct = 1
            else:
                self.punct = 0

    def check_length(self):
        chars = list(self.name)
        if(len(chars) >=6 and len(chars) <= 12):
            self.length_ok = 1
        else:
            self.length_ok = 0


    def word_passes_checks(self):
        self.check_lower()
        self.check_upper()
        self.check_digit()
        self.check_punct()
        self.check_length()

        if ( self.lower == 1 and self.upper == 1 and self.digit == 1 and self.punct == 1 and self.length_ok == 1 ):
            return 1
        else:
            return 0




s = 'ABd1234@1,a F1#,2w3E*,2We3345'
#s = 'hello,WORLD,Robot1$'
print "input string: ",s

input_string = s.split(',')
words = []

print "checking which words satisfy the password requirements."
for chunk in input_string:
    w = word(str(chunk)) #create word object with name as chunk
    if( w.word_passes_checks() ):
        words.append(w.name)

print "words that pass the requirements are:"
print words



