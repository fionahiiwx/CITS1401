# Q3
a = 10
b = 15
if a > b:
    a += b
else:
    a += b * 2

if a < b:
    print("awesome!")
elif a > 20:
    print("great!")
else:
    print("nice!")

#: great!

# Q4
a = 2
b = 1
c = 3

if a > b:
    if a > c:
        print("largest is a")
    else:
        print("largest is c")
elif c > b:
    if a < b:
        print("largest is c")
else:
    print("largest is b")

# Q5
def my_abs(n):
    n = int(n)
    if n == 0:
        return "zero"
    elif n > 0:
        return "positive"
    else:
        return "negative"
print(my_abs(-7.0))

#Q6
def is_odd(n):
    return ((n+1) % 2 == 0)
print(is_odd(2))

# Q7
def bmi_risk(bmi, age):
    if bmi < 22:
        if age < 45:
            return "Low"
        else:
            return "Medium"
    else:
        if age < 45:
            return "Medium"
        else:
            return "High"
print(bmi_risk(22, 45))

# Q8
def buy_goods(cost, savings):
    return (cost < ((5/100) * savings))
print(buy_goods(35, 1000))

# Q9
def record_check(age, gender, location):
    if age > 18 and gender == "M" and (location == "Perth" or location == "Sydney"):
        print("Found him!")
    else:
        print("Did not find him.")
record_check(19, 'M', 'Sydney')

# Q10
def balance_list(items):
    if len(items) % 2 != 0:
        items.append(items[-1])
    return items
print(balance_list([1, 2, 3, 4, 5, 6, 7, 8]))

# Q11
def double_list(items):
    if len(items) % 2 == 0:
        length = len(items)
        for i in range(length):
            items.append(items[i])
    else:
        items.append(items[-1])
    return items
print(double_list(["a", "b", "c", "d"]))

# Q12
def are_anagrams(word1, word2):
    if word1 == word2:
        return False
    else:
        word1 = sorted(list(word1))
        word2 = sorted(list(word2))
        return word1 == word2
if are_anagrams("poodle", "poodle"):
    print("Yes")
else:
    print("No")

# Q13
def locate_person(age_list, name_list, age, name):
    for i in range(len(age_list)):
        if age == age_list[i] and name == name_list[i]:
            return i
print(locate_person([15, 7, 3, 9, 11, 6, 8], ["David", "Tom", "Mary", "Sam", "Harry", "Abby", "Nigel"], 11, "Harry"))

# Q14
def hunting_animals(weather, animal, n):
    if animal == "rabbit":
        bullet = 1
    else:
        bullet = 2
    if weather == "rainy":
        bullet += 1
    return int(abs(n/bullet))
print(hunting_animals("rainy", "rabbit", 6))

# Q15
def check_temperature(temperature, limit):
    temperature = temperature * 9 / 5 + 32
    return limit > temperature
print(check_temperature(30.0, 80.0))

# Q16
def compare_strings(string1, string2):
    if string1[0] == string2[0]:
        if len(string1) == len(string2):
            return "error"
        elif len(string1) > len(string2):
            return string1
        else:
            return string2
    else:
        if string1[-1] == string2[-1]:
            return "error"
        elif ord(string1[-1]) > ord(string2[-1]):
            return string1
        else:
            return string2
print(compare_strings("band", "bread"))
print(compare_strings("abcdef", "abcdef"))
print(compare_strings("cloudy", "cloud"))
print(compare_strings("apple", "faf"))
print(compare_strings("same", "tame"))

# Q17
def can_jump(speed, power, name, injured):
    if injured:
        dist = power * speed * 0.8
    else:
        dist = power * speed

    if dist < 1:
        report = name, "made a false attempt!"
    else:
        dist = ["{:0.2f}".format(dist), "m!"]
        report = name, "can jump", "".join(dist)
    return " ".join(report)
print(can_jump(9.0, 0.6, "Brian", False))
print(can_jump(9.0, 0.6, "Morrison", True))
print(can_jump(9.0, 0.1, "A", True))

# Q18
def should_shutdown(battery_level, time_on):
    return (time_on < 60 and battery_level < 4.7) or (time_on >= 60 and battery_level < 4.8)
ans = should_shutdown(5, 10)
print(ans)
ans = should_shutdown(4.74, 90)
print(ans)
ans = should_shutdown(4.74, 50)
print(ans)

# Q19
def gcd(num1, num2):
    if (num2 == 0):
        return num1
    else:
        return gcd(num2, num1 % num2)
print(gcd(18,12))
print(gcd(24,36))
print(gcd(1024,960))

# Q20
def bitshift(s,k,b):
    s = list(s)
    if b:
        for i in range(k):
            s.append(s[0])
            s.remove(s[0])
    else:
        for i in range(k):
            s.insert(0,s[-1])
            s.pop()
    return "".join(s)
print(bitshift("10011",1,True))
print(bitshift("110011",2,True))
print(bitshift("110011",1,False))
print(bitshift("110011",2,False))

## or
def bitshift2(s,k,b):
    if b:
        return s[k:] + s[:k]
    else:
        return s[-k:] + s[:-k]
print(bitshift2("10011",1,True))
print(bitshift2("110011",2,True))
print(bitshift2("110011",1,False))
print(bitshift2("110011",2,False))

# Q21
def binarytodecimal(binary):
    binary = int(binary)
    decimal, i, n = 0, 0, 0
    while (binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return decimal
print(binarytodecimal('1011000100'))