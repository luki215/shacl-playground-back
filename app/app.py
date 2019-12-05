# app.py - a minimal flask api using flask_restful
from flask import Flask
from flask_restful import Resource, Api, reqparse
import werkzeug
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=['http://localhost:4200'])
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}
    def post(self):
        parse = reqparse.RequestParser()
        parse.add_argument('shacl_file', type=werkzeug.datastructures.FileStorage, location='files')
        parse.add_argument('turtle_file', type=werkzeug.datastructures.FileStorage, location='files')
        args = parse.parse_args()
        shaclFile = args['shacl_file']
        shaclFile.save("shacl_file")
        turtleFile = args['turtle_file']
        turtleFile.save("turtle_file")

        return {'ok': True}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')