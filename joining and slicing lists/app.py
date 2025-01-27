# Joining Lists
ages_one = [25, 30, 49, 60, 75]
ages_two = [19, 65, 21, 44, 38]
ages_three = [33, 29, 13, 12, 10]

# This one is creating new variable, it doesn't interfere with old ages_one
joined_lists = ages_one + ages_two
print("Joined Lists:", joined_lists)
print("Ages One Before: ", ages_one)

# Extend method: interferes with the old variable and updates it
ages_one.extend(ages_two)
print("Ages One After Extended:", ages_one)

# Slicing Lists
# scores list remains unchanged, we just slice a copy of the porition
# we want to create new list with
scores = [100, 99, 85, 80, 22, 44, 64]
# It goes to index two but doesn't index 2. So we need to do 0:3
print("From start to index 2: ", scores[0:3])
print("From index 3 to end", scores[3:])
print("From index 1 to 4", scores[1:4])
# The second colon is to denote the step
print("From start to 4 with step of 2", scores[:4:2])
print("From start to end with a step of 2", scores[::2])
# By doing a step of -1 it goes back -1 at a time
print("Reversing the list:", scores[::-1])
