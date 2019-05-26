from flask import Flask
import json
import pandas as pd
from flask import request



app = Flask(__name__)


@app.route('/') 
def rediness_check():
    
    return "200";

@app.route('/info/revenues', methods=['GET']) 
def movie_details():
    title = request.args.get('title');
    movies = pd.read_csv('movie_details.csv');
    
    if (title is not None):
        movies.set_index('title',inplace=True)
        response = movies.loc[title,:];
        revenue = {'revenue' : response['revenue'].max()};

        return json.dumps(revenue);
    else :
        return "no title found"


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=80)

