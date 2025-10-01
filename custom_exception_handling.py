def check_file(file_name):
    if not file_name.endswith('.txt'):
        raise ValueError("Only txt files are allowed")
    print("Valid file")

try:
    check_file('name.txt')
except Exception as e:
    print(e)