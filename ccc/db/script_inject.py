import json

import couchdb

server = couchdb.Server('http://127.0.0.1:5984/')
db = server['tweets']

with open('get_income.json', 'r') as f:
    db.save(json.load(f))