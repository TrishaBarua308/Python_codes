class School:
    school_name= 'Northern University Bangladesh' # class variable

    def __init__(self,stu_name):
        self.stu_name = stu_name      # instance variable




s1 = School('Trisha')
print(s1.school_name)
print(s1.stu_name )
print('\n')


s2=School('Mitu')
s2.school_name="NUB"
print(s2.school_name)
print(s2.stu_name)
print('\n')



s5=School('mitu barua')
print(s5.school_name)
print(s5.stu_name)
print('\n')




s3= School('Barua')
School.school_name="Override school name"
print(s3.school_name)
print(s3.stu_name)
print('\n')


s4= School("Trisha Barua")
print(s4.school_name)
print(s4.stu_name)