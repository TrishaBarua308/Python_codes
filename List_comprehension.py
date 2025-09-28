a=[1,10,19,18,17,16,15,14,13,12,11]

for i in a:
    if i%2==0:
        print(i)

a =[i for i in a if i%2==0]
print(a)

b = [1,2,3,4,5,6,7,8,9]

'''for i in range(len(b)):
    if b[i]%2==0:
        b[i]=b[i]**2

print(b)
'''

b_new = [i**2 if i%2==0 else i for i  in b]
print(b_new)