subjects = ["c++", "c", "DBMS","OS","toc"]
print(subjects)
print(subjects[0])
print(subjects[3])
print(subjects[2:]) # index=2 to last index
print(subjects[-1]) # reverse

print(subjects + ["CD","OOP"])
print(subjects * 2) # all items 2 times

print("python" in subjects) # ans in bool, check python exists in list or not, output=false
print("python" not in subjects)

print(subjects + ["DEPT", 1016])