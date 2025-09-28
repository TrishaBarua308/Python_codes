# set
# unordered = cannot access value by index
# immutable = cannot update value after decalring
# contain unique value only, no duplicate

a=[1,2,2,3,4,4,4,5]
print("Type of a  ",type(a))
b = set(a)
print(b)
print("Type of b  ",type(b))

t = {1,2,3,4,5,5,6}
f = {3,4,5,5,5,5,5}

p = t.union(f)
print(p)

piii = t.intersection(f)
print(piii)