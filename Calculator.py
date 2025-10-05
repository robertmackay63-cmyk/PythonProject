from operator import truediv


def multiplication(num1, num2):
    return num1 * num2


def addition(num1, num2):
    return num1 + num2


def subtraction(num1, num2):
    return num1 - num2


def divide(num1, num2):
    return num1 / num2

Finished = False
while not Finished:
    while True:
        try:
            value1 = int(input("Enter 1st number: "))
            break
        except ValueError:
            print('Try Again')
    while True:
        try:
            value2 = int(input("Enter 2nd number: "))
            break
        except ValueError:
            print('Try again')

    print("Select operation 1-Division, 2-Multiplication, 3-Addition, 4-Subtraction, 5-Exit")
    while True:
        try:
            operation = int(input("Choose operation 1/2/3/4/5: "))
            if operation <1 or operation>5:
                raise ValueError ('Not in range 1-5')
            break
        except ValueError:
            print("Invalid input. Try again.")
    if operation == 1:
        try:
            print(value1, "/", value2, "=", divide(value1, value2))
        except ZeroDivisionError:
            print("Can't divide by zero")
    elif operation == 2:
        print(value1, "*", value2, "=", multiplication(value1, value2))
    elif operation == 3:
        print(value1, "+", value2, "=", addition(value1, value2))
    elif operation == 4:
        print(value1, "-", value2, "=", subtraction(value1, value2))
    else:
        print("BYE")
        Finished = True
