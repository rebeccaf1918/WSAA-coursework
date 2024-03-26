# assignment03-cso.py - Topic 4 Assignment 
# Author: Rebecca Feeley

# Program which retrieves the dataset for the "exchequer account (historical series)" from the CSO
# and stores it in a file called "cso.json".


# import the required modules

import requests
import json

url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en"

# getting and extracting the data from the url
response = requests.get(url)
data = response.json()

# print(result)  commented out for clarity

with open("data.json", 'w') as file:  # opening a file in write mode to write the cso data to the file
    json.dump(data, file)

