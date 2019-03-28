from flask import Flask
import json
import pandas as pd
from flask import request
import random



app = Flask(__name__)



@app.route('/predictions', methods=['GET']) 
def movie_details():
    title = request.args.get('title');
    
    if (title is not None):
        response = random.choice(['Blockbuster','Average','Poor']);
        return str(response);


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)

