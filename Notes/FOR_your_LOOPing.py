#PS 1st For loops notes

Numbers = [34,453,23523,235435,23464346745,435356,23546,3453522,32425,234,63,23,325,52345,324,324234,324]

for i in Numbers:
    i /= 2
    if i > 100:
        print(f"{i} is only half of {i*2}. It is a large number")
    else:
        print(i)

print("The loops is over")

for i in range(1,20,2):
    print(i)

for i in range(20,0,-2):
    print(i)