import couchdb
import json

server = couchdb.Server('http://127.0.0.1:5984/')
#db = server.create('tweets')
db = server['tweets']
tweet ={"city":"melbourne","income":30000}
tweet2 = {"city": "geelong", "income": 23000}
tweets3 = {"city": "score", "income": 10000}

db.save(tweet2)
db.save(tweets3)

