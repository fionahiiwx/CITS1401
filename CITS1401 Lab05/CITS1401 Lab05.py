# Q1
def get_name(name_dict, id_num):
    if id_num not in name_dict:
        return None
    else:
        return name_dict[id_num]
test_dictionary = {11:'Fred', 2001:'Agnes'}
print(get_name(test_dictionary, 2001))
test_dictionary = {11:'Fred', 2001:'Agnes'}
print(get_name(test_dictionary, 10))

print("\n") #################################

# Q2
def word_counter(input_str):
    counts = {}
    input_str = input_str.split(" ")
    if input_str == "":
        return counts
    else:
        for w in input_str:
            if w != "":
                counts[w.lower()] = counts.get(w.lower(),0) + 1
    return counts
word_count_dict = word_counter("This is a sentence")
items = word_count_dict.items()
sorted_items = sorted(items)
print(sorted_items)
word_count_dict = word_counter("A WORD is a word it is")
items = word_count_dict.items()
sorted_items = sorted(items)
print(sorted_items)
word_count_dict = word_counter("A a a a B B ")
items = word_count_dict.items()
sorted_items = sorted(items)
print(sorted_items)
print(word_counter(''))

print("\n") #################################

# Q3
def find_key(input_dict, value):
    count = 0
    for i in input_dict:
        count += 1
        if input_dict[i] == value:
            return i
        elif input_dict[i] != value and count == len(input_dict):
            return None

test_dictionary = {100:'a', 20:'b', 3:'c', 400:'d'}
print(find_key(test_dictionary, 'b'))
test_dictionary = {100:'a', 20:'b', 3:'c', 400:'d'}
print(find_key(test_dictionary, 'e'))

print("\n") #################################

# Q4
def make_index(words_on_page):
    new_dict = {}
    for i in words_on_page:
        for j in words_on_page[i]:
            if j not in new_dict:
                new_dict[j] = [i]
            elif j in new_dict:
                new_dict[j].append(i)
    return new_dict


input_dict = {
   1: ['hi', 'there', 'fred'],
   2: ['there', 'we', 'go'],
   3: ['fred', 'was', 'there']}
output_dict = make_index(input_dict)
for word in sorted(output_dict.keys()):
    print(word + ': ' + str(output_dict[word]))

print("\n") #################################

# Q5
def make_dictionary(filename):
    new_dict = {}
    with open(filename, "r") as fopen:
        for row in fopen:
            if row == "\n":
                continue
            row = row.replace("\n", "")
            if row not in new_dict:
                new_dict[row] = 1
            elif row in new_dict:
                new_dict[row] = new_dict[row] + 1
    return new_dict
dictionary = make_dictionary('jolly.txt')
for key in sorted(dictionary.keys()):
    print(key + ': ' + str(dictionary[key]))

print("\n") #################################

# Q6
def isbn_dictionary(filename):
    new_dict = {}
    try:
        with open(filename, "r") as fopen:
            for line in fopen:
                if line == "\n":
                    continue
                line = line.replace("\n", "").split(",")
                if line[-1] not in new_dict:
                    new_dict[line[-1]] = (line[0], line[1])
            return new_dict
    except FileNotFoundError:
        print("The file", filename, "was not found.")
        return None

your_dict = isbn_dictionary('books.csv')
if your_dict != None:
    for isbn in sorted(your_dict.keys()):
        print(isbn + ':', your_dict[isbn])
your_dict = isbn_dictionary('loads_of_books.csv')
if your_dict != None:
    for isbn in sorted(your_dict.keys()):
        print(isbn + ':', your_dict[isbn])

print("\n") #################################

# Q7
def long_enough(strings, min_length):
    new_list = []
    for i in range(len(strings)):
        if len(strings[i]) >= min_length:
            new_list.append(strings[i])
    return new_list
strings = ['a', 'bc', 'def', 'ghij', 'klmno']
print(long_enough(strings, 3))
strings = ['', '12', 'def', '123', 'klmno']
print(long_enough(strings, 0))

print("\n") #################################

# Q8
def my_enumerate(items):
    new_list = []
    for i in range(len(items)):
        new_list.append((i, items[i]))
    return new_list
ans = my_enumerate([10, 20, 30])
print(ans)

print("\n") #################################

# Q9
def run_length_encode(data):
    new_list = []
    for i in range(len(data)):
        if (data[i], data.count(data[i])) not in new_list:
            new_list.append((data[i], data.count(data[i])))
    return new_list
data = [5, 5, 5, 10, 10]
print(run_length_encode(data))
data = [10, 20, 30, 30, 30, 30]
print(run_length_encode(data))

print("\n") #################################

# Q10
def composite2(N):
    num = 0
    while N > 0:
        num += 1
        count = 0
        for i in range(1, num+1):
            if num % i == 0:
                count += 1
        if count > 2:  # composite: more than 2 divisions
            if num % 2 != 0:
                N -= 1
    return num
print(composite2(3))
print(composite2(5))

print("\n") #################################

# Q11
def series(x):
    a = 0
    n = 0
    while (1/(2**n)) >= x:
        a += (1/(2**n))
        n += 1
    return round(a,4)
print(series(0.5))
print(series(0.25))
print(series(0.01))
print(series(0.001))

print("\n") #################################

# Q12
def nextRound(k,scores):
    count = 0
    for i in scores:
        if i >= scores[k-1] and i > 0:
            count += 1
    return count
print(nextRound(5,[10,9,8,7,6,6,6,5,4]))
print(nextRound(2,[0,0,0,0]))

print("\n") #################################

# Q13
def singleDigit(N):
    while int(N) > 9:
        a = []
        for i in range(len(str(N))):
            N = str(N)
            a.append(int(N[i]))
        N = sum(a)
    return N
print(singleDigit(48))
print(singleDigit(198))

print("\n") #################################

# Q14
def sequence(n):
    new_list = [n]
    while int(n) > 1:
        if int(n) % 2 == 0:
            n = n/2
        else:
            n = 3 * n + 1
        new_list.append(int(n))
    return new_list
print(sequence(12))
print(sequence(20))

def sequence(n):
    lst = [n]
    while n != 1:
        if n % 2 == 0:
            n = int(n/2)
        else:
            n = int(n*3+1)
        lst.append(int(n))
    return lst
print(sequence(12))
print(sequence(20))