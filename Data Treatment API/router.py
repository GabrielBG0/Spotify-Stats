from flask import Flask
from flask_restful import Api, Resource
from playlistStatsEP import PlaylistStatsEP

app = Flask(__name__)
api = Api(app)


api.add_resource(PlaylistStatsEP, "/plStats")

if __name__ == '__main__':
    app.run(debug=True)
