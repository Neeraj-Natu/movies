from flask import Flask
import json
import pandas as pd
from flask import request
import requests




app = Flask(__name__)



@app.route('/') 
def rediness_check():
    
    return "200";
    



@app.route('/movie-details', methods=['POST']) 
def movie_details():
    content = request.get_json();
    title = content['title'];

    movie_service = "http://movies.default.svc.cluster.local:80/movies";
    popularity_service = "http://popularity.default.svc.cluster.local:80/popularity";
    revenue_service = "http://revenue.default.svc.cluster.local:80/revenues";

    
    if (title is not None):
        
        query_param = {'title':title};
        movie_response = requests.get(movie_service, params=query_param).json();
        popularity_response = requests.get(popularity_service, params=query_param).json();
        revenue_response = requests.get(revenue_service, params=query_param).json();
        
        ## merging the responses remains to do 
        #movie_response.update(popularity_response);
        #movie_response.update(revenue_response);


        return json.dumps(movie_response);
    
    else :
        return "title not found"


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=80)

