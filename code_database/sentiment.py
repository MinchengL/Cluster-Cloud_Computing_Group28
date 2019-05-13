import couchdb
import json
import couchdb.design
import inflection

server = couchdb.Server('http://127.0.0.1:5984/')
db = server["user_test"]
results = {}

counts = db.view('get_sen_count/get_sen',group = True)
sums = db.view('get_sen_count/get_sen_sum',group = True)
for sum_sen in sums:
    num = sum_sen.value
    name = sum_sen.key
    for count_city in counts:
        num1 = count_city.value
        mean = num/num1
    results[name] = mean
print(results)


