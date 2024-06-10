def add(a,b):
    return a + b
  
def subtract(a, b):
    return a - b
  
def multiply(a, b):
    return a * b
  
def divide(a, b):
    if divide == 0:
        print("Cannot divide by 0")
    else:
        return a / b

welcome = print("Welcome to Nehans Four Function Calculator")
choose_function = int(input("1 for add, 2 for subtract, 3 for multiply, 4 for divide "))
a = float(input("Enter First number: "))
b = float(input("Enter Second number: "))

if choose_function == 1:
    print("Result", add(a,b))
elif choose_function == 2:
    print("Result", subtract(a,b))
elif choose_function == 3:
    print("Result", multiply(a,b))
elif choose_function == 4:
    print("Return", subtract(a,b))
else:
    print("Invalid choice")
