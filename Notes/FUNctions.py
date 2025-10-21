#PS 1st FUNctions

#set variables first then functions


def coolFuntionName():
    print("Parker wins")

coolFuntionName()

def coolNewFuntion(name,fav_num):
    print(f"Your name is {name} And your favorite number is {fav_num}")

coolNewFuntion("Robert",345)

def add(x,y):
    return x+y

total = add(5,5)
print(total)
print(f"10 + 72 = {add(10,72)}")

x = 0

while x < add(3,9):
    print("duck")
    x+=1

print("goose")

def initials(Name):
    names = Name.split(" ")
    initials = ""
    for Name in names:
        initials += Name[0]
    
    return initials

print(initials("Albert Has A Hat And His Ape"))

print(initials("Yarharhar Out Ur _ Getting On The _ Pack Randy And No Kicking Ed Darwin"))