#PS 1st While loops notes
import time as Clawk
import random as Hey
num = 1

while num <= 20:
    Clawk.sleep(0.25)
    num +=1
    print(num)


goose = Hey.randint(1,20)
count = 0

while count != goose:
    count += 1
    if count == goose:
        break
    else:
        print("duck")
else:
    print("goose")

i = 0

while i < 20:
    if i == 10:
        print("i is 10")
        continue
    else:
        print(f"{i} iteration of the loop")
    i += 1

print("the loop ended")