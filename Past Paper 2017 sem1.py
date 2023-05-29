# Q1
def splitEmailAddress(Address):
    Address = Address.replace("@",".")
    return Address.split(".")
print(splitEmailAddress("Michael.Wise@uwa.edu.au"))

# Q2
def basename(P):
    x = P.split("/")
    for i in x:
        if "." in i:
            words = i.split(".")
    return words[0]
print(basename("/Users/michaelw/CITS1401/exam.doc"))

# Q3
def manhat(x,y):
    num = 0
    for i in range(len(x)):
        num += abs(y[i-1] - x[i-1])
    return num
print(manhat([1,3,5,7],[1,9,25,42]))

# Q5
def ft6b():
    numberGames = {}
    numberGames[(1,2,4)] = 5
    numberGames[(4,2,1)] = 10
    numberGames[(1,2)] = 12
    try:
        sum = 1
        for k in numberGames:
            sum *= numberGames[k]
        numberGames.append(sum)
        print('Try block executed.')
    except:
        print('Exception occured')
    print(numberGames, 'Sum=', sum)
ft6b()

# Q6
def merge(list1, list2):
    if len(list1) > len(list2):
        mlist = list1
        slist = list2
    else:
        mlist = list2
        slist = list1
    for item in slist:
        flag = True
        idx = 0
        while flag:
            if item < mlist[idx]:
                mlist.insert(idx,item)
                flag = False
            idx += 1
    return mlist
print(merge([1,3,5,11,12],[2,4,6,8]))

# Q7
def marksdistribution(D):
    grades = ["N","P","Cr","D","HD"]
    grade_count = [0,0,0,0,0]
    marks = {}
    for i in D:
        if D[i] < 50:
            grade_count[0]+=1
        elif D[i] < 60:
            grade_count[1]+=1
        elif D[i] < 70:
            grade_count[2]+=1
        elif D[i] < 80:
            grade_count[3]+=1
        else:
            grade_count[4]+=1
    for j in range(len(grades)):
        if grade_count[j] != 0:
            marks[grades[j]] = grade_count[j]
    return marks
print(marksdistribution({"Fred":55,"James":67,"Jemima":71}))

# Q8
def pow(x, n):
    if n == 0:
        return (1)
    if n == 1:
        return (x)
    if n % 2 == 0:
        x1 = pow(x, n // 2)
        return (x1 * x1)
    x1 = pow(x, n // 2)
    return (x * x1 * x1)
print(pow(2,3))