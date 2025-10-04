class Grandfather:
    def __init__(self, color, f_name):
        self.color = color
        self.f_name = f_name

class Father(Grandfather):  # indicate single inherit
    def __init__(self,hobby, color,f_name):
        super().__init__(color, f_name)
        self.hobby=hobby


#g=Grandfather()
f=Father('cricket','blue','barua')
print(f"{f.hobby}\n{f.color}\n{f.f_name}")
