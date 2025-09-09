#PS 1st basic calculator

running = True

while running:
    number1 = int(input("Enter your first number").strip())
    number2 = int(input("Enter your second number").strip())
    operation = input("Which operator would you like to use?(Hint: write the first three letters of the operations name): ").strip()

    if operation == "add":
        number3 = number1 + number2
        print(f"{number1} + {number2} = {number3:2f}")
    elif operation == "sub":
        number3 = number1 - number2
        print(f"{number1} - {number2} = {number3:2f}")
    elif operation == "mul":
        number3 = number1 * number2
        print(f"{number1} x {number2} = {number3:2f}")
    elif operation == "div":
        number3 = number1 / number2
        print(f"{number1} / {number2} = {number3:2f}")
    elif operation == "mod":
        number3 = number1 % number2
        print(f"{number1} % {number2} = {number3:2f}")
    elif operation == "exp":
        number3 = number1 ** number2
        print(f"{number1}^{number2} = {number3:2f}")
    elif operation == "flo":
        number3 = number1 // number2
        print(f"{number1} // {number2} = {number3:2f}")
    
    stop = input("Do you want to terminate the program")
    
    if stop = "yes":
        running = False
