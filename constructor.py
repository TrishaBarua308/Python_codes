class Student:
    def __init__(self):  # default constructor
        self.name=""
        self.id=""

    def __init__(self,name,id):  # parameterized constructor
        self.name=name
        self.id=id

    def __init__(self,name="Trisha", id=1016):     # default parameter constructor
        self.name=name
        self.id=id


s1=Student()  # call default value constructor
print(s1.name, s1.id)

s2=Student("Mitu",16) # call parameterized constructor
print(s2.name, s2.id)