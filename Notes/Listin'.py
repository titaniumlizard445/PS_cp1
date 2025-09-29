#PS 1st List Notes

import random as Random

Listable = ["Not a number" , True , 2 , 4.68]

print(Listable[2])
print(f"The list is {len(Listable)} somethings long ")

print(Listable)
Listable[0] = "Still not a number"

Listable[2:3] = [4 , 9.3276482349]
Listable.pop()
Listable.pop(2)
Listable.remove(True)

print(Listable)

Listable.clear()

print(Listable)

Listable.insert(1, True)
Listable.extend([3.14159265358979323846, 87, "Fr"])

print(Listable)

Fat_board = [
    ["_","_","_"],
    ["_","_","_"],
    ["_","_","_"]
]

print(Fat_board)

fruit = ("blueberries", "Strawberries","Blackberries")

setable = {"Not a set", "not a set", "your face"}

#print(Random.choice(Listable, weights=(50,20,28,2), k=4))


#PendingDeprecationWarning