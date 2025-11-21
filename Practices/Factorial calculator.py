#PS 1st someone elses pseudocode factorial calculator

#Key for changes
#PS(Change) my changes
#everything else was someone else



#define function Factorial(number):
def Factorial(number):
    #total=1
    total =1
    #For i in range(number):
    for i in range(number):
        #total=total*number
        total=total*number
        #number-=1
        number-=1
    #return total
    return total

#print("Welcome to Factorial Calculator!")
print("Welcome to Factorial Calculator!")
#While True:
while True:
    #number=input("Enter a whole non-zero number.")
    number=input("Enter a whole non-zero number.")
    #If number.isint()==False or int(number)==0:
    #PS(.isint() is not a valid method replace with isdigit())
    if number.isdigit()==False or int(number)==0:
        #Print("Invalid answer")
        print("Invalid answer")
        #continue
        continue
    #else:
    else:
        #number=int(number)
        number=int(number)
        #total=Factorial(number)
        total=Factorial(number)
        #print(f"Original num: {number} | Factorial: {Total}")
        print(f"Original num: {number} | Factorial: {total}")
        #go_again=input("would you like to get the Factorial of another number? Yes/No").strip().Capitalize()
        go_again=input("would you like to get the Factorial of another number? Yes/No").strip().capitalize()
        #if go_again == "Yes":
        if go_again == "Yes":
            #Continue
            continue
        #else:
        else:
            #print("good bye!")
            print("good bye!")


