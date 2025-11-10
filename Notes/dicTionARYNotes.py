#PS 1st Dictionary Notes

Car1 = {
    "Brand":"Koenigsegg",
    "Model":"Koenigsegg One",
    "Year":2015,
    "Color":"Silver",
    "Horsepower":1360,
    "Top Speed":"273 Mph",
    "Seats":2
}

Car2 = {
    "Brand":"Mustang",
    "Model":"Ford Mustange",
    "Year":1967,
    "Color":"Midnight Blue",
    "Horsepower":480,
    "Top Speed":"130 Mph",
    "Seats":5
}

Car3 = {
    "Brand":"Telsa",
    "Model":"CyberTruck",
    "Year":2023,
    "Color":"Silver",
    "Horsepower":845,
    "Top Speed":"130 Mph",
    "Seats":5
}



Cars = [Car1, Car2, Car3]

for x in Cars:
    print(f"The car is a {x["Brand"]}")
    print(f"The car is a {x["Model"]}")
    print(f"The car is from {x["Year"]}")
    print(f"The car is  {x["Color"]}")
    print(f"The car has {x["Horsepower"]} horsepower")
    print(f"The car goes {x["Top Speed"]} at top speed")
    print(f"The car has {x["Seats"]} seats\n")

