# Global and Local Variables
# variable scope refers to region the code is available, recognized and can be used

# Global Scope Variables
# Created outside of functions and accessible throughout the entire scripe including inside the functions
x = 10


def print_x():
    print(f"x inside the print_x function is {x}")


print_x()
print(f"global value of x is {x}")
# Local Scope Variables
# Created within a function which are only aviable to use inside a function
y = 20


def print_y():
    # Python automatically creates a variable inside the function it is used but until
    # changed inside it accessess the global one
    # If you wish to ever change the global variable inside the function it must be declared as
    global y
    # That way it would update the value of global variable with that of declared local
    # So both would output 25 inside and outside
    y = 25
    # local variable updaiting doesnt update global and when called y inside the
    # def it calls the one inside the function
    print(f"y inside the print_y function is {y}")


print_y()
print(f"global value of y is {y}")


# Enclosing Scope Variables
# Variables created inside a function that can then be accessed within nested functions within
# the original function
def outer():
    age = 25

    def inner():
        # works similar to global variable
        # since we dont want to update the global variable instead the one in its nearest
        # nonlocal scope
        nonlocal age
        age = 30
        print(f"age inside inner() is {age}")

    inner()
    print(f"age inside outer() is: {age}")


outer()
