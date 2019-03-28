from flask import Flask
import json
import pandas as pd
from flask import request



app = Flask(__name__)



@app.route('/ratings', methods=['GET']) 
def movie_ratings():
    movieId = request.args.get('movieId');
    movies = pd.read_csv('ratings_small.csv');

    if (movieId is not None):

        movies.set_index('movieId',inplace=True)
        response = movies.loc[int(movieId),:];
        return str(response);
        
    else:
        return "movieId not found"
                



if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8092)

