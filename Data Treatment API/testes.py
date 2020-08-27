import spotipy
import numpy as np
import matplotlib.pyplot as plt
import startup
import playlistStats
import json
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
import config

credentials = config.getCredentials()
client_id = credentials[0]
client_secret = credentials[1]
playlist_id = '5qezJrYrhycL3FVyyRCjGa'
redirect_uri = 'http://google.com/'
username = '22qgar7duksytos2kcf7znuca'
scope = 'user-library-read playlist-read-private'

client_credentials_manager = SpotifyClientCredentials(
    client_id=client_id, client_secret=client_secret)

try:
    token = util.prompt_for_user_token(
        username, scope, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)
    sp = spotipy.Spotify(auth=token)
except:
    print('Token is not accesible for ' + username)


print(sp.playlist_tracks(
    playlist_id))
