"""Demonstrations of Dictionary Capabilities."""


# Declaring the type of a dictionary
schools: dict[str, int]

# Intialize to an empty dictionary
schools = dict()

# Set a key-value pairing in the dictionary
schools["UNC"] = 19400
schools["Duke"] = 6717
schools["NCSU"] = 26150

# print a ditionary literal representation
print(schools)

# Access a value by its key -- "lookup"
print(f"UNC has {schools['UNC']} Students.")

# Remove a key-value pair from dictionary 
# By its key.
schools.pop("Duke")

# Test for the existance of a Key
is_duke_present: bool = "Duke" in schools
print(f"Duke is present: {is_duke_present}")


# Upddate/reassign a key value pair
schools["UNC"] += 20000
schools["NCSU"] += 200

print(schools)

# Demonstration of dictionary literals

# empty dictionary literal
schools = {}  # same as dict()
print(schools)

# Alternatively, initizie key value pairs
schools = {"UNC": 19400, "Duke": 6717, "NCSU": 26150}
print(schools)

# What happens when a key does not exists?
# print(schools["UNCC"])


# Example looping over the keys of a dict
for key in schools:
    print(f"Key: {key} -> Value: {schools[key]}")

for school in schools:
    print(f"Key: {school} -> Value: {schools[school]}")