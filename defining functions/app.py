# defining functions
# print doesnt store a value
def greet():
    # The print() function in Python outputs text to the console but does not return a value that can be stored.
    print("Hello World")


greet()
greet()
# if I were to print greet() it would print none because it doesnt store a value
print(greet())


# return does store a value in result
def say_hello():
    # it stores aarish in variable name
    name = "aarish"
    return f"Hello {name}"


result = say_hello()
print(result)


# Example 3
def add_numberss(a, b):
    print(a + b)  # Only prints the sum, doesn't return it


result = add_numberss(5, 3)
print("Result:", result)  # This will print "Result: None"
# Output will be 8 and none. 8 for the first print statement in def and None for the result


# Example 4
def add_numbers(a, b):
    return a + b  # Returns the sum


result = add_numbers(5, 3)
print("Result:", result)  # This will print "Result: 8"
# Output will be 8
# Use return when You need the function output for further use.
# You want to store a value in a variable.
# You want to use the function’s result in calculations.

# Use print when
# You only need to display the output and don’t need to store it.
