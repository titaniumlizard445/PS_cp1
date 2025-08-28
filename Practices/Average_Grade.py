#PS 1st Average grade

ClassGrades = []
ClassNumber = int(input("how many classes do you have"))
Average = 0
for i in range(0, ClassNumber):
    ClassGrades.append(input(f"what is your grade in class, {i}."))

for i in ClassGrades:
    Average = Average + int(i)

Average /= ClassNumber
Average = round(Average, 2)
print(Average)

