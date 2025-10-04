class Employee:
    company_name = 'ostad company'

    def __init__(self,name,salary):
        self.name = name
        self._salary=salary


    # @property
    # def get_salary(self):  # it works like variable, we can change it
    #     return self.salary


    @property  # declaring with same name as variable,, it convert it into read only mood, we cannot
    def salary(self):         # change it after declaring
        return self._salary

    @salary.setter
    def salary(self,new_salary):
        self._salary = new_salary


e = Employee('Trisha',20000)
print(e.name)
print(e.salary)

# e.salary = 30000
# print("after change :")
# print(e.name)
# print(e.salary)
# not working -- def salary func
# to solve it use set salary--salary.setter


e.salary = 30000
print("after change :")
print(e.name)
print(e.salary)
