#PS 1st Flexibility Calculator
#vars
running = True
values = []
#create functions for each type of operation
#sum
def addall(*numbers):
    total = 0.0
    for i in numbers:
        for x in i:
            total+=x
    return total

#Average
def Averages(*numbers):
    average = 0.0
    iterations = 0
    for i in numbers:
        for y in i:
            average+=y
            iterations+=1
    average/=iterations
    return average
    
#Max
def Maximum(*numbers):
    max = 0.0
    for i in numbers:
        for z in i:
            if z >= max:
                max = z
    return max

#Min
def Minimum(*numbers):
    min = numbers[0]
    for i in numbers:
        for a in i:
            if a <= min:
                min = a
    return min

#Product
def Multiplyall(*numbers):
    product = 1
    for i in numbers:
        for b in i:
            product *= b
    return product

#introduce user
print(f"Hello and welcome to the multi number calculator! \n")
#loop to keep user going until stopped
while running:
    #display options for operations and input for type of operation
    operation = input(f"Which operation would you like to user for your data set? \n 1)Sum (add all your numbers together) \n 2)Average (Sum then divide by how many numbers there were) \n 3)Max (find the largest number in the data set) \n 4)Min (opposite of Max (finds smallest number)) \n 5)Product (Multiply all numbers together) \n").strip()

    #ask for values that the user wants to user
    print('Please write each of your values after the word "Enter value here: " if you are done entering your values write "done"')
    while "done" not in values:
        user_currently_added_value = input("Enter a value here: ")
        #convert each input to a float if it is not the word done
        if user_currently_added_value != "done":
            user_currently_added_value = float(user_currently_added_value)
            values.append(user_currently_added_value)
        elif user_currently_added_value == "done":
            values.append(user_currently_added_value)
        else:
            print("Please enter a Valid Value")
    values.remove("done")
    #Use calculating function and display answer
    if operation == "1":
        print(f"The Sum of your data set is {str(addall(values))}")
    if operation == "2":
        print(f"The Average of your data set is {str(Averages(values))}")
    if operation == "3":
        print(f"The Maximum value in your data set is {str(Maximum(values))}")
    if operation == "4":
        print(f"The Minimum value in your data set is {str(Minimum(values))}")
    if operation == "5":
        print(f"The Product of your data set is {str(Multiplyall(values))}")
        
    #ask for if program should go again
    done = input("Would you like to use the calculator again? \n y/n ").strip()
    if done.lower() == "n":
        print("Goodbye!")
        running = False
