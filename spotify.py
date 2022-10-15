from contextlib import nullcontext
from flask import Blueprint, jsonify  # jsonify creates an endpoint response object
from flask_restful import Api, Resource # used for REST API building
import requests  # used for testing 
import time

# Blueprints enable python code to be organized in multiple files and directories https://flask.palletsprojects.com/en/2.2.x/blueprints/
spotify_api = Blueprint('spotify_api', __name__,
                   url_prefix='/api/spotify')

# API generator https://flask-restful.readthedocs.io/en/latest/api.html#id1
api = Api(spotify_api)


def getSpotifyAPI():
    global spotify_data  # the covid_data global is preserved between calls to function
    try: spotify_data
    except: spotify_data = None

    """
    Preserve Service usage / speed time with a Reasonable refresh delay
    """
    if updateItem(): # request Spotify data
	querystring = {"q":"<REQUIRED>","type":"multi","offset":"0","limit":"10","numberOfTopResults":"5"}
        url = "https://spotify23.p.rapidapi.com/search/"
	headers = {
		"X-RapidAPI-Key": "45de2811f2mshc93a1328afeb302p1ee42bjsnbde76995c6f3",
		"X-RapidAPI-Host": "spotify23.p.rapidapi.com"
	}
        response = requests.request("GET", url, headers=headers, params=querystring)
        spotify_data = response
    else:  # Request Covid Data
        response = spotify_data

    return response
