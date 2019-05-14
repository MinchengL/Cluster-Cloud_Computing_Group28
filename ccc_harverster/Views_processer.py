#This file is developed by Team 28 of COMP90024 of The University of Melbourne
#YING DU : 925566
#XINHUI LU : 965246
#MINCHENG LI : 889903
#MIAN WANG : 948291
#MINGZE XIA : 948737

import couchdb

def design_view_lga_map(db):

    view = {
        "_id": "_design/lga_map",
        "views": {
            "lga_map_check": {
            "reduce": "_sum",
            "map": "function (doc) {emit(doc.id, 1);}"
            },
            "lga_map_cities": {
            "reduce": "_sum",
            "map": "function (doc) {emit(doc.properties_vic_lga__2, 1);}"
            },
            "lga_geo_data": {
                "map": "function (doc) {  emit(doc.properties_vic_lga__2, [doc.geometry_type, doc.geometry_coordinates]);}"
            }
        }
    }
    try:
        db.save(view)
    except couchdb.http.ResourceConflict:
        design = db["_design/lga_map"]
        db.delete(design)
        db.save(view)

def design_view_income(db):

    view = {
        "_id": "_design/income_data",
        "views": {
            "income_data_check": {
            "reduce": "_sum",
            "map": "function (doc) {emit(doc.id, 1);}"
            }
        }
    }

    try:
        db.save(view)
    except couchdb.http.ResourceConflict:
        design = db["_design/income_data"]
        db.delete(design)
        db.save(view)

def design_view_crime_rate(db):

    view = {
        "_id": "_design/crime_rate_data",
        "views": {
            "crime_rate_data_check": {
            "reduce": "_sum",
            "map": "function (doc) {emit(doc.id, 1);}"
            }
        }
    }
    try:
        db.save(view)
    except couchdb.http.ResourceConflict:
        design = db["_design/crime_rate_data"]
        db.delete(design)
        db.save(view)

def design_view_get_income(db):
#    db = server['income_data']
    view = {
        "_id": "_design/get_income",
        "views": {
            "income_2010-11": {"map": "function (doc) {  emit(doc.properties_lga_name16, doc.properties_income_aud_2010_11);}"},
            "income_2011-12": {"map": "function (doc) {  emit(doc.properties_lga_name16, doc.properties_income_aud_2011_12);}"},
            "income_2012-13": {"map": "function (doc) {  emit(doc.properties_lga_name16, doc.properties_income_aud_2012_13);}"},
            "income_2013-14": {"map": "function (doc) {  emit(doc.properties_lga_name16, doc.properties_income_aud_2013_14);}"},
            "income_2014-15": {"map": "function (doc) {  emit(doc.properties_lga_name16, doc.properties_income_aud_2010_11);}"},
            "total_income": {
            "map": "function (doc) { emit(((doc.properties_income_aud_2010_11 + doc.properties_income_aud_2011_12 + doc.properties_income_aud_2012_13 + doc.properties_income_aud_2013_14 + doc.properties_income_aud_2014_15) / 6), doc.properties_lga_name16);}"
            }
        }
    }
    try:
        db.save(view)
    except couchdb.http.ResourceConflict:
        design = db["_design/get_income"]
        db.delete(design)
        db.save(view)

def design_view_get_crime(db):
#    db = server['crime_rate_data']
    view = {
        "_id": "_design/crime",
        "views": {
            "crime_search": {
            "map": "function (doc) { emit([doc.lga_name,doc.lga_code],doc.sexual_offences);}",
            "reduce": "_sum"
            }
        }
    }
    try:
        db.save(view)
    except couchdb.http.ResourceConflict:
        design = db["_design/crime"]
        db.delete(design)
        db.save(view)

def design_view_get_sen_count(db):
#    db = server['tweets_data']
    view = {
      "_id": "_design/get_sen_count",
      "views": {
        "get_sen": {
          "map": "function (doc) {  if(doc.city){  emit(doc.city, 1);}}",
          "reduce": "_sum"
        },
        "get_sen_sum": {
          "map": "function (doc) {  emit(doc.city,doc.sentiment_score);}",
          "reduce": "_sum"
        },
        "isalco_coor": {
          "map": "function(doc){  if(doc.IsAlcohol == 1){  emit(doc.IsAlcohol,doc.geo);}}"
        },
        "week_count": {
          "reduce": "_count",
          "map": "function(doc){  if(doc.post_date){  var week =doc.post_date.split(\" \")[0];  emit(week ,1);}}"
        },
        "drink_count": {
          "map": "function(doc){  if(doc.IsAlcohol == 1){  emit(doc.IsAlcohol,doc.geo);}}",
          "reduce": "_count"
        },
        "tweet_sum": {
          "reduce": "_count",
          "map": "function (doc) {  emit(doc.city,1);}"
        },
        "drink_count_C": {
          "reduce": "_count",
          "map": "function (doc) {  if(doc.IsAlcohol==1){  emit(doc.city, 1);}}"
        },
        "get_sen_and_drink": {
          "map": "function (doc) {  if(doc.IsAlcohol==1){  emit(doc.IsAlcohol,doc.sentiment_score );}}"
        }
      }
    }
    try:
        db.save(view)
    except couchdb.http.ResourceConflict:
        design = db["_design/get_sen_count"]
        db.delete(design)
        db.save(view)