#PS 1st What is your grade

while True:

    grade = input("Enter a grade here\n").strip()
    grade_without_percent = grade.strip("%")
    grades = []
    grades.append(float(grade_without_percent))
    divided_factor = len(grades)
    combined = grades.sum()
    average_grade = combined / divided_factor

    if average_grade > 100.0:
        print(f"You have an {average_grade} on average. That is technically equal to an A")
    elif average_grade >= 94.0:
        print(f" You have an {average_grade} on average. That is an A")
    elif average_grade >= 90.0:
        print(f" You have an {average_grade} on average. That is an A-")
    elif average_grade >= 87.0:
        print(f" You have an {average_grade} on average. That is an B+")
    elif average_grade >= 84.0:
        print(f" You have an {average_grade} on average. That is an B")
    elif average_grade >= 80.0:
        print(f" You have an {average_grade} on average. That is an B-")
    elif average_grade >= 77.0:
        print(f" You have an {average_grade} on average. That is an C+")
    elif average_grade >= 74.0:
        print(f" You have an {average_grade} on average. That is an C")
    elif average_grade >= 70.0:
        print(f" You have an {average_grade} on average. That is an C-")
    elif average_grade >= 65.0:
        print(f" You have an {average_grade} on average. That is an D")
    elif average_grade >= 60:
        print(f" You have an {average_grade} on average. That is an D-")
    elif average_grade <= 60:
        print(f" You have an {average_grade} on average. That is an F. DO BETTER")
    elif not average_grade:
        print("please enter a valid input")
    
    stop = input("Stop the Program?\n")
    
    if stop == "yes":
        break

