from flask import Flask
from flask_cors import CORS
import couchdb
app = Flask(__name__)
CORS(app, supports_credentials=True)

def after(resp):
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Method'] = '*'
    resp.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return resp

app.after_request(after)
server = couchdb.Server('http://127.0.0.1:5984')
db = server['tweets_data']
db_income = server['income_data']
db_map = server['lga_map_data']
db_crime = server['crime_rate_data']