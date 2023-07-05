# Concatenating strings
str1 = "Welcome"
str2 = "from PBS"
result = str1 + " " + str2  
print (result)

# Accessing individual characters
my_string = "Python"
print(my_string[0])
print(my_string[-1]) 

# Slicing strings
my_string = "Python workshop from PBS"
print(my_string[0:6])
print(my_string[7:])   

# String length
my_string = "Python workshop from PBS"
print(len(my_string))

# Changing case (upper to lower & vice-versa)
my_string = "Python workshop from PBS"
print(my_string.upper())       # Convert to uppercase
print(my_string.lower()) 

# Finding substrings
my_string = "Hello, World!"
print(my_string.find("World"))
print(my_string.startswith("Hello"))
print(my_string.endswith("!"))

# Replacing substrings
my_string = "Hello, World!"
new_string = my_string.replace("Hello", "Hi")
print(new_string)

# Splitting and joining strings
my_string = "Hello, World!"
split_list = my_string.split(",")
new_string = "-".join(split_list)
print(new_string)

# Stripping whitespace
my_string = "   Python   "
print(my_string.strip())

# String formatting
name = "Alice"
age = 25
print("My name is {} and I am {} years old.".format(name, age))
print(f"My name is {name} and I am {age} years old.")
