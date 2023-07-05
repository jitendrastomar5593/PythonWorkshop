# Dictionaries

# Creating a dictionary
my_dict = {"key1": "value1", "key2": "value2"}
print(my_dict)
empty_dict = {}
print(empty_dict)

# Accessing dictionary values
print(my_dict["key1"]) 

# Modifying dictionary values
my_dict["key1"] = "value3"
print(my_dict)
my_dict["key3"] = value3 
print(my_dict)

# Dictionary length and membership
print(len(my_dict))
print("key2" in my_dict)

# Removing key-value pairs
del my_dict["key1"]
print(my_dict)
my_dict.pop("key2")
my_dict.clear()
print(my_dict)

# Iterating over a dictionary
for key in my_dict:
    value = my_dict[key]
    print(key, value) 

# Dictionary methods
keys = my_dict.keys()
values = my_dict.values()
items = my_dict.items()
print(keys)
print(values)
print(items)

