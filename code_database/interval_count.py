import couchdb
import json
import couchdb.design
import inflection

server = couchdb.Server('http://127.0.0.1:5984/')
db = server["user_test"]
crimes = db.view('get_sen_count/get_sen_and_drink')
result = {}
result["[-1,-0.75]"] = 0
result["[-0.75,-0.50]"] = 0
result["[-0.50,-0.25]"] = 0
result["[-0.25,0]"] = 0
result["[0,0.25]"] = 0
result["[0.25,0.50]"] = 0
result["[0.50,0.75]"] = 0
result["[0.75,1.0]"] = 0


for crime_count in crimes:
    range = crime_count.value
    print(range)
    if(range>=-1  and range<-0.75):
        result["[-1,-0.75]"] += 1
    elif (range >= -0.75 and range < -0.50):
        result["[-0.75,-0.50]"] += 1
    elif (range >= -0.50 and range < -0.25):
        result["[-0.75,-0.50]"] += 1
    elif (range >= -0.25 and range < 0):
        result["[-0.25,0]"] += 1
    elif (range >= 0 and range < 0.25):
        result["[0,0.25]"] += 1
    elif (range >= 0.25 and range < 0.50):
        result["[0.25,0.5]"] += 1
    elif (range >= 0.50 and range < 0.75):
        result["[0.50,0.75"] += 1
    else:
        result["[0.75,1.0]"] += 1

    print(result)





