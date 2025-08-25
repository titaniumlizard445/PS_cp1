#PS 1st who_are_you
running = True
Users = []
dictionary = {}
while running:

    current_user = input("Enter your name here: ")
    if current_user in Users:
        print("You have already answered")
        print("You are",current_user, "and you are", dictionary[current_user,"Age"], "years old, and your favorite color is", dictionary[current_user,"Favorite color"]+".")

    else:
        Users.append(current_user)
        
        age = input("Enter your age: ")
        fav_color = input("What is your favorite color: ")
        
        dictionary[current_user , "Age"] = age
        dictionary[current_user , "Favorite color"] = fav_color 
    
    end = input("End the program?: ")
    if end == "yes":
        running = False
    
Users.clear()
dictionary.clear()