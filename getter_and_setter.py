class Employee:
    def __init__(self,name,salary):
        self.name=name
        self._salary=salary # by convention _salary means its a private/protected variable, but actually its
                            # not logically works , we have to do it manually

    def get_salary(self,password):
        if password=='admin':
            print(f"Salary = {self._salary}\n")
        else:
            print("Sorry, Its a private matter...")


    def set_salary(self,password, salary):
        if password=='admin':
            self._salary=salary
            print(f"New salary = {self._salary}\n")
        else:
            print("Sorry, your approach is not correct.\n")


e1 = Employee('Trisha',30000)
print(f"\nEmployee Name = {e1.name}")
# e1.get_salary(123)  # sorry private matter
#
# e1.get_salary('admin')  # it will show salary

#e1.set_salary(123,40000)
e1.set_salary('admin',40000)