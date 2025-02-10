# use *args to accept any number of positional arguments
def print_total(*args):
    # *unpacked set and just args is a packed set as a tuple/list
    print(args)

    total = 0
    for number in args:
        total += number
    print(total)


# unpacking operator is useful when we want to pass varying amount of arguments into a function
# dynamic method
# no error because unpacking operator allows unlimited number of arguments to be passed into dynamically
print_total(50, 75)
print_total(24, 35, 79, 100, 15)


# use *kwargs to accept any number of keyword arguments
def print_ninja(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(f"{key}--{value}")
    return


print_ninja(name="aarish", age=23)
print_ninja(first_name="anna", belt_color="pink")
