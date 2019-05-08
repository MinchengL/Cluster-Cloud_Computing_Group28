from flask import Flask
import couchdb
app = Flask(__name__)
server = couchdb.Server('http://127.0.0.1:5984')
db = server['tweets']
