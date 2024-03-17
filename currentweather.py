# currentweather.py - Topic 2 Assignment 
# Author: Rebecca Feeley

# Program which prints out the current temperature on the console


# import the required modules

import requests
import json

url = "https://api.open-meteo.com/v1/forecast?latitude=53.82&longitude=-9.5&current=temperature_2m,wind_speed_10m"

# New coordinates of my location
new_latitude = 54.27
new_longitude = -8.47

# Updating the URL with the new coordinates
url = f"https://api.open-meteo.com/v1/forecast?latitude={new_latitude}&longitude={new_longitude}&current=temperature_2m,wind_speed_10m"

# to obtain the contents of the above web page

response = requests.get(url)
#print(response.json()) # commented out for clarity

data = response.json() # converting the response obtained to a json dictionary

temperature = data['current']['temperature_2m']
temp_units = data['current_units']['temperature_2m']
print(f"The current air temperature at my co-ordinates at 2m above the ground is {temperature}{temp_units}")


# Program which prints out the current wind direction (10m) on the console

url2 = "https://api.open-meteo.com/v1/forecast?latitude=54.2697&longitude=-8.4694&current=wind_direction_10m"

response2 = requests.get(url2)
# to obtain the info from the above webpage

data2 = response2.json()

wind_direction = data2['current']['wind_direction_10m']
wind_direction_unit = data2['current_units']['wind_direction_10m'] # to obtain the unit wind direction is displayed in

# Printing the current wind direction 
print (f"The current wind direction is: {wind_direction}{wind_direction_unit}")