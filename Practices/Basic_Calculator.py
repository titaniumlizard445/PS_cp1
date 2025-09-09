#PS 1st basic calculator

running = True

while running:
    number1 = int(input("Enter your first number"))
    number2 = int(input("Enter your second number"))
    operation = input("Which operator would you like to use?(Hint: write the first two letters of the operations name): ")

    if operation == "ad":
        number3 = number1 + number2
    

    print(number3)