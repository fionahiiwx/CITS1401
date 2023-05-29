## Q1
a = 2*(3+4)**5/6-7-8
print(a)
b = (2*((3+4)**5)/6)-7-8
print(b)

## Q2
a = 4 + 5.0
print(type(a))

## Q3
a = 4//2
print(type(a))

## Q4
a = float("12")
print(type(a))

## Q5
#a = int("12.0")
#print(type(a))

## Q6
hurrah = "hurrah"
G_B_D = "G_B_D"
a1b2c3 = "a1b2c3"
a1 = "a1"
abc123 = "abc123"
#this_is_very_long_variable_name! = "long"
WelcomeHome = "WelcomeHome"
#123abc = "123abc"
some_var = "some_var"
#Welcome Home = "Welcome Home"
this_is_a_very_long_variable_name = "long long"

## Q8
apple = 15
pineapple = apple * 2 + 1
orange = apple + pineapple
orange = orange - (apple * 2)
print(orange)

## Q9
a = 10
b = 12
c = 15
d = 20
s = a**2 + b**2 + c**2 + d**2
print(s)

## Q10
x = int(input(""))
factorial = 1
if x == 0:
    print(factorial)
else:
    for i in range(1, x+1):
        factorial = factorial * i
    print(factorial)

## Q11
x = int(input())
sum = 0
if x < 0:
    for i in range(x, 1):
        sum += i ** 2
else:
    for i in range(x + 1):
        sum += i ** 2
print(sum)

## Q12
n = int(input())
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))
for i in range(n):
    fibonacci(i)
print(fibonacci(i))

## Q13
n = int(input())
summ = []
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))
for i in range(n):
    summ.append(fibonacci(i))
print(sum(summ))

## Another way of Q13
n = int(input())
a = 0
b = 1
summ = 1
if n <= 1:
    summ == n
else:
    for i in range(2,n):
        c = a + b
        a = b
        b = c
        summ += c
print(summ)