## PARAMETER METHOD ##

def search_space(file, id, d1, d2, queryLocId_y, queryLocId_x, space_x, space_y, locList_data, missing):
    # 1. Find location of queryLocId
    # 2. Make search space around queryLocId according to d1(east-west) & d2(north-south)
    for row in file:
        # this_row format is [LocId, Latitude(x), Longitude(y), Category]
        if ", " in row:
            this_row = row.split(", ")
        elif "," in row:
            this_row = row.split(",")
        elif " " in row:
            this_row = row.split(" ")

        if this_row[0].upper() in missing:
            continue
        this_row[0] = this_row[0].upper()

        if this_row[0] == id:  # to find the data of the queryLocId
            if "\n" in this_row[-1]:  # find "\n" to be removed
                this_row[-1] = this_row[-1].replace("\n", "")
            queryLocId_x = float(this_row[1])
            queryLocId_y = float(this_row[2])
            space_x = [queryLocId_x - d1, queryLocId_x + d1]  # the most left & right of the space
            space_y = [queryLocId_y - d2, queryLocId_y + d2]  # the most bottom & top of the space
            locList_data.append(list(this_row))
            return queryLocId_y, queryLocId_x, space_x, space_y, locList_data

def find_id_in_space(file, space_x, space_y, queryLocId_x, queryLocId_y, locList, locList_data, missing):
    # Find IDs within search space
    for row in file:
        # this_row format is [LocId, Latitude(x), Longitude(y), Category]
        if ", " in row:
            this_row = row.split(", ")
        elif "," in row:
            this_row = row.split(",")
        elif " " in row:
            this_row = row.split(" ")

        if (this_row[0].upper() in missing) or (this_row[1].upper() in missing) or (this_row[2].upper() in missing):
            continue
        if "\n" in this_row[-1]:  # find "\n" to be removed
            this_row[-1] = this_row[-1].replace("\n", "")

        if "".join(this_row).isalpha() != True:  # to exclude table headers
            x = float(this_row[1])
            y = float(this_row[2])
            if (x >= space_x[0] and x <= space_x[1] and y >= space_y[0] and y <= space_y[1]) and (
                    x != queryLocId_x and y != queryLocId_y):  # when this LocId's within search space and not including the queryLocId
                this_row[-1] = this_row[-1].upper()
                locList.append(this_row[0])
                locList_data.append(list(this_row))
    return locList, locList_data

def same_category(simLocList, simLocList_data, locList_data):
    # Find IDs that are in the same category as queryLocId
    for i in range(1, len(locList_data)):
        if locList_data[i][-1] == locList_data[0][-1]:  # when this ID has the same category as the queryLocId
            simLocList.append(locList_data[i][0])
            simLocList_data.append(list(locList_data[i]))
    return simLocList, simLocList_data

def calc_dist(simLocList_data, distSorted, queryLocId_x, queryLocId_y):
    # 1. Find each of the distance between the queryLocId and IDs in the same category
    # 2. sort the distances
    for i in range(len(simLocList_data)):
        x = float(simLocList_data[i][1])
        y = float(simLocList_data[i][2])
        dist = ((x - queryLocId_x)**2 + (y - queryLocId_y)**2) ** (1/2)
        distSorted.append(float(format(dist, ".4f")))
    return sorted(distSorted)

def calc_avg_std(distSorted, avgstd):
    # Find mean & standard deviation of the IDs with the same category
    avg = sum(distSorted) / len(distSorted)
    var = sum(((x - avg)**2) for x in distSorted) / len(distSorted)
    std = var ** (1/2)
    avgstd = [float(format(avg, ".4f")), float(format(std, ".4f"))]
    return avgstd

def main(inputFile,queryLocId,d1,d2):
    ## Variables ##
    locList = []
    locList_data = []  # [[Id, latitude(y), longitude(x), category], ...]
    simLocList_data = []  # [[Id, latitude(y), longitude(x), category], ...]
    simLocList = []
    distSorted = []
    avgstd = []
    space_x = []
    space_y = []
    missing = ["", "NA", "N/A"]
    queryLocId_x = 0.0
    queryLocId_y = 0.0

    fopen = open(inputFile,"r")
    queryLocId = queryLocId.upper()

    queryLocId_y, queryLocId_x, space_x, space_y, locList_data = search_space(fopen, queryLocId, float(d1), float(d2), queryLocId_y, queryLocId_x, space_x, space_y, locList_data, missing)
    fopen.seek(0)
    locList, locList_data = find_id_in_space(fopen, space_x, space_y, queryLocId_x, queryLocId_y, locList, locList_data, missing)
    fopen.close()
    simLocList, simLocList_data = same_category(simLocList, simLocList_data, locList_data)
    distSorted = calc_dist(simLocList_data, distSorted, queryLocId_x, queryLocId_y)
    avgstd = calc_avg_std(distSorted, avgstd)

    return locList, simLocList, distSorted, avgstd


# locList,simLocList,distSorted,avgstd = main("Locations-sample-Project1.csv", "L83", 1.5, 2.2)
locList,simLocList,distSorted,avgstd = main("Project1edit.csv", "L83", 1.5, 2.2)
locList_sample = ['L3', 'L18', 'L47', 'L53', 'L91']
simLocList_sample = ['L3', 'L18', 'L53']
distSorted_sample = [0.4804, 1.6936, 2.2567]
avgstd_sample = [1.4769, 0.7412]
print(locList)
print(simLocList)
print(distSorted)
print(avgstd)

# locList,simLocList,distSorted,avgstd = main("Locations-sample-Project1.csv", "L83", 1.5, 2.2)
# locList,simLocList,distSorted,avgstd = main ("Locations-sample-Project1.csv", "L77", 3, 3.85)