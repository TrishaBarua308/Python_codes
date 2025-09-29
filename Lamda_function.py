# anonymous function
# unnamed function
# no print, only return
# compress function

def square(a):
    return a**2

print(square(5))

squ = lambda x : x**2
print(squ(3))

add = lambda a,b : a+b
print(add(12,23))

student = [('t',98),('f',100),('m',97)]
sort_students= sorted(student,key=lambda x:x[1])  # sorted(apply in which, sort basis on x, s[1] means 1st columns
print(sort_students)

student = [(98, 't'),(100,'f'),(97, 'm')]
sort_students= sorted(student,key=lambda x:x[0])  # sorted(apply in which, sort basis on x, s[1] means 1st columns
print(sort_students)

# MAP
nums = [1,2,3,4,5]
now = list(map(float, nums))
print(now)
next = list(map(str, nums))
print(next)
sq_nums=map(lambda x:x**2, nums) # map(what will do, where it will do)
print(sq_nums)
sq_nums_l = list(map(lambda x:x**2, nums))
print(sq_nums_l)

# FILTER
e= list(map(lambda x: x%2==0, nums)) # gives binary value
print(e)
even = list(filter(lambda x: x%2==0, nums))
print(even)

# reduce
import functools
sum = functools.reduce(lambda x,y:x+y, nums)
print(sum)