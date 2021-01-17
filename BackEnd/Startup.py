import spotipy
from spotipy import client
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials


class SpotipyClient:

    _instace = None

    def __init__(self, client_id, client_secret, redirect_url, username, scope):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_url = redirect_url
        self.scope = scope
        self.username = username

        client_credentials_maneger = SpotifyClientCredentials(
            client_secret=self.client_secret, client_id=self.client_id)
        token = util.prompt_for_user_token(
            self.username, self.scope, self.client_id, self.client_secret, self.redirect_url)
        self.sp = spotipy.Spotify(auth=token)

    @classmethod
    def instance(cls, client_id, client_secret, redirect_url, username, scope):
        if cls._instace is None:
            cls._instace = cls(client_id, client_secret,
                               redirect_url, username, scope)
        return cls._instace
