from flask import Flask
import couchdb
app = Flask(__name__)

server = couchdb.Server('http://127.0.0.1:5984')
db = server['tweets_data']
db_income = server['income_data']
db_map = server['lga_map_data']
db_crime = server['crime_rate_data']