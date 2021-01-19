from typing import Counter
import numpy as np
from PLalistTools import PlaylistDecomposer


class PlaylistAnalizer:

    def __init__(self, client):
        if client is None:
            raise Exception('No Spotipy client privided')

        self.client = client

    def metricStatistics(self, metrics, playlist_id):
        tools = PlaylistDecomposer(self.client)
        means = dict()
        playlist = tools.getPlaylistTracks(playlist_id)

        for metric in metrics:
            sup = list()
            for track in playlist:
                sup.append(track[0][metric])
            means[metric] = np.mean(sup)
        return means

    def keyDIstribution(self, playlist_id):
        keys = list()
        tools = PlaylistDecomposer(self.client)
        processed_playlist = tools.getPlaylistTracks(playlist_id)

        for track in processed_playlist:
            keys.append(tarck[0]['key'])
        keys.sort()
        counted_keys = Counter(keys)

        return counted_keys
