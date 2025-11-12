#PS 1st Order Up (make a menu and give total cost of user selection)'

Side_dishes_ordered = 0
order = []
User_choice = ""
Cost = 0

#options for hamburgers and how much they are
Bamhurgers = {
    "CheeseBurger":7.00,
    "Double Pattie":15.00,
    "Hamburger":3.00,
    "Western Bacon":12.00,
    "Classic Bamhurger":5.00,
    "Burrito Bamhurger":10.00,
    "Breakfast Bamhurger":25.00
}
 
#options for drinks and how much they are
Dinks = {
    "Mylkshakes":{
        "Chocolate":10.00,
        "Vanilla":100.00,
        "Mint Chocolate":8.00
    },
    "Super duper delicious Dihydrogen Monoxide from a fresh spring in the Switzerland Alps":100.00,
    "approximately 3.14159265358979323846 oz of tap water":3.14,
    "Orange Juice":4.00,
    "Lemonade":2.50,
    "Dehydrated water (to make water just add water)":1000.00
}
#options for sides and how much they are
sides = {
    "French Fries": 3.00,
    "In-n-Out Fries":10.00,
    "Onion Rings":5.00,
    "Mac & Cheese":9.00,
    "salad":2.50
}
#whole menu
reasonably_price_menu = {
    "Hamburgers":Bamhurgers,
    "Drinks":Dinks,
    "Sides":sides
}

#Displays Individual menu and just makes code more modular
def IndividualMenu(Food_type):
    options = Food_type.keys()
    prices = Food_type.values()
    print({options})
    print({prices})

print("Hello and welcome to the Reasonably priced Restaurant located directly above I-15\n\nThe Freedom Diner\n\n")

Ordering = True
while Ordering:
    User_choice = ""
    #type of food they are ordering
    selection = input("What type of food would you like to order? \n 1) Bamhurgers \n 2) Drinks \n 3) Sides \n Please input the number here: ").strip()
    print(selection)
    #ordering Hamburgers
    if selection == "1":
        print("Please select one of the following to order with the prices below each respectively ")

        #Display Options
        IndividualMenu(Bamhurgers)
        #ask user what they want
        User_choice = input("What type of Bamhurger do you want? \n write here: ").strip()
        if User_choice in Bamhurgers:
            order.append(User_choice)
            Cost += Bamhurgers[User_choice]
        else:
            print("Invalid Input Please Try Again (Make sure to write it as it is in the Menu)")
    #ordering Drinks
    if selection == "2":
        print("Please select one of the following to order with the prices below each respectively")

        #Display Options
        IndividualMenu(Dinks)
        #ask user what they want
        User_choice = input("What type of Bamhurger do you want? \n write here: ").strip()
        if User_choice in Dinks:
            order.append(User_choice)
            Cost += Dinks[User_choice]
        else:
            print("Invalid Input Please Try Again (Make sure to write it as it is in the Menu)")
    #ordering two sides
    if selection == "3":
        print("Please select one of the following to order with the prices below each respectively")

        #Display Options
        IndividualMenu(sides)
        #ask user what they want

        User_choice = input("What type of Bamhurger do you want? \n write here: ").strip()
        if User_choice in sides:
            order.append(User_choice)
            Cost += sides[User_choice]
        else:
            print("Invalid Input Please Try Again (Make sure to write it as it is in the Menu)")

    #finish order
    done = input("Are you done ordering?").strip().lower()
    if done == "yes" or  done == "y":
        #check to make sure that the user has ordered two side dishes
        if Side_dishes_ordered >= 2:
            Ordering = False
        else:
            print("Please order two or more side dishes")
    else:
        print("\n Continue Ordering \n")

print(f"Your Order is: ")
for x in order:
    print(f"{x}\n")
print(f"The cost of your order is: {Cost}")