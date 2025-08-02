def calculator():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter seconnd number: "))
        op = input("Enter an operation (+, -, *, /): ")

        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            result = num1 / num2
        else:
            print("invalid operation")
            return
        print(f"The result is: {result}")

    except ValueError:
        print("please enter a valid number!")
    except ZeroDivisionError:
        print("you cannot divide by zero!")
    finally:
        print("Thanks for using the calculator!")

calculator()
#loop until the user choose to quit.
while True:
    calculator()
    again = input("do another calculation? (yes/no): ")
    if again.lower()!= 'yes':
        break



