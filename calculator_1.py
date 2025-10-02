def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    try:
        return a / b
    except Exception as e:
        return {f"Error occurred. {e}"}


def modulus(a, b):
    try:
        return a % b
    except Exception as e:
        return {f"Error occurred. {e}"}


while True:
    print('\nSelect Operation: ')
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")

    try:
        n = int(input('Enter choice(1/2/3/4/5): '))
        if n not in [1, 2, 3, 4, 5]:
            print("Invalid choice\n")
        else:
            num1 = float(input('\nInput first number : '))
            num2 = float(input('Input second number : '))

            if n == 1:
                print(f"\nAddition : {num1} + {num2} = ", add(num1, num2))
            elif n == 2:
                print(f"\nSubtraction : {num1} - {num2} = ", subtract(num1, num2))
            elif n == 3:
                print(f"\nMultiplication : {num1} x {num2} = ", multiply(num1, num2))
            elif n == 4:
                print(f"\nDivision : {num1} + {num2} = ", divide(num1, num2))
            elif n == 5:
                print(f"\nModulus : {num1} % {num2} = ", modulus(num1, num2))
            else:
                print("\nInvalid choice. Try again later\n")

    except Exception as e:
        print("Error occurred, ",e)



    choice = input("\nDo you want to continue this process? (Y/N):  ")
    if choice == 'y' or choice == 'Y':
        continue
    else:
        print("\nThanks for visiting our site\n")
        break

