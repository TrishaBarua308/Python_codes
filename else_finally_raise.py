'''try:
    with open('name.txt','r') as f:
        print(f.read())
    a=ftp # value error
    a=[1,2,3]
    print(a[9]) # out of range
    print(10/0) # divided by 0

except Exception as e:
    print(e)

else:
    print("code executed successfully") # else works when file

finally:
    print("always run , if code have error or not")'''


# create manual exception/ trigger
def file_check(file_name):
    if not file_name.endswith('.txt'):
        raise ValueError("Only txt file are allowed")
    print("Valid file")

file_check('name.csv')