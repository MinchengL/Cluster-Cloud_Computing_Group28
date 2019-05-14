#This file is developed by Team 28 of COMP90024 of The University of Melbourne
#YING DU : 925566
#XINHUI LU : 965246
#MINCHENG LI : 889903
#MIAN WANG : 948291
#MINGZE XIA : 948737

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
    final_results = {}

    sums = db.view('get_sen_count/get_sen_sum', group=True)
    counts = db.view('get_sen_count/get_sen', group=True)
    for sum_sen in sums:
        num = sum_sen.value
        sums_name = sum_sen.key
        for count_city in counts:
            num1 = count_city.value
            count_name = count_city.key
            if count_name == sums_name:
                dict[count_name] = num/num1
            else:
                continue
    final_results = filter_city(db_map,dict)
    return jsonify(final_results)

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
            result["[-0.50,-0.25]"] += 1
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
    tweet_sum = db.view('get_sen_count/isalco_coor')
    for row in tweet_sum:
        if row.value[0] is not None:
            dict[i] = row.value
            i = i + 1
    print(dict)
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

