# 1. Define a Python function stringexpand(name) which, given a string name, returns the
#    expanded string such that white space is added after each character of the input string.
#    For example, stringexpand(“Adam”) returns “A d a m”.

def stringexpand(name):
    return " ".join(list(name.replace(" ","")))
print(stringexpand("Adam"))

#######################################################################################################################

# 2. Define a Python function palindrome(word), which checks whether the input string is
#    palindrome or not (irrespective of whether the alphabets are upper or lower case) and
#    then returns boolean result accordingly. Palindrome string is the string which is same
#    both backwards and forwards. For example, palindrome("Racecar") will return True.
#    Similarly, palindrome("dude") will return False.

def palindrome(word):
    word_list = list(word.lower().replace(" ", ""))
    rev_word_list = list(reversed(word_list))
    return word_list == rev_word_list
print(palindrome("Racecar"))

#######################################################################################################################

# 3. Define a Python function sortdict(dict) which, given a dictionary dict of student IDs
#    and students WAM as keys and values respectively, returns the list of tuples sorted by
#    student WAM in descending order. For example,
#    sortdict({212222:35,2222222:85,2232222:55}) returns
#    [(2222222, 85), (2232222, 55), (212222, 35)]
#    Hint: Think about using sort() function with lists.

def sortdict(dict):
    print(dict.items())
    return sorted(dict.items(), key=lambda x:x[1], reverse=True)
print(sortdict({212222:35,2222222:85,2232222:55}))

#######################################################################################################################

# 4. [Use recursion to solve this problem]
#    Define a Python function sumdigits(n) which, given a positive integer, returns the sum
#    of the digits of input n.
#    For example, sumdigits(1234) returns 10 (obtained by summing all the digits of input: 1+2+3+4=10).

def sumdigits(n):
    if n == 0:
        return 0
    return (n%10 + sumdigits(int(n/10)))
print(sumdigits(1234))

#######################################################################################################################

# 5. Below mentioned is the Maclaurin series for the exponential function ex. Summing higher
# number of terms provides better approximation.

# (infinity, n=0)Capital Sigma ((x^n)/n!) = 1 + x + (x^2)/2! + ..... = e^x

# where “!” represents the factorial such as 1!=1,2!=2 x 1=2,3!=3 x 2 x 1=6 and so on.
# Define a Python function seriesexp(x,tol) which, given numerical values x and tol,
# returns the sum of the above series for input x till the absolute value of the term becomes
# smaller than tol. For example, seriesexp(1,0.1) returns 2.66666 which is obtained by
# adding first four terms only because the absolute value of fifth term (1^4)/4! becomes
# smaller than the input to the function 0.1 i.e. (1/24)<0.1

def seriesexp(x,tol):
    exp = 0
    n = 0
    while True:
        if n == 0:
            value = x**n
        else:
            den = 1 # denominator
            for i in range(1,n+1):
                den *= i
            value = (x**n)/den
        if value < tol:
            break
        exp += value
        n += 1
    return exp
print(seriesexp(1,0.1))

#######################################################################################################################

# 6. Write a Python function multiply_lists(lst) which can return the product of the
#    numerical data in the input list lst. However, it is possible that the input list, lst,
#    possibly contain other lists (which can be empty or further contain more lists). You can
#    assume that the lists only contain numerical data and lists. For example,
#    multiply_lists([1,2,[],3.5,4]) returns 28.0;
#    Similarly multiply_lists([1,[2],[3.5,[4]]]) also returns 28.0.
new_list = []
def multiply_lists(lst):
    num = 1.0
    if lst != []:
        for i in lst:
            if type(i) == list:
                multiply_lists(i)
            if i != [] and type(i) != list:
                new_list.append(i)
        for j in new_list:
            num *= j
    return num
print(multiply_lists([1,2,[],3.5,4]))

#######################################################################################################################

# 7. Claremont cricket club has many players and needs to make combinations of three
#    players for the practice sessions. There are three type of players: Batsman, bowler and
#    wicket-keeper. All of them are in different pools and the club needs to select one player
#    from each pool and make a combination. All players in each pool need to have practice
#    session with all players of other pool.
#    Write a python function team_maker(pool1,pool2,pool3) for the above situation
#    which, given three lists of pools of players (pool1,pool2,pool3) returns a list
#    containing all different combinations for the practice sessions. Each item of the output
#    list has the names of players combined as a string with a white space ' '.
#    For example,
#    team_maker(['Smith','Finch'],['Cummins','Lyon'],['Adam','Payne'])
#    returns ['Smith Cummins Adam', 'Smith Cummins Payne', 'Smith Lyon
#    Adam', 'Smith Lyon Payne', 'Finch Cummins Adam', 'Finch Cummins
#    Payne', 'Finch Lyon Adam', 'Finch Lyon Payne']

def team_maker(pool1,pool2,pool3):
    team_list = []
    for i in range(len(pool1)):
        for j in range(len(pool2)):
            for k in range(len(pool3)):
                if len(pool1[i]) > 0 and len(pool2[j]) > 0 and len(pool3[k]) > 0:
                    # Only team of 3 are formed
                    team_list.append(pool1[i]+" "+pool2[j]+" "+pool3[k])
    return team_list
