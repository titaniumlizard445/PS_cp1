# PS 1st Shopping List Manager

def UserSignIn():
    import time as Clock
    import random as Random

    UserUnlock = False

    Users = ["ParkerSwenson" , "Dirk" , "Bracken" , "Elijah" , "Liam", "PaxtonHall", "Watch", "ElementsOfTechnology", "Veritasium", "Water"]

    UserPasswords = {
        "ParkerSwenson" : "Uc@s1$TP3ri0d",
        "Dirk" : "676767",
        "Bracken" : "Fred",
        "Elijah" : "G@rry",
        "Liam" : "I_L1k3_C0d3",
        "PaxtonHall" : "P@k1$tan-rUlZ",
        "Watch":"H3@dPh0n35",
        "ElementsOfTechnology":"Tf2IzB3$t",
        "Veritasium" : "@n3leM3Nt0FTruth",
        "Water" : "H2O"
    }

    Timeout = Random.randint(1,4)



    while True:
        NameInput = input("Input Username Here:  ").strip()

        if NameInput in Users:
            UserUnlock = True
            PasswordInput = input("Input Password Here: ").strip()

            if PasswordInput == UserPasswords[NameInput]:
                print("Log in Success")
                print(f"Welcome, {NameInput}")
                break
            else:
                print("Invalid Password")
                if Timeout == 1:
                    print("Please wait 10 seconds before trying again")
                    Clock.sleep(10)
                elif Timeout == 2:
                    print("Please wait 20 seconds before trying again")
                    Clock.sleep(20)
                elif Timeout == 3:
                    print("Please wait 30 seconds before trying again")
                    Clock.sleep(30)
                elif Timeout == 4:
                    print("Please wait 60 seconds before trying again")
                    Clock.sleep(60)
        else:
            print("invalid Username")
            if Timeout == 1:
                print("Please wait 10 seconds before trying again")
                Clock.sleep(10)
            elif Timeout == 2:
                print("Please wait 20 seconds before trying again")
                Clock.sleep(20)
            elif Timeout == 3:
                print("Please wait 30 seconds before trying again")
                Clock.sleep(30)
            elif Timeout == 4:
                print("Please wait 60 seconds before trying again")
                Clock.sleep(60)




running = True
items_to_permanently_borrow_from_the_store = []

UserSignIn()
while running:
    print("\n Welcome to the shopping list manager choose one of the following by entering the number of the task that you want to use \n 1> Add an item to the list \n 2> remove items from the list \n 3> Display the shopping list \n 4> Leave the program")
    action = int(input("Input a number: "))
    
    if action == 1:
        item = input("What do you want to permanently borrow: ")
        items_to_permanently_borrow_from_the_store.append(item)
    elif action == 2:
        no_item = input("What item do you want to remove from the list of items that you want to permanently borrow from the store: ")
        if no_item in items_to_permanently_borrow_from_the_store:
            index = items_to_permanently_borrow_from_the_store.index(no_item)
            items_to_permanently_borrow_from_the_store.pop(index)
            print(f"{no_item} removed successfully")
        else:
            print("item is not in the list.")
    elif action == 3:
        print(f" You have {items_to_permanently_borrow_from_the_store} in your list")
    elif action == 4:
        running = False
    else:
        print("Not a valid input")
