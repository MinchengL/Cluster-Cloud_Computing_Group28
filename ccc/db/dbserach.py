import couchdb

server = couchdb.Server('http://127.0.0.1:5984/')
db = server['tweets']


result = db.view('_design/get_income')
print(result)


