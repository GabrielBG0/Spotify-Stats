import requests
import json

BASE = "http://127.0.0.1:5000/"

data = {"data": ('acousticness', 'danceability', 'energy', 'instrumentalness',
                 'liveness', 'speechiness', 'valence')}

response = requests.get(BASE + "plstats")
print(response.json())
