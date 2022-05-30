from flask import Flask, request
from flask_restful import Resource, Api
from search_results import search_results
from archive_details import archive_details


app = Flask(__name__)
api = Api(app)

class search(Resource):
    def get(self, keywords):
        search_result = search_results(keywords=keywords)
        return search_result, 200

    
class drive_details(Resource):
    def post(self):
        data = request.get_json()
        z = archive_details(data["link"])
        return z, 200


api.add_resource(search, '/search/<string:keywords>')
api.add_resource(drive_details, '/drive', endpoint = 'drive')

if "__main__" == __name__:
    app.run()
    # app.run(debug=True)
