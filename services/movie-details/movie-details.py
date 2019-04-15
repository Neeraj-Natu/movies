from flask import Flask
import json
import pandas as pd
from flask import request
import requests



app = Flask(__name__)



@app.route('/movie-details', methods=['POST']) 
def movie_details():
    content = request.get_json();
    title = content['title'];

    prediction_service = "http://predictions:9004/predictions";
    movie_service = "http://movies:9002/movies";
    rating_service = "http://ratings:9003/ratings";

    
    if (title is not None):
        
        # code goes here
        query_param = {'title':title};
        movie_response = requests.get(movie_service, params=query_param).json();


        return str(movie_response.to_dict());
    else :
        return "title not found"


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=9001)

