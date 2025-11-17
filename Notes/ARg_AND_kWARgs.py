#PS 1st args and kwargs


def Parameter_ex(animal = "Chameleon", color = "Silver"):
    return f"This animal is {color} and is a {animal}"


print(Parameter_ex("Penguin","blue"))

print(Parameter_ex(color = "green", animal="frog"))

print(Parameter_ex())


def GoodMorning(*people, **times_of_day):
    for Person in people:
        if Person == "Liam":
            print("stop talking Liam")
        else:
            for time_of_day in times_of_day.values():
                print(f"Good Morning {Person} it is {time_of_day}. Are you ready for your routine?\n")

GoodMorning("Liam","Blaine","Elijah","Projector Screen","Computer","Isaac","Pryor","Dirk", Morning = "9:00am", Morning2 = "9:30am", Morning3 = "10:00am")