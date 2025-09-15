#PS 1st Crew Shares Project

#The crew earned a whole bunch of money on the last outing (an input in dollars), but the captain didn't have time to divvy it all up before release everyone to port. He gave each member of the crew 500 dollars for the evening and then sat down with his first mate to properly divide the shares. this program divides the shares


Money = float(input("How much money was earned on the voyage?"))
Crew = float(input("How many crew members were there (please input a number) on the voyage?"))
#caluculates shares and share value

shares = 7 + 3 + Crew
sharevalue = Money / shares

#assigning each member their money

captain_money = sharevalue * 7
first_mate_money = sharevalue * 3
Crew_money = sharevalue - 500

#telling the user how much each member of the crew gets

print(f"The captain receives: {captain_money:.2f}")
print(f"The first mate receives: {first_mate_money:.2f}")
print(f"The crew still needs: {Crew_money:.2f}")

