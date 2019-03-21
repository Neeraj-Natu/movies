from flask import Flask
import json
import pandas as pd
import numpy as np


app = Flask(__name__)



@app.route("/movies")
def details():
    details = pd.read_csv('movie_details.csv');    
    return details.to_string(index=False)



if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5005)

