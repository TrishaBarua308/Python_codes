# multiple class relationship
# Association
class Laptop:
    def __init__(self,brand):
        self.brand=brand

class Student:
    def __init__(self,name,Laptop_obj):
        self.name = name
        self.Laptop_v = Laptop_obj

    def show_laptop_info(self):      # calls laptop's brand that's why self.Laptop_v.brand
        print(f"\n{self.name} has a laptop named {self.Laptop_v.brand}\n\n")


lp = Laptop("DELL")
st = Student('Trisha',lp)
st.show_laptop_info()



# Aggregation
class Department:
    def __init__(self,name):
        self.name=name

class University:
    def __init__(self,name):
        self.name = name
        self.departments = [] # create empty list to store dept list

    def add_dept(self,dept):
        self.departments.append(dept)

    def show_dept(self): # dept.name = indicate dept name of dept class
        return [dept.name for dept in self.departments]   # create list comprehension

u = University("NUB")
d1 = Department('CSE')
d2 = Department("Science")
u.add_dept(d1)
u.add_dept(d2)
print(u.show_dept())


# compositon

class Engine:
    def __init__(self,power):
        self.power = power

class Car:
    def __init__(self,brand,power):
        self.brand = brand
        self.engine=Engine(power)  # indicate class obj,like e = Engine(100) here 100 indicate power

    def show_car_info(self):         # self.engine works as obj of Engine class
        print(f"\n{self.brand} has an engine with {self.engine.power} HP.\n")


c = Car('Toyota',200)
c.show_car_info()










