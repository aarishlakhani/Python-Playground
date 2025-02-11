# main function
# files can be imported using the import function
import helpers
from helpers import multiply

# If you dont want to do helpers.dot everytime you call a function
# you can just import the function itself using ==> from helpers import add
# This way you can just do result = add(2,7)

# note how we have helpers in the terminal, that is from the print(__name__) in the helpers file
# We print that without calling explicity because Python is a script. It calls everything except the main function which needs
# to be called explicitly


def main():
    print("hello from inside the main function, in the app file")
    # here we are using the helpers add function
    result = helpers.add(2, 7)
    print(result)
    result2 = multiply(2, 2)
    print(result2)


if __name__ == "__main__":
    main()
