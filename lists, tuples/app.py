# Lists and Tuples are both collections of data
# Lists
# Lists use square brackets similar to arrays in java
name = ["aarish", "arshaan", "akbar"]

print(name)
print(name[1])
print(name[2])
print("The length of the list is:", len(name))

# Lists can be changed after they have been initialized, behave similar to arrays
name[1] = "navina"
print(name)

# list methods are functions that we use on particular datatype or object
name.append("bow")
print(name)

name.remove("aarish")
print(name)

name.sort()
print(name)

# Tuples
# Tupes use parenthesis
top_score = (100, 95, 92, 92, 85, 88, 90)
print(top_score)
print(top_score[0])
print(top_score[2])
print("The length of the tuple is", len(top_score))

# Tuples cannot be changed, they are immutable can be used for coordinates
# top_score[0] = 99= this would throw a typeerror saying 'tuple' object does not support item assignment
# Tuple methods
print(top_score.count(92))
print(top_score.index(92))
# Tuple cannot be sorted, to sort them we must convert them to a list
asse_top_score = list(top_score)
# this would sort it from assecending to descending
asse_top_score.sort()
print(asse_top_score)
