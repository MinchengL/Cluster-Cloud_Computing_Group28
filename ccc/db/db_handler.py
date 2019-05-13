import couchdb
import json

server = couchdb.Server('http://127.0.0.1:5984/')
#db = server.create('tweets')
db = server['tweets']


tweets4 = {"city": "score", "income": 20000}

db.save(tweets4)