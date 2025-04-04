'''subjects = ["c", "c++","algo","dbms","python","toc"]
print(len(subjects))
subjects.append("os")
print(subjects)
subjects.insert(2,"dept")
print(subjects)
subjects.remove("algo")
print(subjects)
subjects.sort()
print(subjects)
subjects.reverse()
print(subjects)
subjects.pop()
subjects.pop()
print(subjects)

#subjects.clear()
#print(subjects)

sub2 = subjects.copy()
print(sub2)
p = sub2.index("os")    #count from 0 index, os = 2 index
print(p)
print(sub2 + ["os","os","toc",'toc'])
m = sub2.count("toc")
print(m)'''

subjects = ["c", "c++","algo","dbms","python","toc","os","os","os","toc"]
m = subjects.count("toc")
print(m)