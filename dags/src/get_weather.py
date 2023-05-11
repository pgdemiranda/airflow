import requests
import os
from datetime import datetime
import json

# API params
url = "https://weatherapi-com.p.rapidapi.com/current.json"

querystring = {"q":"London"}

headers = {
	"X-RapidAPI-Key": "a48f29529dmshd13e41e171bbb50p140fe5jsnf78a86423555",
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

if response.status_code==200:
    # get data
    json_data = response.json()
    filename = str(datetime.now().date()) + '.json'
    
    tot_name = os.path.join(os.path.dirname(__file__), 'data', filename)
    
    with open(tot_name, 'w') as outputfile:
        json.dump(json_data, outputfile)

else:
    print(response.status_code)
    print("Error in API call")

# print(response.json())
# print(response)