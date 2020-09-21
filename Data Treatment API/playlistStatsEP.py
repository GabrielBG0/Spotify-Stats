import config
import playlistStats
from playlistStats import PlaylistStats
from flask_restful import reqparse, abort
from flask.views import MethodView


credentials = config.getCredentials()

analysis_mean = reqparse.RequestParser()
analysis_mean.add_argument("wanted_statistics", type=dict,
                           required=True, help="list of wanted statistics is needed")


class PlaylistStatsEP(MethodView):
    def get(self, playlist_id):
        pls = PlaylistStats(credentials[0], credentials[1], playlist_id)
        respose = playlistStats.runPlaylistKeys(pls)

        return respose
