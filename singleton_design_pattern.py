# singleton
class Singleton:
    _variable = None  # class variable create

    def __new__(cls):   # to access class variable, while creating obj, new method will call
        if cls._variable is None:
            print("1st time created")
            cls._variable = super(Singleton, cls).__new__(cls)
        return cls._variable

t = Singleton() # 1st time obj created
p = Singleton() # 2nd time it will return the previous value

print(t==p)

