from web import app
from flask import render_template
from web import db,db_income,db_map,db_crime
from flask import jsonify

import json

#def __cols(pairs=[]):
#    return map(lambda x: {'id': '', 'label': x[0], 'type': x[1]}, pairs)


@app.route('/')
def home_page():
    return render_template('frontEndPage_2.html')

@app.route('/hello')
def home_page1():
    return render_template('hello.html')






@app.route('/get_income_data')
def ret_income_data():
    dict = {}
    counter=0
    tweet_sum = db_income.view('get_income/total_income',)
    for row in tweet_sum:
        str = row.value.split('(')
        dict[row.key] = str[0]
        if counter==9:
            break
        counter +=1
    print(dict)
    return jsonify(dict)

@app.route('/get_crime_data')
def ret_crime_data():
    dict = {}
    tweet_sum = db_crime.view('crime/crime_search', group=True)
    for row in tweet_sum:
        # dict[row.key] = row.value
        string1 = row.key[0].split('(')
        print(string1)
        dict[string1[0]] = row.value
    print(dict)
    return jsonify(dict)



@app.route('/get_alcohol_time')
def ret_alcohol_time():
    dict ={}
    res = db.view('get_sen_count/week_count', group=True)
    for row in res:
        dict[row.key] = row.value
    return jsonify(dict)




@app.route('/get_senti_data')
def ret_sentidata():
    dict = {}

    sums = db.view('get_sen_count/get_sen_sum', group=True)
    counts = db.view('get_sen_count/get_sen', group=True)
    for sum_sen in sums:
        num = sum_sen.value
        name = sum_sen.key
        for count_city in counts:
            num1 = count_city.value
            mean = num / num1
            if name is not None:
                dict[name] = mean

    return jsonify(dict)



@app.route('/get_alchohol_data')
def ret_alchohol_time():
    dict = {}
    res = db.view('get_sen_count/week_count', group=True)
    for row in res:
        dict[row.key] = row.value

    return jsonify(dict)


@app.route('/get_alchohol_income')
def ret_alcohol_income():
    tweet_dict = {}
    income_dict = {}
    result_dict = {}

    tweet_res = db.view('get_sen_count/drink_count_C', group=True)
    income_res = db_income.view('get_income/total_income')

    for row in tweet_res:
        tweet_dict[row.key] = row.value

    for row in income_res:
        city = row.value.split('(')
        income_dict[city[0]] = row.key

    for tweet_item in tweet_dict:
        for income_item in income_dict:
            if tweet_item is not None and income_item is not None:
                if tweet_item in income_item or income_item in tweet_item:
                    data_list = [tweet_dict[tweet_item], income_dict[income_item]]
                    result_dict[tweet_item] = data_list

    return jsonify(result_dict)

@app.route('/get_alcohol_senti')
def ret_alcohol_senti():
    result = {}
    data = db.view('get_sen_count/get_sen_and_drink')

    result["[-1,-0.75]"] = 0
    result["[-0.75,-0.50]"] = 0
    result["[-0.50,-0.25]"] = 0
    result["[-0.25,0]"] = 0
    result["[0,0.25]"] = 0
    result["[0.25,0.50]"] = 0
    result["[0.50,0.75]"] = 0
    result["[0.75,1.0]"] = 0

    for crime_count in data:
        range = crime_count.value
        if (range >= -1 and range < -0.75):
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
            result["[0.25,0.50]"] += 1
        elif (range >= 0.50 and range < 0.75):
            result["[0.50,0.75]"] += 1
        else:
            result["[0.75,1.0]"] += 1
    print(result)
    return jsonify(result)


@app.route('/get_marker')
def ret_alcohol_marker():
    i = 0
    dict = {}
    tweet_sum = db_map.view('lga_map/lga_geo_data')
    for row in tweet_sum:
        dict[i] = row.value[1][0][0][0]
        i = i + 1
    return jsonify(dict)


@app.route('/get_alcohol_crime')
def ret_alcohol_crime():
    tweet_dict = {}
    crime_dict = {}
    result_dict = {}

    tweet_res = db.view('get_sen_count/drink_count_C', group=True)
    crime_res = db_crime.view('crime/crime_search', group=True)

    for row in crime_res:
        city_name = row.key[0].split('(')[0]
        crime_dict[city_name] = row.value

    for row in tweet_res:
        if row.key is not None:
            tweet_dict[row.key] = row.value

    for tweet_item in tweet_dict:
        for income_item in crime_dict:
            if tweet_item is not None and income_item is not None:
                if tweet_item in income_item or income_item in tweet_item:
                    data_list = [tweet_dict[tweet_item], crime_dict[income_item]]
                    result_dict[tweet_item] = data_list

    return jsonify(result_dict)


def filter_city(db, results):
    final_results = {}

    for item in results:
        if item is not None:
            city_name = item.upper()
            for row in db.view('lga_map/lga_map_cities',group=True):
                if row.key.find(city_name) != -1:
                    final_results[item] = results[item]
    return final_results






''''@app.route('/get_income_map')
def ret_income_map():
    string_data=''
    income_sum = db_income.view('get_income/total_income')
    geo_map = db_map.view('lga_map/lga_geo_data')
    for item in income_sum:
        geojson_data = {
            "type": "Feature",
            "geometry": {
                "type": None,
                "coordinates": None
            },
            "properties": {
                "name": None,
                "value": None
            }
        }
        item_value = item.value.split('(')
        geojson_data["properties"]["name"] = item_value[0]
        geojson_data["properties"]["value"] = item.key
        for row in geo_map:
            if item_value[0].upper() in row.key:
                geojson_data["geometry"]["type"]=row.value[0]
                geojson_data["geometry"]["coordinates"] = row.value[1]
        result = str(geojson_data)
        string_data += result

    geojson_data_2 = {
        "type": "FeatureCollection",
        "features": str
    }

    ret_data=json.dumps(geojson_data_2)
    print(type(ret_data))
    return ret_data



'''

# crime data for chart
''''@app.route('/get_crime_data')
def ret_crime_data():
   result = db.view('get_income/total_income')
   for row in result:

     

    return jsonify(response)



@app.route('/sentiment_data')
def ret_alcohol_time():
    result = db.view('my_design/name1')
    dict = {}
    for row in result:
    
'''