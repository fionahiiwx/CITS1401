def createUE(file):
    alldata = ""
    # fopen = open(file,"r")
    # wfopen = open("CITS1400 file open usernames", "w")
    with open(file,"r") as fopen:
        for line in fopen:
            ls = line.split(",")
            uname = ls[1][0] + ls[2][:-1]
            if len(uname) > 5:
                uname = uname[:5]
            email = (ls[1] + "." + ls[2][:-1] + "@student.uwa.edu.au")
            dataline = uname + "\t\t" + email + "\n"
            alldata = alldata + dataline
            # wfopen.write(uname + email + "\n\n")
    with open("CITS1400 file open usernames", "w") as wfopen:
        wfopen.write("Username\tEmail Address\n" + "="*55 + "\n")
        wfopen.write(alldata)
    # fopen.close()
    # wopen.close()
    print("End of process")

createUE("CITS1400 names.csv")