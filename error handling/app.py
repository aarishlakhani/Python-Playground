# example without error handling

# example 1
# try capturing a user data and converting it to an integer
# try:
#     number = int(input("Enter a number:"))
#     print("You entered: ", number)
# # If a user enters anything thats not a number
# except:
#     print("That is not a number")
# finally:
#     print("Completed")

# can also write except like this
# and this would print out the error
# except ValueError as e:
#   print("That is not a number")
#   print("Error: ", e)

# example 2
a = 10
b = 0

try:
    print(a / b)
except ZeroDivisionError as z:
    print("This cannot be divided")
    print("Error: ", z)
finally:
    print("Run again")
