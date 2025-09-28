# key value pair
# no indexing
# key immutable

a = {1:"apple",2:"ball",3:"cat"}
print(a)  

for i in a:
    print(i)  #only print key value

for i in a.values():
    print(i)  # print value 2nd


print(a.keys(), a.values())

for i,j in a.items():
    print(f"key = {i} and value = {j}")


c = [2,3,4,5]
d = ['trisha', 'barua', 'mitu', 'cse']
t = dict(zip(c,d))
print(t)

print(t[5])  # search by key


f = dict(zip(d,c))

print(f['cse'])



