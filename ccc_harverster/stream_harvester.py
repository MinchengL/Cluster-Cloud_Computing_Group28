import time
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import twitter_credentials
import json
import couchdb
import queueData

#location = [144.5937,-38.5047,145.6299,-37.5113]
location = [140.957576, -39.134073, 149.977361, -33.996347]
#location = [-39.134073, 140.957576,-33.996347 , 149.977361]

class TwitterStreamer():

    def __init__(self):
        pass

    def stream_tweets(self):
        listener = StdOutListener()
        auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
        auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
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
