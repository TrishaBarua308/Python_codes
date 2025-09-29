def info(fn,ln):
    print(fn,ln)

info('Trisha', "Barua")
#info('mitu') # 1 argument needed error

def more(f,l="Barua"):# its a default parameter
    print(f,l)

more("Munny") # 2nd arg empty, so use default value
more("Trisha","Mitu") # 2nd not empty, default not use here

def greeting():
    pass # likes a place holder nothing else

greeting()