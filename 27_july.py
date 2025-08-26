def sumArray(numbers):
    total=0
    for i in numbers:
        total += i
    return total

def main():
    size =5
    numbers = []
    print(f"Input {size} numbers ")

    for i in range(size):
        n = int(input())
        numbers.append(n)

    ans = sumArray(numbers)
    print("Sum = ",ans)

main()