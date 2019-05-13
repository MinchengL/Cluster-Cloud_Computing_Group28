import couchdb

server = couchdb.Server('http://127.0.0.1:5984/')
db = server['tweets_data']
res = db.view('get_sen_count/get_sen', group= True)
for row in res:
    print(row)