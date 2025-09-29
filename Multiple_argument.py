'''def add(a,b):
    r = sum(a,b) # sum only accept list / tuple
    return r

print(add(10,20))'''

def add(*pipip):
    print(pipip)
    return sum(pipip)

print(add(1,2,4))

another = add(9,8,7,6,5,4,3.6,2,1)
print(another)