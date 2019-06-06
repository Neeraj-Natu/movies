from flask import Flask
import json
import pandas as pd
from flask import request
import sys


app = Flask(__name__)


@app.route('/') 
def rediness_check():
    
    return "200";

@app.route('/movies/popularity', methods=['GET']) 
def movie_details():
    title = request.args.get('title');
    movies = pd.read_csv('movie_details.csv');
    
    if (title is not None):
        movies.set_index('title',inplace=True)
        response = movies.loc[title,:];
        response['popularity'] = pd.to_numeric(response['popularity']);
        popularity = {'popularity' : response['popularity'].mean()};

        return json.dumps(popularity);

    else :
        return "no title found"


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=80)

