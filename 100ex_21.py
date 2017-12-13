import math

class Point:
    #remember where you started from
    starting_x = 0
    starting_y = 0
    def __init__(self,x=0,y=0):
        print "creating new point object"
        self.x = x
        self.y = y
        starting_x = self.x
        starting_y = self.y
        print "starting at position:",self

    def __str__(self):
        return '%d,%d' % (self.x,self.y)

    def moveUp(self,i):
        was = self.y
        self.y = self.y + int(i)
        print "moving up from",was,"to",self.y

    def moveDown(self,i):
        was = self.y
        self.y = self.y + (int(i) * -1) 
        print "moving down from",was,"to",self.y

    def moveLeft(self,i):
        was = self.x
        self.x = self.x + (int(i) * -1)
        print "moving left from",was,"to",self.x

    def moveRight(self,i):
        was = self.x
        self.x = self.x + int(i)
        print "moving right from",was,"to",self.x

    def findDistanceTaxiCabGeo(self):
        #print int(round(math.sqrt(pos[1]**2+pos[0]**2)))
        return int(round(math.sqrt(self.y**2+self.x**2)))

p= Point()

f = open("journey.txt","r")
for l in f.readlines():
    if(l.isspace()):
        continue
    commands = l.rstrip("\n").split(" ")
    direction = commands[0].strip(" ")
    steps = commands[1].strip(" ")

    print "go",direction,"a total of",steps,"steps"

    if(direction=="LEFT"):
        p.moveLeft(steps)
    if(direction=="RIGHT"):
        p.moveRight(steps)
    if(direction=="UP"):
        p.moveUp(steps)
    if(direction=="DOWN"):
        p.moveDown(steps)

print "ending position is:",p
print "distince in taxicab geometry is",p.findDistanceTaxiCabGeo()
