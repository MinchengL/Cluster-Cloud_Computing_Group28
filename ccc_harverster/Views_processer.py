import couchdb

def design_view_lga_map(db):

    view = {
        "_id": "_design/lga_map",
        "views": {
            "lga_map_check": {
            "reduce": "_sum",
            "map": "function (doc) {emit(doc.id, 1);}"
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
