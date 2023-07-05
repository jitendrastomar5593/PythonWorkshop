# File handling in Python

# Opening a file
# file = open("Module-2\demo.txt", "r")
# file = open("Module-2\demo.txt", "w")
# file = open("Module-2\demo.txt", "a")

# Reading from a file
file = open("Module-2\demo.txt", "r")
content = file.read()
print(content)
file.close()

# Writing to a file
file = open("Module-2\demo.txt", "w")
file.write("Hello everyone, from PBS")
file.close()

# Appending to a file
file = open("Module-2\demo.txt", "a")
file.write("\nthis is another 3rd line")
file.close()

# Using 'with' statement
with open("Module-2\demo.txt", "r") as file:
    content = file.read()
    print(content)

# Reading file line by line
with open("Module-2\demo.txt", "r") as file:
    for line in file:
        print(line)

# Checking file existence
import os
if os.path.exists("Module-2\demo.txt"):
    print("File exists")
else:
    print("No such file exists!!")