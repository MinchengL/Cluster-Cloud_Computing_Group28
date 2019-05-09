import couchdb
import json
import couchdb.design
import inflection

server = couchdb.Server('http://127.0.0.1:5984/')
db = server["user_test"]
tweets = db.view('get_sen_count/tweet_sum',group = True)
drinks = db.view('get_sen_count/drink_count_C',group = True)
results = {}

for tweets_count in tweets:
    name = tweets_count.key
    num = tweets_count.value
    #print(num)
    for drinks_C in drinks:
        num1 = drinks_C.value
        percentage = num1/num
        results[name] = percentage
print(results)



