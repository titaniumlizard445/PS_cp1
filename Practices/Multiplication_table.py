#PS 1st Multiplication table

row = [1,2,3,4,5,6,7,8,9,10,11,12]
new_row = []
#Prints the calculated rows 
for a in row:
    for x in range(len(row)):
        new_element = row[x] * a
        new_row.append(new_element)
        #multiplies each row
    new_row.append(new_element)
print(list[new_row])