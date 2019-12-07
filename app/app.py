# app.py - a minimal flask api using flask_restful
from flask import Flask
from flask_restful import Resource, Api, reqparse
import werkzeug
from flask_cors import CORS
from pyshacl import validate

app = Flask(__name__)
CORS(app)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}
    def post(self):
        parse = reqparse.RequestParser()
        parse.add_argument('shapes_file', type=werkzeug.datastructures.FileStorage, location='files')
        parse.add_argument('data_file', type=werkzeug.datastructures.FileStorage, location='files')
        args = parse.parse_args()
        shaclFile = args['shapes_file']
        shaclFile.save("tmp/shapes_file")
        turtleFile = args['data_file']
        turtleFile.save("tmp/data_file")

        r = validate("tmp/data_file", shacl_graph="tmp/shapes_file", data_graph_format="turtle", shacl_graph_format="turtle", debug=False)
        conforms, results_graph, results_text = r


        return {"conforms": conforms, "results_graph": str(results_graph.serialize(format="n3").decode("utf-8")), "results_text": results_text}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')