#PS 1st Mappable notes

stuff = [243234,324,242,324,23,423,423,42,42,34,23,42,34234,2342]
more_stuff = []

#for i in stuff:
#    more_stuff.append(stuff/3)


some_stuff = map(lambda a: a/3, stuff)
print(some_stuff)
for a in some_stuff:
    print(a)