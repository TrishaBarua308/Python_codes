a = int(input("Input a = "))
b = int(input("Input b = "))
c = int(input("Input c = "))

'''if a > b:
    if a > c:
        print("Max = a = ", a)
    else:
        print("Max = c = ", c)
else:
    if b > c:
        print("Max = b = ", b)
    else:
        print("Max = c = ", c)'''

print("max = ",a if a>b else b) #ternary

d = input("Input a alphabet : ")
if d=='a' or d=='e' or d=='i' or d=='o' or d=='u' :
    print("Vowel")
else:
    print("Constant")
