# Booleans
is_authenticated = True

print(is_authenticated)
# Should print to False because is_authenticated is True
# not is a logical operator in python
print(not is_authenticated)

# comparision operators
x, y = 5, 10
print("Is x=5 greater than y=10? :", x > y)
print("Is x=5 less than y=10? : ", x < y)
# == double equal to check and =single equal to assign
print("Is x=5 equal to y=10? : ", x == y)
#! is a comparision operator in python
print("Is x=5 not equal to y=10? : ", x != y)
# can use not with == to achieve the same results
print("Is x=5 not equal to y=10? : ", not (x == y))

print("Is x greater than or equal equal to y? :", x >= y)
print("Is x less than or equal equal to y? :", x <= y)

# boolean operators and member checking
x, y = True, False
print("x=True and y= False")
print("x and y", x and y)
print("x or y", x or y)

# Type Caste Values
# Falsy values --> 0 numbers and empty data structures
# It gives false if empty and true if full
print(bool(0))
print(bool(15))
print(bool("hello ninjas"))
print(bool([]))


# evaluating strings
name = "aarish"
print(name.startswith("a"))
print(name.startswith("m"))
print(name.endswith("o"))
