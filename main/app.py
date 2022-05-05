from flask import Flask, request
from flask_restful import Resource, Api
from search_results import results_data

app = Flask(__name__)
api = Api(app)

class drive_results(Resource):
    def get(self, keywords):
        search_result = results_data(keywords=keywords)
        return search_result, 200

api.add_resource(drive_results, '/search_data/<string:keywords>')

if "__main__" == __name__:
    app.run(debug=True)
