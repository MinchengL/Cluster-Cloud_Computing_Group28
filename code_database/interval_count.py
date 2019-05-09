import couchdb
import json
import couchdb.design
import inflection

server = couchdb.Server('http://127.0.0.1:5984/')
db = server["user_test"]
crimes = db.view('get_sen_count/get_sen_and_drink')



for crime_count in crimes:
    range = crime_count.value
    print(range)
    if(range>=-1  and range<-0.75):
        #print(range)
        result1 = {}
        for count_drink in crimes:
            i = i+1
            result1["[-1,-0.75]"] = i
        print(result1)
    else:
        print("interval[-1,-0.75] have no data")
    if (range >= -0.75 and range < -0.50):
        #print(range)
        result2 = {}
        for count_drink in crimes:
            j = j+1
            result2["[-0.75,-0.50]"] = j
        print(result2)
    else:
        print("interval[-0.75,-0.50] have no data")
    if (range >= -0.50 and range < -0.25):
        #print(range)
        result3 = {}
        for count_drink in crimes:
            k = k+1
            result3["[-0.75,-0.50]"] = k
        print(result3)
    else:
        print("interval[-0.50,-0.25] have no data")
    if (range >= -0.25 and range < 0):
        #print(range)
        result4 = {}
        for count_drink in crimes:
            a = a+1
            result4["[-0.25,0]"] = a
        print(result4)
    else:
        print("interval[-0.25,0] have no data")
    if (range >= 0 and range < 0.25):
        #print(range)
        result5 = {}
        for count_drink in crimes:
            b = b+1
            result5["[0,0.25]"] = b
        print(result5)
    else:
        print("interval[0,0.25] have no data")
    if (range >= 0.25 and range < 0.50):
        #print(range)
        result6 = {}
        for count_drink in crimes:
            c = c+1
            result6["[0.25,0.5]"] = c
        print(result6)
    else:
        print("interval[0.25,0.5] have no data")
    if (range >= 0.50 and range < 0.75):
        #print(range)
        result7 = {}
        for count_drink in crimes:
            e = e+1
            result7["[0.50,0.75"] = e
        print(result7)
    else:
        print("interval[0.50,0.75] have no data")
    if (range >= 0.75 and range < 1.0):
       # print(range)
        result8 = {}
        for count_drink in crimes:
            g = g+1
            result8["[0.75,1.0]"] = g
        print(result8)
    else:
        print("interval[0.75,1.0] have no data")






