m = int(input("Input your marks : "))
if 80<=m<100 :
    print("A+")
elif 70<=m<80:  # or , take 70 also a+,so use and
    print("A")
elif 60<=m<70:
    print("A-")

i=1
while i<=10:
    if i==5:
        break
    print(i,". Trisha")
    i= i+1

print("Stop")