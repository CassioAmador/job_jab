import os
import csv

import json 

def csv_to_json(csvFilePath=os.path.join(os.pardir, 'ofertas.csv'), jsonFilePath=os.path.join(os.pardir, 'ofertas.json')):
    jsonArray = []
      
    #read csv file
    with open(csvFilePath, encoding='utf-8') as csvf: 
        #load csv file data using csv library's dictionary reader
        csv_reader = csv.reader(csvf, delimiter=";")
        header = next(csv_reader)

        #convert each csv row into python dict
        job_id=0
        for row in csv_reader: 
            #add this python dict to json array
            jsonArray.append({"model":"job_search.job","pk":job_id,"fields": {"doc_id": row[0],
                        "employer_name": row[1],
                        "date_posted": row[2],
                        "employment_type": row[3],
                        "location": row[4],
                        "title": row[5],
                        "description": " ".join(row[6:])}})
            job_id+=1
  
    #convert python jsonArray to JSON String and write to file
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf: 
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)
          
csv_to_json()