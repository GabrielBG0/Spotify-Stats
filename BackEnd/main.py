from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {"data": "Hello Wolrd"}


api.add_resource(HelloWorld, "/HelloWorld")

if __name__ == '__main__':
    app.run(debug=True)
