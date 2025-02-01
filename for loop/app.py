# for loop with lists --> iterate a collection of date over a certain range of numbers
# iterable means can loop through them
# lists, tuples,dictionary, sets and strings are iterable data type
# for is definite loop
names = ["aarish", "akbar", "arshaan", "navina"]
for name in names:
    print(name)
    # if I did print(names) instead it would still print 4 times but we will be calling the entire names list
print()
for name in names:
    if name == "arshaan":
        break
    print(name)
print()
# doesnt print out akbar only aarish arshaan navina
for name in names:
    if name == "akbar":
        continue
    print(name)
print()
# for loop with stirngs
# prints N I N J A
word = "ninja"
for letter in word:
    print(letter.upper())
