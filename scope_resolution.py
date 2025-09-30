# scope --> region/area where a variable can access
'''x='global'

def fun():
    x='local'
    print(x)

fun()
print(x)
'''

# LEGB
# l=local
# e=enclosing
# g=global
# b=build in --sum, print,input,max

n="global"

def outer():
    n="enclosing"
    def inner():
        n="Local"
        print(n) # inner func scope, local
    inner()# local
    print(n) # outer function scope, enclosing
outer() # enclosing
print(n) # global func scope

print('\n')
# local convert to global use global

p = "globally"
def out():
    p="enclosingly"
    def inn():
        '''global p
        p ="locally" '''# global convert local to global,  but cannot change enclose
        nonlocal p
        p= "locally" # convert enclose to local
        print(p)
    inn()
    print(p)
out()
print(p)