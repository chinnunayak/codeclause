#This is create empty list for calculator
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x , y):
    return x * y

def divide(x, y):
    if y== 0:
        return "Can't divide by zero"
    return x / y
#Main program
while True:
    print("Options:")
    print("Enter '+' for addition")
    print("Enter '-' for subtraction")
    print("Enter '*' for multipication")
    print("Enter '/' for division")
    print("Enter 'quit' to end the program")

    user_inpt = input(" : ")
    if user_inpt == "quit":
        break

    operation = {
        '+' : add,
        '-' : subtract,
        '*' :multiply,
        '/' :divide
    }

    if user_inpt in operation:
        num1 = float(input("Enter First number:"))
        num2 = float(input("Enter Second number: "))
        result = operation[user_inpt](num1, num2)
        print("Result:", result)
    
    else:
        print("Invalid Input.")