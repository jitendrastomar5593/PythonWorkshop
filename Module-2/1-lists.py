# Creating a list
my_list = [1, 2, 3, 4, 5]
empty_list = []

# Accessing list elements
print(my_list[0])
print(my_list[2:4])
print(my_list[-1])

# Modifying list elements
my_list[0] = 10
my_list.append(6)
my_list.extend([7, 8])
my_list.insert(2, 11)
my_list.remove(3)
del my_list[1]

# Verifying the content
print(my_list)
print(len(my_list))
print(5 in my_list)

# List concatenation and repetition
combined_list = my_list + [6, 7]
repeated_list = my_list * 3
print (combined_list)
print (repeated_list)

# Iterating over a list:
for item in my_list:
    print(item)

# List sorting and reversing
my_list.sort()
my_list.sort(reverse=True)
my_list.reverse()
print (my_list)

# List comprehension
squares = [x**2 for x in my_list]
print(squares)