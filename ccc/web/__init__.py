#This file is developed by Team 28 of COMP90024 of The University of Melbourne
#YING DU : 925566
#XINHUI LU : 965246
#MINCHENG LI : 889903
#MIAN WANG : 948291
#MINGZE XIA : 548737


from flask import Flask
import couchdb
app = Flask(__name__)

server = couchdb.Server('http://127.0.0.1:5984')
db = server['tweets_data']
db_income = server['income_data']
db_map = server['lga_map_data']
db_crime = server['crime_rate_data']