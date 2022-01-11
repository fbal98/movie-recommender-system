from Recommendation import Recommendation


from flask import Flask
from flask_restful import Api, Resource
import json
import pickle
app = Flask(__name__)
api = Api(app)

class GetRecommendationEndPoint(Resource):
    def post(self, favMovie):

        if favMovie is None:
            raise ValueError
            return favMovie
        else:
            r = Recommendation()
            recommendation = r.make_recommendation(favMovie)
            if recommendation is None:
                return {'data': 'couldn\'t find recommendation'}
            else:
                return {"data": recommendation}




api.add_resource(GetRecommendationEndPoint, '/recommend/<favMovie>')
if __name__ == "__main__":
    app.run(debug=True)






