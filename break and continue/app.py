count = 0
# break
# --> break out of loop
while count < 10:
    if count == 5:
        break
    # breaks after 0 1 2 3 4 and breaks out of the loop at count =5
    print(count)
    count += 1

# continue
# --> skip an interation
# the count enters this loop at 5 but doesnt print it, it adds +1 to the count then continues
# At count =9, count <10 but since the remainder is not equal to zero it conitnues and doesnt print
# and exit the loop. It prints 0 1 2 3 4 6 8 10 and not 9 because of this reason
while count < 10:
    count += 1
    if count % 2 != 0:
        continue
    print(count)
