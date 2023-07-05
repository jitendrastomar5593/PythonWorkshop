## Control flow

# if statement
x = -4
if x > 0:
    print("x is +ve")

# if-else statement
x = 35
if x > 0:
    print("x is +ve")
else:
    print("x is -ve")

# if-elif-else statement
x = -10
if x > 0:
    print("x is +ve")
elif x == 0:
    print("x is 0")
else:
    print("x is -ve")



## Loops

# for loop
tech = ['Python','AI',"ML"]
for t in tech:
    print(t)

# while loop
x = 0
while x < 5:
    print(x)
    x += 1

# break statement
tech = ['AI',"ML",'Python']
for t in tech:
    if t == "Python":
        break
    print(t)

# continue statement
tech = ['AI',"ML",'Python']
for t in tech:
    if t == "Python":
        continue
    print(t)

# pass statement
x = 5
if x > 0:
    pass  # Placeholder for future code
else:
    print("x is non-positive")
