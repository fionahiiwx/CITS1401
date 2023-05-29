# Student Name: Fiona Hii (Hii Wan Xuan)
# Student ID: 23346272

def find_col(file, missing_col):
    # 1. Check if all 4 of the column is present
    # 2. Determine column header order
    locid_ind = 0
    lat_ind = 0
    lon_ind = 0
    cat_ind = 0

    for row in file:
        if len(row.split(",")) < 4:
            print("File has missing column(s)")
            missing_col = True
            break

        this_row = row.split(",")
        this_row[-1] = this_row[-1].replace("\n", "")

        for index in range(len(this_row)):
            # identify the columns
            if this_row[index].upper() == "LOCID":
                locid_ind = index
            elif this_row[index].upper() == "LATITUDE":
                lat_ind = index
            elif this_row[index].upper() == "LONGITUDE":
                lon_ind = index
            elif this_row[index].upper() == "CATEGORY":
                cat_ind = index
            else:
                break
        break

    return locid_ind, lat_ind, lon_ind, cat_ind, missing_col

def duplicate_locid(file, dup_dict, locid_ind):
    # Finding which LocID is duplicated and which is not duplicated in the file
    for row in file:
        this_row = row.split(",")
        this_row[-1] = this_row[-1].replace("\n", "")
        locid = this_row[locid_ind].upper()

        if locid not in dup_dict:
            dup_dict[locid] = 0
        else:
            dup_dict[locid] += 1
    return dup_dict

def check_querylocid(file, locid_ind, cat_ind, locIDs_list, data, lon_ind, lat_ind):
    # 1. Check if both the queryLocId is in the data
    # 2. Get the data of both the LocId

    count_locid1 = 0
    count_locid2 = 0

    for row in file:

        this_row = row.split(",")
        this_row[-1] = this_row[-1].replace("\n", "")
        this_row[locid_ind] = this_row[locid_ind].upper()
        this_row[cat_ind] = this_row[cat_ind].upper()

        if this_row[locid_ind].upper() == locIDs_list[0].upper() and this_row[lon_ind] != "" and this_row[
            lat_ind] != "" and this_row[cat_ind] != "":
            count_locid1 += 1
            data[0].append(this_row)
        elif this_row[locid_ind].upper() == locIDs_list[1].upper() and this_row[lon_ind] != "" and this_row[
            lat_ind] != "" and this_row[cat_ind] != "":
            count_locid2 += 1
            data[1].append(this_row)

    return data, count_locid1, count_locid2


def search_space(file, radius, data, locid_ind, lat_ind, lon_ind, cat_ind, dup_dict):
    # Find which LocId is within either or both of the circle

    for row in file:

        this_row = row.split(",")
        this_row[-1] = this_row[-1].replace("\n", "")
        this_row[locid_ind] = this_row[locid_ind].upper()
        this_row[cat_ind] = this_row[cat_ind].upper()

        if this_row[0].isalpha() == False and this_row[locid_ind] != "" and this_row[lat_ind] != "" and this_row[
            lon_ind] != "" and this_row[cat_ind] != "" and dup_dict[this_row[locid_ind]] == 0:
            # Not the header,with no missing data and no duplications
            lat = float(this_row[lat_ind])
            lon = float(this_row[lon_ind])
            dist1 = ((lat - float(data[0][0][lat_ind])) ** 2 + (lon - float(data[0][0][lon_ind])) ** 2) ** (1 / 2)
            dist2 = ((lat - float(data[1][0][lat_ind])) ** 2 + (lon - float(data[1][0][lon_ind])) ** 2) ** (1 / 2)
            if dist1 <= radius and this_row != data[0][0]:
                # within the first circle and not the queryLocID
                data[0].append(this_row)
            if dist2 <= radius and this_row != data[1][0]:
                # within the second circle and not the queryLocID
                data[1].append(this_row)
    return data


def types_of_cat(file, cat_list, cat_ind):
    # Finding all the different types of category present in the data
    for row in file:
        this_row = row.split(",")
        this_row[-1] = this_row[-1].replace("\n", "")
        cat = this_row[cat_ind].upper()
        if cat not in cat_list and cat != "CATEGORY":
            cat_list.append(cat)
    return cat_list


def LDCount_process(data, cat_ind, LDCount, cat_list):
    # Finding the amount of LocID, within each circle, in each category
    for i in range(len(data)):
        for cat in cat_list:
            count = 0
            for j in range(len(data[i])):
                if data[i][j][cat_ind] == cat:
                    count += 1
            LDCount[i][cat] = count
    return LDCount


def cal_simScore(LDCount):
    # Calculate using the cosine similarity score formula
    numerator = 0
    dena = 0  # denominator a
    denb = 0  # denominator b
    for cat1, val1 in LDCount[0].items():
        numerator += val1 * LDCount[1].get(cat1, 0.0)
        dena += val1**2
    for val2 in LDCount[1].values():
        denb += val2**2
    return numerator / ((dena * denb) ** (1 / 2))


