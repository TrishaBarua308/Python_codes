'''num = ['a','b','c','d','e','f','g']

x = 1
for x in num :
    print(x, end=" ")
'''
#1+2+3+.......+n
n = int(input("Input n = "))

sum=0
for i in range (1, n+1, 1) :  # start =1,  < n+1,  difference =1
    print(i,end=" ")
    sum = sum + i

print('\n')
print("sum = ", sum)


# 1^2 + 2^2 + _---------+n^2
s=0

for i in range ( 1, n+1, 1):
    s = s+ i*i

print(s)
