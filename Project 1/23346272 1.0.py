## GLOBAL METHOD ##


######## EXP ########
## Input 1 ##
# locList,simLocList,distSorted,avgstd = main("Locations-sample-Project1.csv", "L83", 1.5, 2.2)
## Ouput
# locList
#: ['L3', 'L18', 'L47', 'L53', 'L91']
# simLocList
#: ['L3', 'L18', 'L53']
# distSorted
#: [0.4804, 1.6936, 2.2567]
# avgstd
#: [1.4769, 0.7412]

## Input 2 ##
# locList2,simLocList2,distSorted2,avgstd2 = main ("Locations-sample-Project1.csv", "L77", 3, 3.85)
# locList2
#: ['L4', 'L15', 'L17', 'L26', 'L30', 'L31', 'L33', 'L38', 'L52', 'L58', 'L88']
# simLocList2
#: ['L17', 'L52']
# distSorted2
#: [3.2559, 4.3635]
# avgstd2
#: [3.8097, 0.5538]


# Name: Fiona Hii
# Student ID: 23346272


def search_space(file, id, d1, d2):
    global queryLocId_y
    global queryLocId_x
    global space_x
    global space_y
    global locList_data
    for row in file:
        this_row = row.split(",")  # [LocId, Latitude(y), Longitude(x), Category]
        if this_row[0] in missing:
            continue
        this_row[0] = this_row[0].upper()
        if this_row[0] == id:  # to find the data of the queryLocId
            if "\n" in this_row[-1]:  # find "\n" to be removed
                this_row[-1] = this_row[-1].replace("\n", "")
            queryLocId_y = float(this_row[1])
            queryLocId_x = float(this_row[2])
            space_y = [queryLocId_y - d1, queryLocId_y + d1]  # the most bottom and top of the space
            space_x = [queryLocId_x - d2, queryLocId_x + d2]  # the most left and right of the space
            locList_data.append(list(this_row))
            break

def find_id_within_box(file):
    global locList
    global locList_data
    for row in file:
        this_row = row.split(",")
        if (this_row[0] in missing) or (this_row[1] in missing) or (this_row[2] in missing):
            continue
        if "\n" in this_row[-1]:  # find "\n" to be removed
            this_row[-1] = this_row[-1].replace("\n", "")
        if "".join(this_row).isalpha() != True:  # to exclude table headers
            y = float(this_row[1])
            x = float(this_row[2])
            if (x >= space_x[0] and x <= space_x[1] and y >= space_y[0] and y <= space_y[1]) and (x != queryLocId_x and y != queryLocId_y):  # when this LocId's within search space and not including the queryLocId
                this_row[-1] = this_row[-1].upper()
                locList.append(this_row[0])
                locList_data.append(list(this_row))

def same_category():
    global simLocList
    global simLocList_data
    for i in range(1, len(locList_data)):
        if locList_data[i][-1] == locList_data[0][-1]:  # when this ID has the same category as the queryLocId
            simLocList.append(locList_data[i][0])
            simLocList_data.append(list(locList_data[i]))

def calc_dist():
    global distSorted
    for i in range(len(simLocList_data)):
        y2 = float(simLocList_data[i][1])
        x2 = float(simLocList_data[i][2])
        dist = ((x2 - queryLocId_x)**2 + (y2 - queryLocId_y)**2) ** (1/2)
        distSorted.append(float(format(dist, ".4f")))
    distSorted = sorted(distSorted)

def calc_avg_std():
    global avgstd
    avg = sum(distSorted) / len(distSorted)
    var = sum(((x - avg)**2) for x in distSorted) / len(distSorted)
    std = var ** (1/2)
    avgstd = [float(format(avg, ".4f")), float(format(std, ".4f"))]

## Variables ##
locList = []
locList_data = []  # [[Id, latitude(y), longitude(x), category], ...]
simLocList_data = []  # [[Id, latitude(y), longitude(x), category], ...]
simLocList = []
distSorted = []
avgstd = []
space_x = []
space_y = []
missing = ["", "na", "NA", 0.0]
queryLocId_x = 0.0
queryLocId_y = 0.0

def main(inputFile,queryLocId,d1,d2):
    # OVERALL:
    # Find location of queryLocId
    # Make search space around the queryLocId according to d1 & d2
    # Find the IDs within search space
    # Find IDs that are in the same category as the queryLocId
    # Find distance of those ID from the ori ID and then sort them
    # Find mean and sd of them

    fopen = open(inputFile,"r")
    queryLocId = queryLocId.upper()
    search_space(fopen, queryLocId, float(d1), float(d2))
    fopen.seek(0)
    find_id_within_box(fopen)
    fopen.close()
    same_category()
    calc_dist()
    calc_avg_std()
    return locList, simLocList, distSorted, avgstd

locList,simLocList,distSorted,avgstd = main("Project1edit.csv", "L83", 1.5, 2.2)
print(locList)
print(simLocList)
print(distSorted)
print(avgstd)
# locList,simLocList,distSorted,avgstd = main("Locations-sample-Project1.csv", "L83", 1.5, 2.2)
# locList,simLocList,distSorted,avgstd = main ("Locations-sample-Project1.csv", "L77", 3, 3.85)