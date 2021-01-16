

class PlaylistDecomposer:
    def __init__(self, sp):
        self.sp

    def getPlaylistTracks(self, playlist_id):
        playlistTracks = self.sp.playlist_tracks(
            self.playlist_id, fields='items.track(name, id)')

        playlist_processed = list()
        for x, y in playlistTracks.items():
            for a in y:
                for v, i in a.items():
                    playlist_processed.append(i)
        return playlist_processed
