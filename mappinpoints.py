# !flask/bin/python 

import sys

from flask import Flask, render_template, request, redirect, Response
import random, json
from urllib.request import urlopen
import requests

def read(latitude,longitude):
    url = 'https://maps.googleapis.com/maps/api/geocode/json?latlng={},{}&key=AIzaSyBW5QZVpvnxWPcemecQBxhxZrjPjxB2bXU'.format(latitude, longitude)

    json_data = requests.get(url).json()
    place = json_data['results'][0]['formatted_address']
    return place

import csv_reader 

def latlong(dictionary, truckID):
    result = []
    # for i in range(len(dictionary[truckID][7])):
    # for i in range(150):
    latitude = dictionary[truckID][7][2]
    longitude = dictionary[truckID][8][2]
    val = read(latitude, longitude)
        # seen = set(result)
        # if val not in seen:
            # seen.add(val)
            # result.append(val)
    # latlon = [val, latitude, longitude]
    # result.append(latlon)
    # print(result)
    result = [latitude, longitude]
    return result

# latlong(csv_reader.readMyFile('ITM_20190121.csv'), '1084067241')
app = Flask(__name__)

@app.route('/map2.html')
def output():
	# serve index template
    place = latlong(csv_reader.readMyFile('ITM_20190121.csv'), '1084067241')
    return render_template('map.html', address2 = place)

if __name__ == '__main__':
	# run!
	app.run()

