import time
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import twitter_credentials
import json
import couchdb
import queueData

#location = [140.957576, -39.134073, 149.977361, -33.996347]

class TwitterStreamer():

    def __init__(self):
        pass

    def stream_tweets(self, consumer_key, consumer_secret, access_token, access_token_secret, location):
        listener = StdOutListener()
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        stream = Stream(auth, listener)
        stream.filter(locations=location)

class StdOutListener(StreamListener):

    def __init__(self):
        pass

    def on_data(self, data):
        jsondata = json.loads(data)
        user_id = jsondata['user']['id']
        queueData.keyword_list.put(user_id)
        queueData.rawdata_list.put(data)

    def on_error(self, status):
        if status ==420:
            time.sleep(100)
        print(status)
