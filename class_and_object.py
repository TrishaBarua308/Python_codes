# create class named animal

class Animal: # class name always title wise , 1st upper case
    def __init__(self): # self indicate obj of the animal class
        name=""
        food=""

a1 = Animal()
a1.name="Panda"
a1.food="bamboo"

print(a1.name, a1.food)

a2 = Animal()
a2.name="Cat"
a2.food="Milk"
print(a2.name, a2.food)