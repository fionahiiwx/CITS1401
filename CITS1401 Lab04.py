# Q1
x = ["HaVE A GrEAt DaY!".swapcase(), "HeLlO".lower(), "Welcome to an introduction to coding".replace("o", "u"),
     "watch out!".islower(),
     "Total: $6.33".startswith("Total:"),
     "excited".capitalize()]
y = ['hAve a gReaT dAy!', 'hello', 'Welcume tu an intruductiun tu cuding', False, True, 'EXCITED']
for i in range(len(x)):
    if x[i] == y[i]:
        print(True)
    else:
        print(False)

print("\n") ###########################################################################################################

# Q2
def is_a_number(string):
    if " " in string:
        string = "".join(string.split(" "))
    if "," in string:
        string = "".join(string.split(","))
    if "-" in string:
        string = "".join(string.split("-"))
    return string.isnumeric()
print(is_a_number('stubby'))
print(is_a_number('453'))
print(is_a_number('453 12'))
print(is_a_number('45,312'))
print(is_a_number('-453.12'))

print("\n") ###########################################################################################################

# Q3
def count_word(sentence, word):
    return sentence.count(word)
print(count_word('stubby tubby chubby gubby', 'tubby'))
print(count_word('1213141516171819', '1'))

print("\n") ###########################################################################################################

# Q4
def find_word(sentence, word):
    return sentence.index(word)
print(find_word('stubby tubby chubby gubby', 'tubby'))
print(find_word('1213141516171819', '1'))

print("\n") ###########################################################################################################

# Q5
def top_and_tail(string):
    return string[1:-1]
print(top_and_tail('stubby'))
print(top_and_tail('another test string'))

print("\n") ###########################################################################################################

# Q6
def half_string(string):
    if (len(string)+1) % 2 == 0:
        n = (len(string)-1)/2
    else:
        n = len(string)/2
    return string[0:int(n)]
print(half_string('stubby'))
print(half_string('spongebob'))

print("\n") ###########################################################################################################

# Q7
def second_half_string(string):
    if (len(string)+1) % 2 == 0:
        n = (len(string)-1)/2
    else:
        n = len(string)/2
    return string[int(n):]
print(second_half_string('stubby'))
print(second_half_string('spongebob'))
print(second_half_string('a'))
print(second_half_string('XY'))
print(second_half_string('XYZ'))

print("\n") ###########################################################################################################

# Q8
def first_nth_string(string, n):
    return string[:n]
item = first_nth_string("this is some string", 4)
print(item)
item = first_nth_string("this is some string", 7)
print(item)

print("\n") ###########################################################################################################

# Q9
def full_name(first_name, last_name):
    return first_name + " " + last_name
print(full_name('Alex', 'Ng'))
print(full_name('Malcolm', 'X'))

print("\n") ###########################################################################################################

# Q10
def count_items(data):
    return len(data)
print(count_items([1, 2, 3, 4, 5]))
print(count_items([1, 2]))

print("\n") ###########################################################################################################

# Q11
def count_item(data, item):
    return data.count(item)
print(count_item([1, 2, 3, 4, 5], 1))
print(count_item([1, 2, 1, 2, 1, 2], 2))

print("\n") ###########################################################################################################

# Q12
def third(data):
    return data[2]
print(third([10, 20, 30, 40, 50]))
print(third(['cat', 'dog', 'cow', 'chicken', 'crow']))

print("\n") ###########################################################################################################

# Q13
def insert_item_end(data, item):
    data.append(item)
    return data
print(insert_item_end([1, 2, 3, 4, 5], 1))
print(insert_item_end([1, 2, 1, 2, 1, 2], 2))

print("\n") ###########################################################################################################

# Q14 ??????????????????????????????????????
def append_list_new(data1, data2):
    new_data = []
    new_data.extend(data1)
    new_data.extend(data2)
    return new_data
print(append_list_new([1, 2, 3, 4, 5], [1]))
print(append_list_new([1, 2, 1, 2, 1, 2], [2, 3, 4, 5]))
test_list = [10, 20, 30]
count = append_list_new(test_list, [1])
test_list[0] = 5
if count != [10, 20, 30, 1]:
    print("Your new list is still referencing old lists!")

print("\n") ###########################################################################################################

# Q15 ?????????????????????????????????????
def append_lists(data1, data2):
    new_data = data1
    for i in data2:
        new_data.append(i)
    return new_data
print(append_lists([1, 2, 3, 4, 5], [1]))
print(append_lists([1, 2, 1, 2, 1, 2], [2]))
test_list = [10, 20, 30]
count = append_list_new(test_list, [1])
test_list[0] = 5
if count != [10, 20, 30, 1]:
    print("Your new list is still referencing old lists!")

print("\n") ###########################################################################################################

# Q16
def almost_last(data):
    return data[-2]
print(almost_last([10, 20, 40]))
print(almost_last([1, 2]))

print("\n") ###########################################################################################################

