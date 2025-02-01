# Control Flow-If Statements
score = 7
if score > 5:
    print("score is greater than 5")
# If/Else Statement
if score > 10:
    print("the score is greater than 10")
else:
    print("the score is less than 10")
# If/elif/else
if score > 10:
    print("the score is greater than 10")
elif score > 5:
    print("the score is greater than 5 but less than 10")
else:
    print("the score is 5 or less")
# AND, OR , NOT, IS NOT
age = 20
if age > 12 and age < 20:
    print("teenager")
if age < 13 or age > 19:
    print("not a teenager")

authenticated = True
# boolean moves to the next one only when true when autheticated is false and if not authenticated is the line
# since if not authenticated is true it prints the next line
if not authenticated:
    print("you are not authenticated")
if authenticated is not False:
    print("you are authenticated")
