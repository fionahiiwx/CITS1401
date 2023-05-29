#### JSON ####
#import csv
#import json

#def csv_to_json(csvFilePath, jsonFilePath):
#    jsonArray = []

    # read csv file
#    with open(csvFilePath, encoding='utf-8') as csvf:
#        # load csv file data using csv library's dictionary reader
#        csvReader = csv.DictReader(csvf)

        # convert each csv row into python dict
#        for row in csvReader:
            # add this python dict to json array
#            jsonArray.append(row)

    # convert python jsonArray to JSON String and write to file
#    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
#        jsonString = json.dumps(jsonArray, indent=4)
#        jsonf.write(jsonString)


#csvFilePath = r'Locations-sample-Project1.csv'
#jsonFilePath = r'Project1FileJson.json'
#csv_to_json(csvFilePath, jsonFilePath)

#### PARQUET ####
#import pandas as pd

#def write_parquet_file():
#    df = pd.read_csv('Locations-sample-Project1.csv')
#    df.to_parquet('Project1PARQUET')
#write_parquet_file()

#import pandas as pd
#df = pd.read_csv('Locations-sample-Project1.csv')
#df.to_parquet('Project1PARQUET.parquet')

#### ARVO ####

import json

with open('Project1JSON.json') as file:
  db = json.load(file)

print(db)