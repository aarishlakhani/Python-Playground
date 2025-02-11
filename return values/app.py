# return  values
def square(x):
    return x * x


result = square(5)
print(result)


# returning multiple values are returned as a tuple
def get_coords():
    x = 25.5
    y = 48.2
    # python implicity turns this into a tuple and returns tutple with x and y
    return x, y


result = get_coords()
print(result)
# x, y = get_coords()
# print(x, y)

# using return to break out of a function
age = 15


def do_something():
    if age < 20:
        return
    print(age)


do_something()
