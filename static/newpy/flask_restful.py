#!/usr/bin/env python
from flask import Flask
from flask_restful import Resource, Api
from flask_restful.reqparse import RequestParser
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

class Baz(Resource):
    def put(self):
        parser = RequestParser()
        parser.add_argument('location', location='json', required=True)
        params = parser.parse_args()
        return params['location']

api = Api(app)
api.add_resource(Baz, '/baz', endpoint='api_baz')

if __name__ == '__main__':
    app.run(debug=True)
