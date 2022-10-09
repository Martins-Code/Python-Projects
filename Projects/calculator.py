def add(a, b):
    answer = a + b
    print()
    print(f'{str(a)} + {str(b)} = {answer}')


def sub(a, b):
    answer = a - b
    print()
    print(f'{str(a)} - {str(b)} = {answer}')


def mul(a, b):
    answer = a * b
    print()
    print(f'{str(a)} * {str(b)} = {answer}')


def div(a, b):
    answer = a / b
    print()
    print(f'{str(a)} / {str(b)} = {answer}')


while True:
    print()
    print("A: Addition")
    print("B: Subtraction")
    print("C: Multiplication")
    print("D: Division")
    print("E: Exit")

    choice = input("Select Operation: ")

    if choice.lower() == "a":
        print("Addition")
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        add(a, b)
    elif choice.lower() == "b":
        print("Subtraction")
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        sub(a, b)
    elif choice.lower() == "c":
        print("Multiplication")
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        mul(a, b)
    elif choice.lower() == "d":
        print("Division")
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        div(a, b)
    elif choice.lower() == "e":
        print("Exit")
        quit()
    else:
        print()
        print("Invalid Choice, please select A, B, C or D")