def find_DCommon(data, DCommon, cat_list, cat_ind, locid_ind):
    common_list = []

    # finding if data[0] or data[1] is longer
    if len(data[0]) > len(data[1]):
        x = data[0]
        y = data[1]
    else:
        x = data[1]
        y = data[0]

    # using the longer ones to compare each of its element to the shorter one
    # if that element is present in both places, the locID of that is added to common_list
    for i in range(len(x)):
        if x[i] in y:
            common_list.append(x[i])

    # making the dictionary of category as key and locID as value
    for cat in cat_list:
        DCommon[cat] = []
        for i in range(len(common_list)):
            if common_list[i][cat_ind] == cat:
                DCommon[cat].append(common_list[i][locid_ind])
    return DCommon


def find_LDClose(data, LDClose, locid_ind, lat_ind, lon_ind, cat_ind, cat_list):
    for i in range(len(data)):
        for cat in cat_list:
            locid = ""
            distance = 0
            for j in range(1, len(data[i])):
                if data[i][j][cat_ind] == cat:
                    # this locID has the same category as the cat
                    lat = float(data[i][j][lat_ind])
                    lon = float(data[i][j][lon_ind])
                    dist = ((lat - float(data[i][0][lat_ind])) ** 2 + (lon - float(data[i][0][lon_ind])) ** 2) ** (
                                1 / 2)
                    if distance == 0:
                        # for the first element added to the locid and distance
                        locid = data[i][j][locid_ind]
                        distance = dist
                    else:
                        if dist < distance:
                            locid = data[i][j][locid_ind]
                            distance = dist
            if locid != "" and distance != 0:
                # empty locid and distance is not added to the LDClose dictionary
                LDClose[i][cat] = (locid, round(distance, 4))
    return LDClose


def main(inputFile, locIds, radius):
    LDCount = [{} for i in range(len(locIds))]
    simScore = 0.0
    DCommon = {}
    LDClose = [{} for i in range(len(locIds))]
    missing_col = False
    data = [[], []]
    cat_list = []
    dup_dict = {}

    if len(locIds) == 2:
        # Contains both the LocID
        if radius > 0:
            try:
                with open(inputFile, "r") as fopen:
                    locid_ind, lat_ind, lon_ind, cat_ind, missing_col = find_col(fopen, missing_col)
                    if missing_col == False:
                        fopen.seek(0)
                        dup_dict = duplicate_locid(fopen, dup_dict, locid_ind)
                        fopen.seek(0)
                        data, count_locid1, count_locid2 = check_querylocid(fopen, locid_ind, cat_ind, locIds, data, lon_ind, lat_ind)
                        if count_locid1 == 1 and count_locid2 == 1:
                            # Both queryLocId are present in the file
                            fopen.seek(0)
                            data = search_space(fopen, radius, data, locid_ind, lat_ind, lon_ind, cat_ind, dup_dict)
                            if len(data[0]) > 1 and len(data[1]) > 1:
                                # There are LocId in those 2 circle
                                fopen.seek(0)
                                cat_list = types_of_cat(fopen, cat_list, cat_ind)
                                LDCount = LDCount_process(data, cat_ind, LDCount, cat_list)
                                simScore = round(cal_simScore(LDCount), 4)
                                DCommon = find_DCommon(data, DCommon, cat_list, cat_ind, locid_ind)
                                LDClose = find_LDClose(data, LDClose, locid_ind, lat_ind, lon_ind, cat_ind, cat_list)
                        else:
                            if count_locid1 < 1 or count_locid2 < 1:
                                # Both or either one of the queryLocId is missing in the file
                                if count_locid1 < 1 and count_locid2 < 1:
                                    print("Invalid queryLocId1 and queryLocId2")
                                elif count_locid1 < 1:
                                    print("Invalid queryLocId1")
                                else:
                                    print("Invalid queryLocId2")
                            else:
                                # Both or either one of the queryLocId has duplications in the file
                                if count_locid1 > 1 and count_locid2 > 1:
                                    print("File contain duplications of queryLocId1 and queryLocId2")
                                elif count_locid1 > 1:
                                    print("File contain duplications of queryLocId1")
                                else:
                                    print("File contain duplications of queryLocId2")
            except FileNotFoundError:
                print("Invalid input file")
        else:
            print("Invalid radius")
    elif len(locIds) < 2:
        print("Missing locId1 and/or locId2")
    else:
        print("Invalid amount of input locId")

    if LDCount == [{} for i in range(len(locIds))]:
        LDCount = [{None} for i in range(2)]
    if simScore == 0.0:
        simScore = None
    if DCommon == {}:
        DCommon = {None}
    if LDClose == [{} for i in range(len(locIds))]:
        LDClose = [{None} for i in range(2)]

    return LDCount, simScore, DCommon, LDClose