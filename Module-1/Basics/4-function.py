# Defining a Function
def greet():
    print("Welcome to the world of Python!")

greet()           # function calling


# Function Parameters
def greet(name):
    print("Hello,", name)
# greet("Jitendra")
greet("Jeetu")

def welcome():
    print("Hello")
    print("world")
    print("hahahaha")

welcome()

# Function Return Values
def add_nums(a, b):
    return a + b
result = add_nums(5, 3)
print(result)


# Default Arguments
def greet(name="Guest"):
    print("Hello,", name)
greet()
greet("John")


# Variable Number of Arguments
def calculate_sum(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total
print(calculate_sum(1, 2, 3))  
print(calculate_sum(1, 2, 3, 4, 5))


# Lambda Functions
double = lambda x: x * 2
print(double(50))


# Scope
def calculate():
    result = 10
    print(result)
calculate()
print(result)   # error is expected


