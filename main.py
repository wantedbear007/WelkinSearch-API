from flask import Flask, request
from flask_restful import Resource, Api
# from .Utilities import search 
# from utils.search import Search
from utils.drive_files_data import DriveData
from utils.search import search_results
# from utils import search, drive_files_data
# from search_results import search_results
# from archive_details import archive_details


app = Flask(__name__)
api = Api(app)

# print(Search.search_keyword("movies"))


class SearchKeyword(Resource):
    def get(self, keywords):
        search_result = search_results(keywords)
        # print(search_result)
        # search_result = search_results(keywords=keywords)
        return search_result, 200

    
class GetDriveFiles(Resource):
    def post(self):
        data = request.get_json()
        archive_data = DriveData.drive_details(data["link"])
        # z = archive_details(data["link"])
        return archive_data, 200


api.add_resource(SearchKeyword, '/search/<string:keywords>')
api.add_resource(GetDriveFiles, '/drive', endpoint = 'drive')

if "__main__" == __name__:
    # app.run()
    app.run(debug=True)
