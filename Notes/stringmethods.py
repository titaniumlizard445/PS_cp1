#PS 1st String methods notes

subject = "Computer Programming 1!"

print(subject.upper())

print(subject.center(100))

print(subject)

# Stupid/idiot Proofing inputs
color = input("What is your favorite color?").strip().capitalize()
print("That is cool. I like " + color + " too!")

full_name = input("What is your full name?").strip().title()
print("That is cool " + full_name + ". I like "+ color + " too!")

print("That is cool  {full_name} . I like {color} too!".format(full_name = full_name, color = color))

#f-strings
print(f"That is cool {full_name}. I like {color} too!")

pi = "3.14159265358979323846"
#print(f"We all know pi is equal to {pi:.9f}")
#print(pi.isdecimal())

sentence = "The quick brown fox jumps over the lazy dog."

word = "jumps"
print(sentence.find(word))
start = print(sentence.index(word))
length = len(word)
#print(sentence[start:start+length])
print(sentence.replace(word, "swims"))
print(sentence)
