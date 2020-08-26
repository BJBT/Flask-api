from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Quotes(Resource):
    def get(self):
        return {
            'name': 'Blayne',
            'age': 21,
            'Hapiness Rating': 8.2
        }

api.add_resource(Quotes, '/')

if __name__ == '__main__':
    app.run(debug=True)