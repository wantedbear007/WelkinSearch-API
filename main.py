from flask import Flask, request
from flask_restful import Resource, Api
from utils.drive_files_data import DriveData
from utils.search import search_results
from flask_cors import CORS


app = Flask(__name__)
api = Api(app)
CORS(app)



class SearchKeyword(Resource):
    def get(self, keywords):
        search_result = search_results(keywords)
        return search_result, 200

    
class GetDriveFiles(Resource):
    def post(self):
        data = request.get_json()
        archive_data = DriveData.drive_details(data["link"])
        return archive_data, 200


api.add_resource(SearchKeyword, '/search/<string:keywords>')
api.add_resource(GetDriveFiles, '/drive', endpoint = 'drive')

if "__main__" == __name__:
    from waitress import serve
    # app.run()
    serve(app, host="0.0.0.0")
    # app.run(debug=True)
