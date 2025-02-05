# arguments
# pass value into a function when calling them
# allows functions to be reusable, flexible, and dynamic by passing different inputs
# positional arguments
def multiply(a, b):
    return a * b


# the position of 2 and 4 matter here
result = multiply(2, 4)
print(result)


# named arguments
def print_score(name, score):
    print(f"{name} has a score of {score}")


# positioning doesn't matter anymore because we are passing using their name/keyword
print_score(score=99, name="aarish")

# default arguments
# We can set default arguments like b=2 here
# These arguments are called when an argument for that variable is not set or assignment


def divide(a, b=2):
    return a / b


# This one will continue to divide 20/4 and not 20/2 because an argument has been set
# and no default argument is required to be looked for/called upon
result = divide(20, 4)
print(result)
# Since we only put only argument here it would use b=2 and print 25(50/2)
result = divide(50)
print(result)
