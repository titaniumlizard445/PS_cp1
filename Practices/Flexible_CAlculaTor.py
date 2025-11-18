#PS 1st Flexibility Calculator
#vars
running = True
values = []
#create functions for each type of operation
#sum
def addall(*numbers):
    total = 0.0
    for x in numbers:
        x += total
    return total

#Average
def Averages(*numbers):
    average = 0.0
    iterations = 0
    for y in numbers:
        y+=average
    average/=iterations
    return average
    
#Max
def Maximum(*numbers):
    max = 0.0
    for z in numbers:
        if z >= max:
            max = z
    return max

#Min
def Minimum(*numbers):
    min = 0.0
    for a in numbers:
        if a <= min:
            min = a
    return min

#Product
def Multiplyall(*numbers):
    product = 1
    for b in numbers:
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
        user_currently_added_value = input("Enter a value here")
        #convert each input to a float if it is not the word done
        if user_currently_added_value != "done":
            float(user_currently_added_value)
            values.append(user_currently_added_value)
        elif user_currently_added_value == "done":
            values.append(user_currently_added_value)
        else:
            print("Please enter a Valid Value")
    
    #Use calculating function

    #display answer

    #ask for if program should go again
