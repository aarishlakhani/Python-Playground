# user input
# This function would end once the input has been added
# We want to be able to save the input to a variable

# input("Your name, please: ")

# To store it in a variable name do this
name = input("Your name, please: ")
# The input is always string by default. You must convert it to an integer
age = int(input("Your age, please: "))

# either this way
# int(age)

print(f"Hello, My name is {name} and you are {age} years old ")

a = input("First number: ")
b = input("Second Number: ")
print(f"sum of those two number is {a+b}")
# This outputs 510 because we didnt convert them to integers first
# Earlier I did just float(a) and float(b) and this gave me 510 and not 15
# That was because I must assign the converted float(a) back to a
# Therefore a= float(a) is important
a = float(a)
b = float(b)
print(f"sum of those two number is {a+b}")
