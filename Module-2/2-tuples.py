# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)
empty_tuple = ()
single_element_tuple = (42,)
print (my_tuple)
print (empty_tuple)
print (single_element_tuple)

# Accessing tuple elements
print(my_tuple[0])
print(my_tuple[2:4])
print(my_tuple[-1])

# Tuple unpacking
new_tuple = (1,2,3)
a, b, c = new_tuple
print(a, b, c)
print(a)
print(b)
print(c)

# Tuple immutability
print (my_tuple)
my_tuple[0] = 10     # Error is expected here.
print (my_tuple)

# Tuple length 
print(len(my_tuple))

# Tuple concatenation and repetition
combined_tuple = my_tuple + (6, 7)
print (combined_tuple)
repeated_tuple = my_tuple * 3
print (repeated_tuple)

# Iterating over a tuple
for item in my_tuple:
    print(item)

# Tuple conversion from list to tuple
my_list = [1, 2, 3]
converted_tuple = tuple(my_list)
print (converted_tuple)