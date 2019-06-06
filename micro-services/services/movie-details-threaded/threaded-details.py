from flask import Flask
import json
import pandas as pd
from flask import request
import requests




app = Flask(__name__)



@app.route('/') 
def rediness_check():
    
    return "200";
    



@app.route('/info/details', methods=['POST']) 
def movie_details():
    content = request.get_json();
    title = content['title'];

    popularity_service = "http://popularity.default.svc.cluster.local:80/info/popularity";
    revenue_service = "http://revenues.default.svc.cluster.local:80/info/revenues";
    budget_service = "http://budget.default.svc.cluster.local:80/info/budget";

    
    if (title is not None):
        
        query_param = {'title':title};
        budget_response = requests.get(budget_service, params=query_param).json();
        popularity_response = requests.get(popularity_service, params=query_param).json();
        revenue_response = requests.get(revenue_service, params=query_param).json();
        
        budget_response.update(popularity_response);
        budget_response.update(revenue_response);


        return json.dumps(budget_response);
    
    else :
        return "title not found"


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=80)

