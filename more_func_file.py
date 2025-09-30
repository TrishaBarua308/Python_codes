import os

if os.path.exists("name.txt"):
    print("file exists")
else:
    print("does no exists")


print("\nanother way\n")


import pathlib

file_path = pathlib.Path('name.txt')
if file_path.exists():
    print('yes exists')
else:
    print("no")


# path file location show
print(os.path.abspath('name.txt'))

print(os.path.getsize('name.txt')) # get size in bytes = 106 bytes

with open('name.txt') as f:
    print(f.read(6))