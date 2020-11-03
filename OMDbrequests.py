"""
API Key: http://www.omdbapi.com/?i=tt3896198&apikey=cd71e660
"""

import requests
import json
import csv

movie_dict = {}
with open('movie_titles_vCorta.csv') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    next(spamreader, None)
    for row in spamreader:
        param = {
            'y': str(row[1]),
            't': str(row[2])
        }
        response = requests.get("http://www.omdbapi.com/?i=tt3896198&apikey=cd71e660",params=param)
        movieInfo = response.json()
        movie_dict[row[0]] = movieInfo
    with open('movieExtraInfo.json',mode='w') as jsonfile:
        json.dump(movie_dict, jsonfile, indent=4)
"""

response = requests.get("http://www.omdbapi.com/?i=tt3896198&apikey=cd71e660",params=param)

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

print(type(response.json()))
"""