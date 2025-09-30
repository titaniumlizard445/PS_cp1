# PS 1st Shopping List Manager
running = True
items_to_permanently_borrow_from_the_store = []

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
