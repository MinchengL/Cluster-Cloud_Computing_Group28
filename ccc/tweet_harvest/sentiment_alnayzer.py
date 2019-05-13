import json
import re
import couchdb
from textblob import TextBlob
import keywordCheck

server = couchdb.Server('http://127.0.0.1:5984/')
try:
    tweets_db = server['tweets']
except BaseException:
    tweets_db = server.create('tweets')

try:
    raw_tweets_db = server['raw_tweets']
except BaseException:
    raw_tweets_db = server.create('raw_tweets')

def keep_text (tweet):
    print(tweet)
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

def analyze_sentiment(tweet):
    tweet_json = json.loads(tweet)
    sentiment_score = TextBlob(keep_text(tweet_json['text'])).sentiment.polarity
    return sentiment_score


def dataProcesser(tweet):
    sentiment_score = analyze_sentiment(tweet)
    write_data = {'_id': None,
                  'post_date': None,
                  'text': None,
                  'user': {'id': None, 'name': None, 'followers_count': None, 'friends_count': None},
                  'geo': [None, None],
                  'city': None,
                  'state': None,
                  'raw_data': None,
                  'sentiment_score': None,
                  'sentiment_result': None,
                  'IsAlcohol':None
                  }
    x = json.loads(tweet)
    write_data['_id'] = str(x['id_str'])
    write_data['post_date'] = x['created_at']
    write_data['text'] = x['text']
    write_data['user']['id'] = x['user']['id']
    write_data['user']['name'] = x['user']['name']
    write_data['user']['followers_count'] = x['user']['followers_count']
    write_data['user']['friends_count'] = x['user']['friends_count']
    if x['geo'] is not None:
        if x['geo']['coordinates'] is not None:
            write_data['geo'] = x['geo']['coordinates']
            print(tweet)
    if x['place'] is not None:
        if x['place']['name'] is not None:
            write_data['city'] = x['place']['name']
        if x['place']['full_name']:
            state_text = x['place']['full_name'].split(',')
            if len(state_text)>1:
                write_data['state'] = state_text[1]
    write_data['raw_data'] = tweet
    write_data['sentiment_score'] = analyze_sentiment(tweet)
    if write_data['sentiment_score'] >0 :
        write_data['sentiment_result'] = 'positive'
    elif write_data['sentiment_score'] <0 :
        write_data['sentiment_result'] = 'negative'
    else:
        write_data['sentiment_result'] = 'neutral'
    write_data['IsAlcohol'] = keywordCheck.check_keyword(x['text'])

    if tweets_db.get(write_data['_id']) == None:
        tweets_db.save(write_data)
        raw_tweets_db.save(x)
        print(write_data)
        print(x)
