class Employee:
    company_name = 'Ostad limited'

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def display_info(self):    # instance method
        print(f"\nEmp. Name = {self.name}\nEmp. Salary = {self.salary}")

    @classmethod    # decorator== officially defines -- class method
    def change_company_name(cls,name):  # cls indicate---its own class
        cls.company_name=name


    #class method = change all occurrence
    #instance method = change only the selected part


a = Employee("Trisha",20)
a.display_info()
print(a.company_name)

b = Employee("Mitu",30)
b.display_info()
#b.change_company_name('ABC company')  # by calling obj, its a bad habit, cause change_company_method is a class method
Employee.change_company_name('ABC company')  # good habit to call this method by classname
print(b.company_name)

c = Employee("piku",20)
c.display_info()
print(c.company_name)