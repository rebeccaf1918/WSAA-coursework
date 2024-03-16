# currentweather.py - Topic 2 Assignment 
# Author: Rebecca Feeley

# Program which prints out the current temperature on the console


# import the required modules

import requests
import json

url = "https://api.open-meteo.com/v1/forecast?latitude=53.82&longitude=-9.5&current=temperature_2m,wind_speed_10m"

# to obtain the contents of the above web page

response = requests.get(url)
#print(response.json())

data = response.json() # converting the response obtained to a json dictionary

temperature = data['current']['temperature_2m']
temp_units = data['current_units']['temperature_2m']
print(f"The current air temperature at the chosen co-ordinates at 2m above the ground is {temperature}{temp_units}")
