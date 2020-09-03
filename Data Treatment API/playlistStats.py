import spotipy
import spotipy.util as util
import numpy as np
import matplotlib.pyplot as plt
import json
import config
from spotipy.oauth2 import SpotifyClientCredentials


class PlaylistStats:

    def __init__(self, client_id, client_secret, playlist_id, redirect_uri='http://google.com/', username='22qgar7duksytos2kcf7znuca', scope='user-library-read playlist-read-private'):
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
        try:
            token = util.prompt_for_user_token(
                self.username, self.scope, client_id=self.client_id, client_secret=self.client_secret, redirect_uri=self.redirect_uri)
            self.sp = spotipy.Spotify(auth=token)
        except:
            print('Token is not accesible for ' + username)

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

    def meanStatisticsPlot(self, processed_playlist, wanted_statistics):
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

    def keyDistribution(self):
        keys = list()
        for track in processed_playlist:
            keys.append(track[0]['key'])
        keys.sort()
        counted_keys = Counter(keys)
        return counted_keys

    def meanStatistics(self):
        means = dict()

        for metric in wanted_statistics:
            sup = list()
            for track in processed_playlist:
                sup.append(track[0][metric])
            means[metric] = np.mean(sup)
            return means


def runPlaylistKeys(app):
    play = app.getPlaylistTracks()
    processed_playlist = app.processData(play)
    playlist_Alalysis = list()
    for track in processed_playlist:
        playlist_Alalysis.append([app.trackAnalysis(track)])
    return app.keyDistribution(playlist_Alalysis)


# spotify:playlist:6EKo3FtKEaoLgNSX8jptsy - hollow knigth
# spotify:playlist:5qezJrYrhycL3FVyyRCjGa -Jul/Aug
'''
if __name__ == '__main__':
    credentials = config.getCredentials()
    app = PlaylistStats(
        client_id=credentials[0], client_secret=credentials[1], playlist_id='5qezJrYrhycL3FVyyRCjGa')

    play = app.getPlaylistTracks()
    processed_playlist = app.processData(play)
    playlist_Alalysis = list()

    for track in processed_playlist:
        playlist_Alalysis.append([app.trackAnalysis(track)])

    wanted_statistics = ('acousticness', 'danceability', 'energy', 'instrumentalness',
                         'liveness', 'speechiness', 'valence')

    app.meanStatistics(playlist_Alalysis, wanted_statistics)
'''
