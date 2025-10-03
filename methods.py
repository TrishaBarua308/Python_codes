class Student:
    def __init__(self,name,id):  # dunder method / double underscore= dunder
        self.name=name
        self.id=id

    def display_info(self):
        print(f"\nName = {self.name}\nID: {self.id}\n")



s1 =Student('Trisha', 1016)
s1.display_info()

s2 =Student("Mitu",16)
s2.display_info()

