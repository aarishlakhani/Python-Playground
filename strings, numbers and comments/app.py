# declaring variables
name = "mario"
age = 30
height = 5.4

name = "luigi"
age = 32
height = "luigi"

# prining variables
print(name, age, height)

# type errors-trying to concatenate variable values together
# concatenating 3 strings would result the expected values
print(name + " is " + "height")
# concatenating strings with integers would throw a type error
# print(name + " is " + age)
# type casting to convert int to string
print(name + " is " + str(age))
# type casting to conver string to int
print(10 + int("20"))

# string methods
greeting = "  Hello, Aarish  "
# String Methods/Functions are both used to maniuplate strings.
# Functions are indepdent block of reusable code, called directly with the argument
# globally available, works across many data types and doesn't access object properties

# Methods are functions that belong to a specific object, it is called on an object(eg-greeting.strip())
# defined in the class of the object, speciic to a data type(str/int), operates on the calling object
# We use .dot notation to invoke methods

# Len function
print(len(greeting))
print(greeting.strip())
# notice how the output above it without whitespace but the output below is with
# Methods just call objects, they don't change their values
# They don't alter the original greeting, they just return a new string value
# Also called non-destructive methods, they don't destroy the original variable value
print(greeting.lower())
print(greeting.upper())
print(greeting.replace("Hello", "Yo").strip())
print(greeting)

# Comments
# for a single line comment
"""
multi-line comment using three single line quotes
"""
