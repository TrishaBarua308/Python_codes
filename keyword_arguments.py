def info(f_name, l_name, age):
    print(f"I am {f_name} {l_name}. I am {age} years old.")

info("trisha","barua",23)
info(25,"tri","mitu")

info(l_name="Barua",f_name='Trisha',age=23)

print("\n")
print("------------------------------------------")

# if more & more arguments
# keyword argument works like a dictionary
def information(**keyarg):
    print(keyarg)
    print(f"\nHello!! I am {keyarg['f_n']} {keyarg['ln']}. My ID no is {keyarg['id']} & I am from {keyarg['dept']} department.")

information(dept="CSE",f_n="Trisha",ln="barua",hei=5.5,  id=1016)