print(team_maker(['Smith','Finch'],['Cummins','Lyon'],['Adam','Payne']))

#######################################################################################################################

# 8. Write a Python function user_account(filename) which, given a file name reads the file,
#    then extracts the users’ first name, last name and date of birth, creates the login and
#    passwords for the user and stores them in logins.txt. The file filename will be a text
#    file in which each value is separated by a comma "," character - and each line of values
#    is separated by a new line ("\n") at the end. Each extracted login and password is stored
#    in logins.txt in such a way that the values are separated by a comma "," and each user
#    data is stored in a separate line. The order of the user data is according to the title of the
#    column, however the order of the titles is not known. Therefore, you must need to search
#    the indexes of titles “First name”, “Last name” and “Date of birth” and use these indexes
#    in retrieving user’s data.
#    The methodology for creating the login is by combining first and last name with a dot "."
#    between them. The passwords are created by last name followed by a dollar sign "$"
#    which is followed by digits of date of birth.
#    For example, a file "userdata.txt" contains following five lines of text
#    s_no,First name,Middle name,Last name,Date of birth,Address,Phone
#    1, Ali,Kem,Khan,12/5/2000,Crawley WA,+43444444
#    2, John,Roger,Smith,1/12/1988,Perth City 6000,+61821021010
#    3, Sarah,Kimberly,Jones,22/8/1999,Subiaco WA,+61431312312
#    4, Huan,Jian,Li,5/8/2002,Claremont 6010 WA,+618323454
#    Running the function user_account("userdata.txt") creates the file login.txt
#    having following contents.
#    Ali.Khan,Khan$1252000
#    John.Smith,Smith$1121988
#    Sarah.Jones,Jones$2281999
#    Huan.Li,Li$582002

# find col, date, file
def find_col(file):
    # 1. Check if all 3 of the column is present
    # 2. Determine column header order
    f_name_ind = 0
    l_name_ind = 0
    dob_ind = 0
    missing_col = False
    count = 0

    for row in file:
        if len(row.split(",")) < 3:
            missing_col = True
            break

        this_row = row.split(",")
        this_row[-1] = this_row[-1].replace("\n", "")

        for index in range(len(this_row)):
            # identify the needed columns
            if this_row[index].upper() == "FIRST NAME":
                f_name_ind = index
                count += 1
            elif this_row[index].upper() == "LAST NAME":
                l_name_ind = index
                count += 1
            elif this_row[index].upper() == "DATE OF BIRTH":
                dob_ind = index
                count += 1
        break

    if count < 3:
        missing_col = True

    return f_name_ind, l_name_ind, dob_ind, missing_col, count

def check_file(file, f_name_ind, l_name_ind, dob_ind, filtered_file):
    days = [31, 27, 31, 31, 30, 31, 30, 31, 30, 31, 30, 31]
    leap_days = [31, 28, 31, 31, 30, 31, 30, 31, 30, 31, 30, 31]

    for row in file:
        this_row = row.split(",")
        this_row[-1] = this_row[-1].replace("\n", "")

        if this_row[f_name_ind].upper() != "FIRST NAME":
            # not header

            # check validity of the first and last names
            if len(this_row[f_name_ind]) < 1 or len(this_row[l_name_ind]) < 1:
                # missing names
                continue
            elif this_row[f_name_ind].isalpha() == False or this_row[l_name_ind].isalpha() == False:
                # name contain numbers or special symbols
                continue

            # check validity of the date of births
            dob = this_row[dob_ind]
            if "/" not in dob or dob.count("/") != 2 or "".join(dob.split("/")).isnumeric() == False:
                # dob not in correct format of day/month/year
                continue
            dob = dob.split("/")
            if dob[0] == "" or dob[1] == "" or dob[2] == "":
                # missing dob
                continue
            day = int(dob[0])
            month = int(dob[1])
            yr = int(dob[-1])
            if len(str(yr)) == 4:
                if month >= 1 and month <= len(days):
                    if yr % 4 == 0:
                        days_in_month = leap_days
                    else:
                        days_in_month = days
                else:
                    continue
            else:
                continue
            if day < 1 or day > days_in_month[month - 1]:
                continue

            filtered_file.append([this_row[f_name_ind], this_row[l_name_ind], this_row[dob_ind]])
    return filtered_file

def user_account(filename):
    alldata = ""
    filtered_file = []
    try:
        with open(filename, "r") as fopen:
            f_name_ind, l_name_ind, dob_ind, missing_col, count = find_col(fopen)
            if missing_col == False or count == 3:
                fopen.seek(0)
                filtered_file = check_file(fopen, f_name_ind, l_name_ind, dob_ind, filtered_file)
                if filtered_file != []:
                    for data in filtered_file:
                        username = data[0] + "." + data[1]
                        pas = data[1] + "$" + "".join(data[-1].split("/"))
                        dataline = username + "," + pas + "\n"
                        alldata += dataline
                    with open("login.txt", "w") as wfopen:
                        wfopen.write(alldata)
                else:
                    print("No valid data in the file")
            else:
                print("File has missing column(s)")
    except IOError:
        print("Invalid input file")

user_account("userdata.txt")