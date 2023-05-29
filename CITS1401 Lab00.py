## Q5
print("CITS1401")

## Q6
print("This program illustrates a chaotic function")
x = float(input("Enter a number between 0 and 1: ")) #taking input from user
for i in range(10):
    x = 3.9 * x * (1 - x)
    print(x)
#: First num with input 0.5: 0.975

## Q7
print("This program illustrates a chaotic function")
x = float(input("Enter a number between 0 and 1: ")) #taking input from user
for i in range(10):
    x = 2.0 * x * (1 - x)
    print(x)
#: Last num with input 0.5: 0.5

## Q8
print("This program illustrates a chaotic function")
x = float(input("Enter a number between 0 and 1: ")) #taking input from user
for i in range(18):
    x = 3.9 * x * (1 - x)
    print(x)
#: The 18th num: 0.6474314980965743

## Q9
print("This program illustrates a chaotic function")
x = float(input("Enter a number between 0 and 1: ")) #taking input from user
for i in range(10):
    x = 3.9 * x * (1 - x)
    if i == 9:
        print(x)
## OR
print("This program illustrates a chaotic function")
x = float(input("Enter a number between 0 and 1: ")) #taking input from user
for i in range(10):
    x = 3.9 * x * (1 - x)
print(x)
#: 0.1040097132674683