# while loop
# loop over a bit of code set number of times while the certain condition is true
score = 0
while score < 10:
    print("the score is:", score)
    # score = score +1
    score += 1

user_input = ""
# As long as the user doesn't input q the condition will stay true
# and the loop will keep asking a letter to input
# The moment he/she enters q the != condition turns false and the loop exits
while user_input != "q":
    user_input = input("Enter a letter or enter 'q' to quit: ")
    print("You enterered: ", user_input)
print("You Quit!")
