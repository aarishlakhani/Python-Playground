# formatted strings (f-string)
# Better than strings because they are dynamic and normal strings are static/hardcoded
name = "aarish"
age = 50

# examples- normal strings
# Reason why these are bad-pretty annoying to do "" multiple times
# Annoying to convert score to str
print("My name is " + name + " and I am " + str(age) + " years old.")
print("My name is", name, "and I am ", str(age), " years old.")

# example -fstring-new method
# python does the implicit type conversion and does heavy lifting for us
# Uses f at the start and curly brackets {}
print(f"My name is Aarish and I am {age} years old.")

# example-fstring-old method using .format method
# first {} brace to apply first argument name
# Second {} brace to apply second argument age
print("{} is of age {}".format(name, age))
# Can also use indexes of the argument
print("{1} is of age {0}".format(name, age))
# Can also use named arguments
print("{n} is of age {a}".format(n=name, a=age))

# expressions in f-strings
# using capitalize to capitalize the first letter
print(f"{name.capitalize()} will live till {age *2}")
