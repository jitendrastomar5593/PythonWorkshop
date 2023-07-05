# Classes & Objects

# creating a bike class (blueprint)
class Bike:
    name    = ""
    gear    = 0
    engine  = ""
    cc      = 0


# creating object of bike class
mybike = Bike()

# assigning values & accessing attributes
mybike.name = "Royal Enfield"
mybike.gear = 5
mybike.engine = "twin-cylinder"
mybike.cc = 350

print ("My bike name: ",mybike.name)
print ("Gears total : ",mybike.gear)
print ("Engine type : ",mybike.engine)
print ("CC          : ",mybike.cc)
print ("\n")

##################################################
#                Another example                 #
##################################################

mybike.name = "Keeway Benda"
mybike.gear = 5
mybike.engine = "4-Cylinder"
mybike.cc = 700

print ("My bike name: ",mybike.name)
print ("Gears total : ",mybike.gear)
print ("Engine type : ",mybike.engine)
print ("CC          : ",mybike.cc)


##################################################
#                Using functions                 #
##################################################

class room:
    length  = 0.0
    breadth = 0.0

    # area calculate:
    def room_area(self):
        print ("Area =",(self.length * self.breadth), "sqft.")

# creating object for room class
myroom = room()

# assigning values
myroom.length  = 30
myroom.breadth = 35

# calling function
myroom.room_area()


