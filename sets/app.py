# sets- unordered and unique elements
# Another way to store data like list or tuples
# Doesnt allow duplicate data storing-unique
# unordered- do not maintain a fixed order. Will print in a different order everytime program is run
ingredient = {"tofu", "avacado", "cherry", "pasta", "tofu"}
# If we have duplicates it won't throw error but python doesn't print the duplicate
# Only one tofu is visible
print(ingredient)

# creating set by casting list into it
scores = [100, 25, 38, 100, 27]
set_scores = set(scores)
print(set_scores)

# add and remove methods
ingredient.add("tomato")
print(ingredient)
# Even though we have two tofu.
# It we still get print without either tofu
# This is because the second tofu was never added and ignored
# Therefore, even asked to remove it only has one tofu which it removes
ingredient.remove("tofu")
print(ingredient)
# Throws key error if you try to remove an element that doesn't exist
# ingredient.remove("apple")
ingredient.discard("avacado")
# discard it useful because it doesnt throw any errors if the element doesnt exist
# helpful if you are unsure if the element exists or not
print(ingredient)

# joining sets(union)
set_one = {1, 2, 3}
set_two = {3, 4, 5}
# union_set = set_one.union(set_two)
# Adds 3 only once cuz remember no duplicates
# | also means union
union_set = set_one | set_two
print(union_set)

# intersection
# For intersection can use & or set_one.intersection(set_two)
int_set = set_one & set_two
print(int_set)

# Difference = -
# Symmetric Difference(Returns  elements that are in either of the sets but not in both.) = ^
# Subset
# Checking if set_one is a subset of set_two
print(set_one <= set_two)
# Returns False= Not a subset

# Frozen(Immutable Sets)
ages = frozenset([19, 21, 35, 25])
print(ages)
# cannot use add or remove anymore and it prints frozenset({...})
# This is different than frozen list(which is basically a tuple)
# Frozen set removes duplicates and has no order
# Tuple maintains order and duplicates
