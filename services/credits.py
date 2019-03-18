import pandas as pd
import json
from flask import Flask
from flask import request


app = Flask(__name__)

@app.route("/credits", methods = ['GET'])
def credits():
    
    creditdb = pd.read_csv('../database/credits.csv');
    
    
    credit_json = creditdb.to_json(orient='records');
    

    return json.dumps(credit_json);
