# for loop with ranges
# Start at 0 and loop 5 times. 0 1 2 3 4
for i in range(5):
    print(i)
print()
# start at 10 and loop till 20 not inclusive
for i in range(10, 20):
    print(i)
print()
# third number 2 is the step count
# goes in the steps of 2
for i in range(10, 20, 2):
    print(i)
print()
# negative steps
# If I only did 10, 0 it would not have printed anything
# Since the natural movement is to go upwards
# Thats why step of -1 is needed. It goes one step back
for i in range(10, 0, -1):
    print(i)
print()
for i in range(20, 10, -2):
    print(i)
