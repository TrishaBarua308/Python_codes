import random

res = random.randint(1,100)
count=0
print("Welcome to the Number Guessing Game!!!")
print("Try to guess the number between 1 and 100")
while True:
    try:
        n = int(input("\nInput your guess: "))
        count += 1

        if n < res:
            print("Too low!!")
        elif n > res:
            print("Too high!!")

        elif n == res:
            print(f"\nCongratulations! You've guessed the number in {count} attempts.")
            break


    except ValueError:
        print("Invalid input. Enter input between 1 to 100.")

    except Exception as e:
        print(f"Error occurred. {e}")
        continue


