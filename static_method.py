class School:
    school_name ='ABC school'

    @staticmethod               # call by class name
    def calculate_gpa(marks):   # static= no need self/cls to call, use as helper, organizer
        if marks >=80:
            return 'A+'
        else:
            return 'Fail'



print(School.school_name)
print(School.calculate_gpa(90))
print(School.calculate_gpa(67))

