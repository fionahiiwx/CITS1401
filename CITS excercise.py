# Q1
memo = []
def fib(n, memo):
    if memo[n] != None:
        return memo[n]
    if n <= 2:
        result = 1
    else:
        result = fib(n-1, memo) + fib(n-2, memo)
    memo[n] = result
    return memo[n]

def fib2(n):
    memo = [None] * (n+1)
    return fib(n, memo)
print(fib2(100))

# Q2
def fibonacci(n):
    seq = [0,1]
    if n == 0:
        seq = [0]
    for i in range(2,n+1):
        next_num = seq[-1] + seq[-2]
        seq.append(next_num)
    return seq
print(fibonacci(100))

# Q3
def fibsum(n):
    seq = [0,1]
    if n == 0:
        seq = [0]
    for i in range(2,n+1):
        next_num = seq[-1] + seq[-2]
        seq.append(next_num)
    return sum(seq)
print(fibsum(100))

# Q4
def fib25(n):
    seq = [0,1]
    seq25 = []
    if n == 0:
        seq = [0]
    for i in range(2, n+1):
        next_num = seq[-1] + seq[-2]
        seq.append(next_num)
    for j in seq:
        if (j == 0) or ((j % 2 != 0) and (j % 5 != 0)):
            seq25.append(j)
    return seq25, sum(seq25)
Fsum,Fseq = fib25(100)
print(Fsum)
print(Fseq)

# Q5
def numword(num):
    ones = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine", 10:"Ten",
            11:"Eleven", 12:"Twelve", 13:"Thirteen", 14:"Fourteen", 15:"Fifteen", 16:"Sixteen", 17:"Seventeen",
            18:"Eighteen", 19:"Nineteen"}
    tenths = {2:"Twenty", 3:"Thirty", 4:"Forty", 5:"Fifty", 6:"Sixty", 7:"Seventy", 8:"Eighty", 9:"Ninety"}
    if num > 99 or num < 1:
        return ("Number out of range")
    elif num < 20:
        return ones[num]
    num = list(str(num))
    return (tenths[int(num[0])] + " " + ones[int(num[1])])
print(numword(1))
print(numword(11))
print(numword(22))
print(numword(99))
print(numword(100))

# Q6
def add_matrices(mat1, mat2):
    matx = mat1[0] + mat2[0]
    maty = mat1[1] + mat2[1]
    return [matx, maty]
print(add_matrices([[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]))

# Q7
def num2str(num):
    ones = {1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight", 9:"Nine", 10:"Ten",
            11:"Eleven", 12:"Twelve", 13:"Thirteen", 14:"Fourteen", 15:"Fifteen", 16:"Sixteen", 17:"Seventeen",
            18:"Eighteen", 19:"Nineteen"}
    tenths = {2:"Twenty", 3:"Thirty", 4:"Forty", 5:"Fifty", 6:"Sixty", 7:"Seventy", 8:"Eighty", 9:"Ninety"}
    if num > 99 or num < 1:
        return ("Number out of range")
    elif num < 20:
        return ones[num]
    num = list(str(num))
    return (tenths[int(num[0])] + " " + ones[int(num[1])])
print(num2str(1))
print(num2str(11))
print(num2str(22))
print(num2str(99))
print(num2str(100))

# Q8
def mergelists(list1, list2):
    new_list = []
    for i in range(len(list1)):
        new_list.append(list1[i])
        new_list.append(list2[i])
    return new_list
print(mergelists([1,2,3],[4,5,6]))

# Q9
def sortoddeven(lst):
    odd = []
    even = []
    for i in lst:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return (odd + even)
print(sortoddeven([1,3,2,6,5,7,9,8,4]))


###########
ones = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine", 10:"Ten",
            11:"Eleven", 12:"Twelve", 13:"Thirteen", 14:"Fourteen", 15:"Fifteen", 16:"Sixteen", 17:"Seventeen",
            18:"Eighteen", 19:"Nineteen"}
for val, key in ones.items():
    print(val, key)

print(list((ones.items())))
print(sorted(ones.items(), key=lambda x:x[1]))
print(ones.get(20, 0))


#########
def abc(x):
    y = x[:]
    z = []
    for i in y:
        z.append(i)
    return z
a = [1,2,3,[]]
b = abc(a)
print(a)
print(b)
a[-1].append("a")
print(a)
print(b)