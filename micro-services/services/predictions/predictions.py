from flask import Flask
import json
import pandas as pd
from flask import request
import random



app = Flask(__name__)


@app.route('/') 
def rediness_check():
    
    return "200";

@app.route('/movies/boxoffice', methods=['GET']) 
def movie_details():
    title = request.args.get('title');
        
    if (title is not None):
        random.seed(10);
        response = random.choice(['Blockbuster','Average','Poor']);
        return str(response);
    else:
        return "title not found"

        
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=80)

