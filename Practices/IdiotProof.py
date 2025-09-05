#PS 1st Idiot Proof

name = input("What is your First and Last name? ")
Valid = False

while Valid != True:
    name = name.strip()
    first_name , Last_name = name.split(" ")

    if len(first_name) == 0 or len(Last_name) == 0:
        print("Invalid format, please try again. ")
        name = input("What is your First and Last name? ")
    else:
        Valid = True



phone_num = input("What is your Phone number? ")
Valid = False

while Valid != True:
    phone_num = phone_num.strip()
    area_code , telephone_prefix , line_number =  phone_num.split(" ")

    if len(area_code) == 3 and len(telephone_prefix) == 3 and len(line_number) == 4:
        Valid = True
    
    else:
        print("Invalid format, please try again. ")
        phone_num = input("What is your Phone number? ")



Grade_Point_Average = input("What is your Grade Point Average? ")
Valid = False

while Valid != True:
    Grade_Point_Average = Grade_Point_Average.strip()
    

    if float(Grade_Point_Average) > 4.0 or float(Grade_Point_Average) < 0.0:
        print("Number to high or to low please try again. ")
        Grade_Point_Average = input("What is your Grade Point Average? ")