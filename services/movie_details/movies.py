from flask import Flask
import json
import pandas as pd
import numpy as np


app = Flask(__name__)

details = pd.read_csv('movie_details.csv');

@app.route("/movies")
def details():
    
    return details.head().to_string



if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5005)

