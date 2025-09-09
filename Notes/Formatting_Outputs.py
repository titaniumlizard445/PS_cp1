#PS 1st Formatting Outputs notes

name = "Ethan"
age = 1
money = 100000000
percent = 89

print("Hello {}, you are {:b}. That is so old. you have {:.2f} you must be poor! percent {:%}".format(name, age, money, percent))



print(f"Hello {name}, you are {age:,}. That is so old! You have {money:.2f} you must be poor! percent {percent:%}")