# Q17
def remove(data):
    data.pop(3)
    return data
print(remove([10, 20, 40, 80]))
print(remove([1, 2, 3, 4, 5]))

print("\n") ###########################################################################################################

# Q18
def nth_member(data, n):
    return data[n]
print(nth_member([10, 20, 30], 0))
print(nth_member(['bob', 'carol', 'ted', 'alice'], 3))

print("\n") ###########################################################################################################

# Q19
def duplicate_last(data):
    new_data = []
    for i in data:
        new_data.append(i)
    new_data.append(data[-1])
    return new_data
print(duplicate_last([1,2,3]))
print(duplicate_last(['hi']))
test_list = [1, 11, -17]
result_list = duplicate_last(test_list)
if test_list != [1, 11, -17]:
    print("Your function changed the list it was given!")

print("\n") ###########################################################################################################

# Q20
def cubed_tuple(number):
    res = (number, number**3)
    return res
print(cubed_tuple(1))
print(cubed_tuple(3))

print("\n") ###########################################################################################################

# Q21
def list_swap(lst):
    new_lst = []
    if (len(lst)) % 2 == 0:
        n = len(lst)
    else:
        n = len(lst) - 1
    for i in range(0,n,2):
        new_lst.append(lst[i+1])
        new_lst.append(lst[i])
    if (len(lst)+1) % 2 == 0:
        new_lst.append(lst[-1])
    return new_lst
print(list_swap([1,2,3,4,5]))
print(list_swap([12,32,54,24,51,23.54]))

print("\n") ###########################################################################################################

# Q22
def num_words(string):
    lst = string.split(" ")
    return len(lst)
print(num_words("Welcome to lists!"))
print(num_words("thi01234&*9 &^%x 1"))

print("\n") ###########################################################################################################

# Q23
def list_sorting(lst1,lst2):
    # lst1: names
    # lst2: age
    # name and age sort according the descending order of age
    # if same age, according to A-Z
    data = [[lst1[x], lst2[x]] for x in range(len(lst1))]
    new_lst1 = []
    new_lst2 = []
    while len(data) > 0:  # sorting the ages
        max_age = max(lst2)
        age = []
        for i in range(len(data)):
            if data[i][1] == max_age:
                age.append(data[i])
                lst1.remove(data[i][0])
                lst2.remove(data[i][1])
        for j in range(len(age)):
            data.remove(age[j])
            new_lst1.append(age[j][0])
            new_lst2.append(age[j][1])

    names = []
    for i in range(len(new_lst2)):
        count = new_lst2.count(new_lst2[i])
        if i > 0 and new_lst2[i] == new_lst2[i-1]:
            continue
        if count >= 2:
            for j in range(i, i+count):
                names.append(new_lst1[j])
            for k in range(count):
                new_lst1.pop(i)
            names = sorted(names)
            for l in range(count):
                new_lst1.insert(i+l, names[l])
            names = []

    return new_lst1, new_lst2

lst1, lst2 = list_sorting(["James", "Sam", "Emma", "Jake", "Suzie", "Charle"], [12, 15, 12, 11, 10, 11])
print(lst1)
print(lst2)
lst1, lst2 = list_sorting(["Namjoon", "Taehyung", "Yoongi", "Jungkook", "Jin", "Hoseok", "Jimin"], [27, 26, 28, 24, 29, 27, 26 ])
print(lst1)
print(lst2)
lst1, lst2 = list_sorting(["Niki", "Sunghoon", "Jake", "Jay", "Heeseung", "Jungwon", "Sunoo"], [16, 19, 19, 19, 20, 17, 18])
print(lst1)
print(lst2)

# another way
def list_sorting(lst1,lst2):
    # lst1: names
    # lst2: age
    # name and age sort according the descending order of age
    # if same age, according to A-Z
    data = [(lst1[x], lst2[x]) for x in range(len(lst1))] # USING TUPLE INSTEAD
    new_lst1 = []
    new_lst2 = []
    data.sort(key = lambda x:x[1], reverse = True) # SORTING WITH HELP OF THE TUPLE, LAMBDA THING
    for i in data:
        new_lst1.append(i[0])
        new_lst2.append(i[1])
    names = []
    for i in range(len(new_lst2)):
        count = new_lst2.count(new_lst2[i])
        if i > 0 and new_lst2[i] == new_lst2[i-1]:
            continue
        if count >= 2:
            for j in range(i, i+count):
                names.append(new_lst1[j])
            for k in range(count):
                new_lst1.pop(i)
            names = sorted(names)
            for l in range(count):
                new_lst1.insert(i+l, names[l])
            names = []
    return new_lst1, new_lst2

lst1, lst2 = list_sorting(["Namjoon", "Taehyung", "Yoongi", "Jungkook", "Jin", "Hoseok", "Jimin"], [27, 26, 28, 24, 29, 27, 26 ])
print(lst1)
print(lst2)
