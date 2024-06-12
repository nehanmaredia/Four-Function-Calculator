def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        print("Cannot divide by 0")
        return None
    else:
        return a / b

def calculator():
    try:
        choose_function = int(input("Choose function:\n1 for add\n2 for subtract\n3 for multiply\n4 for divide\n"))
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choose_function == 1:
            print("Result:", add(a, b))
        elif choose_function == 2:
            print("Result:", subtract(a, b))
        elif choose_function == 3:
            print("Result:", multiply(a, b))
        elif choose_function == 4:
            result = divide(a, b)
            if result is not None:
                print("Result:", result)
        else:
            print("Invalid choice")
    except ValueError:
        print("Please enter valid numbers.")
    except Exception as e:
        print(f"An error occurred: {e}")

while True:
    calculator()
    another_calculation = input("Would you like to calculate another number? (yes/no): ").strip().lower()
    if another_calculation != 'yes':
        break

print("Thank you for using Nehan's Four Function Calculator!")
