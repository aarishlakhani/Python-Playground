# dictionaries
# Collection of key value pairs
# Can be used to count how often we "see" something
person = {"name": "aarish", "age": "23", "job": "egg collector"}
print(person)
print(person["name"])
print(person["job"])
# methods
# Get Method
print(person.get("name"))
# Keys and Value Method
# Dictionary View Data Type
# Mutable
print(person.keys())
print(person.values())
# Returns True= confirms age is a key in person
print("age" in person)

# Copy Method
copied_person = person.copy()
print("Copied Person: ", copied_person)
# Update Method
person.update({"name": "mario", "age": "35"})
print("Upated Person", person)
print("Copied Person", copied_person)

# Update Keys
# Keys are mutable to so cannot be directly updated
# To update keys you must completely delete the key and assign the popped values of old keys to new key name
print("Original Person:", person)
# Update the key "name" to "name1"
person["nameUpdated"] = person.pop("name")
print("Updated Person:", person)

print("mario" in person.values())

person.clear()
print("Cleared Dictionary", person)
