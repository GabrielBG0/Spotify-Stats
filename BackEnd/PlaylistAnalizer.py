from typing import Dict
from Startup import SpotipyClient
from decouple import config
import numpy as np
from PLalistTools import PlaylistDecomposer


class PlaylistAnalizer:

    def __init__(self, client):
        if client is None:
            raise Exception('No Spotipy client privided')

        self.client = client

    def metricStatistics(self, metrics):
        tools = PlaylistDecomposer(self.client)
        means = dict()
        playlist = tools.getPlaylistTracks()

        for metric in metrics:
            sup = list()
            for track in playlist:
                sup.append(track[0][metric])
            means[metric] = np.mean(sup)
        return means
