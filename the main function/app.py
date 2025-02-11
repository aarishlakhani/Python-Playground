# main function

# This special name variable refers to the Python module this file represents
# One of two value when this code runs-
# 1. name of the file itself
# 2. main string with two underscores

# The purpose of the main function (if __name__ == "__main__":) is to prevent certain code from running when the script is imported.
# This doesn’t stop the script from running entirely.
# It only prevents the specific code inside if __name__ == "__main__" from running


# purpose is to conditionally run code if the file was run directly as a standalone program
def main():
    print("Hello from inside the main function")


if __name__ == "__main__":
    main()
