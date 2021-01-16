import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from decouple import config


class PlaylistStats:

    def __init__(self, client_id, client_secret, playlist_id, redirect_uri='https://google.com/', username='22qgar7duksytos2kcf7znuca', scope='user-library-read playlist-read-private'):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        # spotify:user:22qgar7duksytos2kcf7znuca
        self.username = username
        self.scope = scope
        self.sp = None
        self.playlist_id = playlist_id

        client_credentials_manager = SpotifyClientCredentials(
            client_id=self.client_id, client_secret=self.client_secret)
        token = util.prompt_for_user_token(
            self.username, self.scope, client_id=self.client_id, client_secret=self.client_secret, redirect_uri=self.redirect_uri)
        self.sp = spotipy.Spotify(auth=token)

    def getInfo(self):
        return {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "redirect_uri": self.redirect_uri,
            "username": self.username,
            "scope": self.scope
        }

    def getPlaylistTracks(self):
        playlistTracks = self.sp.playlist_tracks(
            self.playlist_id, fields='items.track(name, id)')
        return playlistTracks

    def showPlaylistTracks(self, playlist):
        for x, y in playlist.items():
            for a in y:
                for label, value in a.items():
                    print(value['name'])

    def processData(self, playlist_tracks):
        playlist_processed = list()
        for x, y in playlist_tracks.items():
            for a in y:
                for v, i in a.items():
                    playlist_processed.append(i)
        return playlist_processed

    def trackAnalysis(self, track):
        processedAnalysis = dict()
        analysis = self.sp.audio_features(track['id'])
        analysis[0]['name'] = track['name']
        processedAnalysis = dict(analysis[0])
        return processedAnalysis

    def keyDistributionPlot(self, processed_playlist):
        keys = list()
        for track in processed_playlist:
            keys.append(track[0]['key'])
        keys.sort()
        counted_keys = Counter(keys)

        plt.bar(range(len(counted_keys)), list(
            counted_keys.values()), align='center')
        plt.xticks(range(len(counted_keys)), list(counted_keys.keys()))
        plt.xlabel('Keys')
        plt.title('Playlist Keys')
        plt.show()

    def meanStatistics(self, processed_playlist, wanted_statistics):
        means = dict()

        for metric in wanted_statistics:
            sup = list()
            for track in processed_playlist:
                sup.append(track[0][metric])
            means[metric] = np.mean(sup)

        plt.bar(range(len(means)), list(means.values()), align='center')
        plt.xticks(range(len(means)), list(means.keys()))
        plt.xlabel('metrics')
        plt.title('metrics means')
        plt.ylim((0, 1))
        plt.show()


# spotify:playlist:7rE1I3V4XtVG2EiQJTX1GU - 2020
if __name__ == '__main__':
    app = PlaylistStats(
        client_id=config('SPOTIPY_CLIENT_ID'), client_secret=config('SPOTIPY_CLIENT_SECRET'), playlist_id='7rE1I3V4XtVG2EiQJTX1GU', redirect_uri=config('SPOTIPY_REDIRECT_URI'))

    playlist_tracks = app.getPlaylistTracks()

    processed_playlist = app.processData(playlist_tracks)

    playlist_Alalysis = list()

    for track in processed_playlist:
        playlist_Alalysis.append([app.trackAnalysis(track)])

    wanted_statistics = ('acousticness', 'danceability', 'energy', 'instrumentalness',
                         'liveness', 'speechiness', 'valence')

    app.meanStatistics(playlist_Alalysis, wanted_statistics)
    app.keyDistributionPlot(playlist_Alalysis)
