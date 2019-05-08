from web import db
from web import app
from flask import jsonify




def __cols(pairs=[]):
    return map(lambda x: {'id': '', 'label': x[0], 'type': x[1]}, pairs)

@app.route('/sentiment_data')
def ret_sentidata():
    response = {
       'cols': __cols([('Device', 'string'), ('Tweets', 'number')]),
        'rows':
            {'c': [{'v': '111'}, {'v': 2},{'d','222'},{'dqwq',222}]}

    }
    return jsonify(response)



@app.route('/get_popbar_data')
def ret_bardata():
   pass


@app.route('/get_tl_daily_data')
def ret_tl_daily():
   pass


@app.route('/get_tl_weekly_data')
def ret_tl_weekly():
   pass

@app.route('/get_map_data')
def ret_map_data():
   pass

@app.route('/get_drink_data')
def ret_drink_data():
   pass
