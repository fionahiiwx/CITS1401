## WITH with open() as file METHOD ##

def search_space(file, id, d1, d2, queryLocId_y, queryLocId_x, space_x, space_y, locList_data, id_index, lat_index,
                 lon_index, cat_index):
    # 1. Find location of queryLocId
    # 2. Make search space around queryLocId according to d1(east-west) & d2(north-south)
    for row in file:
        this_row = row.split(",")
        this_row[-1] = this_row[-1].replace("\n", "")  # to remove "\n"

        for index in range(len(this_row)):
            # identify the columns
            if this_row[index].upper() == "LOCID":
                id_index = index
            elif this_row[index].upper() == "LATITUDE":
                lat_index = index
            elif this_row[index].upper() == "LONGITUDE":
                lon_index = index
            elif this_row[index].upper() == "CATEGORY":
                cat_index = index

        this_row[id_index] = this_row[id_index].upper()

        if this_row[id_index] == id:
            # to find the data of the queryLocId
            queryLocId_x = float(this_row[lat_index])
            queryLocId_y = float(this_row[lon_index])
            space_x = [queryLocId_x - d1, queryLocId_x + d1]  # the most left & right of the space
            space_y = [queryLocId_y - d2, queryLocId_y + d2]  # the most bottom & top of the space
            locList_data.append(list(this_row))
    return queryLocId_y, queryLocId_x, space_x, space_y, locList_data, id_index, lat_index, lon_index, cat_index

def find_id_in_space(file, space_x, space_y, queryLocId_x, queryLocId_y, locList, locList_data, id_index,
                     lat_index, lon_index, cat_index):
    # Find IDs within search space
    for row in file:
        this_row = row.split(",")
        this_row[-1] = this_row[-1].replace("\n", "")  # find "\n" to be removed

        if "".join(this_row).isalpha() != True:
            # to exclude table headers
            this_row[id_index] = this_row[id_index].upper()
            x = float(this_row[lat_index])
            y = float(this_row[lon_index])
            if (x >= space_x[0] and x <= space_x[1] and y >= space_y[0] and y <= space_y[1]) and \
                    (x != queryLocId_x and y != queryLocId_y):
                # 1. This LocId's within search space
                # 2. Not including the queryLocId
                this_row[cat_index] = this_row[cat_index].upper()
                locList.append(this_row[id_index])
                locList_data.append(list(this_row))
    return locList, locList_data

def same_category(simLocList, simLocList_data, locList_data, id_index, cat_index):
    # Find IDs that are in the same category as queryLocId
    for index in range(1, len(locList_data)):
        if locList_data[index][cat_index] == locList_data[0][cat_index]:
            # when this ID has the same category as the queryLocId
            simLocList.append(locList_data[index][id_index])
            simLocList_data.append(list(locList_data[index]))
    return simLocList, simLocList_data

def calc_dist(simLocList_data, distSorted, queryLocId_x, queryLocId_y, lat_index, lon_index):
    # 1. Find each of the distance between the queryLocId and IDs in the same category
    # 2. sort the distances
    for index in range(len(simLocList_data)):
        x = float(simLocList_data[index][lat_index])
        y = float(simLocList_data[index][lon_index])
        dist = ((x - queryLocId_x) ** 2 + (y - queryLocId_y) ** 2) ** (1 / 2)
        distSorted.append(float(format(dist, ".4f")))
    return sorted(distSorted)

def calc_avg_std(distSorted):
    # Find mean & standard deviation of the IDs with the same category
    avg = sum(distSorted) / len(distSorted)
    var = sum(((x - avg) ** 2) for x in distSorted) / len(distSorted)
    std = var ** (1 / 2)
    avgstd = [float(format(avg, ".4f")), float(format(std, ".4f"))]
    return avgstd

def main(inputFile,queryLocId,d1,d2):
    # Variables
    locList = []
    locList_data = []
    simLocList = []
    simLocList_data = []
    distSorted = []
    avgstd = [0, 0]
    space_x = []
    space_y = []
    id_index = 0
    lat_index = 0
    lon_index = 0
    cat_index = 0
    queryLocId_x = 0.0
    queryLocId_y = 0.0

    queryLocId = queryLocId.upper()

    d1 = float(d1)
    d2 = float(d2)

    if d1 > 0 and d2 > 0:
        with open(inputFile, "r") as fopen:
            queryLocId_y, queryLocId_x, space_x, space_y, \
            locList_data, id_index, lat_index, lon_index, cat_index = search_space(fopen, queryLocId, d1, d2,
                                                                                   queryLocId_y, queryLocId_x, space_x,
                                                                                   space_y,
                                                                                   locList_data, id_index, lat_index,
                                                                                   lon_index, cat_index)
            if space_x != [] and space_y != []:
                fopen.seek(0)
                locList, locList_data = find_id_in_space(fopen, space_x, space_y, queryLocId_x, queryLocId_y, locList,
                                                         locList_data, id_index, lat_index, lon_index, cat_index)
                if locList != []:
                    simLocList, simLocList_data = same_category(simLocList, simLocList_data, locList_data, id_index,
                                                                cat_index)
                    if simLocList != []:
                        distSorted = calc_dist(simLocList_data, distSorted, queryLocId_x, queryLocId_y, lat_index,
                                               lon_index)
                        avgstd = calc_avg_std(distSorted)
                    else:
                        print("ZeroDivisionError: division by zero")
            else:
                print("Invalid ID")

    else:
        if d1 <= 0:
            print("Invalid d1")
        elif d2 <= 0:
            print("Invalid d2")

    return locList, simLocList, distSorted, avgstd

# locList,simLocList,distSorted,avgstd = main("Locations-sample-Project1.csv", "L83", 1.5, 2.2)
# locList,simLocList,distSorted,avgstd = main("Project1edit.csv", "L83", 1.5, 2.2)
locList,simLocList,distSorted,avgstd = main("Project1ChngColumn.csv", "L83", 1.5, 2.2)

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