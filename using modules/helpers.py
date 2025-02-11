# main function
def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


print(__name__)


def main():
    print("hello from inside the main function, in the helpers file")


# this main function only runs when this check is true
# and this check is only true when we directly run this file
if __name__ == "__main__":
    print(__name__)
    main()
