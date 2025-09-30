'''Error = compiler time ---syntax, indentation,
exceptoin = runtime ---- divide by 0, indexing,key, value Error'''

try:
    with open('file_nei.txt','r') as f:
        print(f.read())
except Exception as e:
    print(e)

'''except FileNotFoundError:
    print("not found")''' # ostad