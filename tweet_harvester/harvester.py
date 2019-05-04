from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import twitter_credentials
import json
import couchdb
'''
# need fix how to connect couchDB

server = couchdb.Server('http://127.0.0.1:5984/')
db = server.create('tweets')
'''


class TwitterStreamer():

    def __init__(self):
        pass

    def stream_tweets(self, fetched_tweets_filename,location):
        # This handles Twitter authetification and the connection to Twitter Streaming API
        listener = StdOutListener(fetched_tweets_filename)
        auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
        auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
        stream = Stream(auth, listener)

        # This line filter Twitter Streams to capture data by the keywords: 
        stream.filter(locations=location)


# # # # TWITTER STREAM LISTENER # # # #
class StdOutListener(StreamListener):

    def __init__(self, fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename

    def on_data(self, data):
        try:
            #print(data)
            #print(type(data))
            
            x=json.loads(data)
            write_data = {'id':None,
                          'post_date':None,
                          'text':None,
                          'user':{'followers_count' : None, 'friends_count' : None},
                          'geo':[None,None]
                          }
            
            
            write_data['id']= x['id']
            write_data['post_date'] = x['created_at']
            write_data['text'] = x['text']
            write_data['user']['followers_count'] = x['user']['followers_count']
            write_data['user']['friends_count'] = x['user']['friends_count']
            if x['geo'] is not None:
                if x['geo']['coordinates'] is not None:
                    write_data['geo'] = x['geo']['coordinates']  ####ONLY FEW data contains geo location!!, most of em are NULL
 
            
            #db.save(write_data) # write data into database   data MUST BE DICT WHEN ADD IN DB!!
            
            

            print(write_data)
            
           
            
            with open(self.fetched_tweets_filename, 'a') as tf:
                tf.write(json.dumps(write_data)) ## save as json file also
                tf.write('\n')
        except BaseException as e:
            print("Error on_data %s" % str(e))
        return True
          

    def on_error(self, status):
        if status ==420:
            time.sleep(100) ### in case of get limit and account get banned
        
        print(status)

 
if __name__ == '__main__':
 
    # Authenticate using config.py and connect to Twitter Streaming API.
    #hash_tag_list = ["beer", "whiskey", "club", "pub", "alcohol" , "drink"]  ##tweet api can not filter by location and hashtags at same time!!
    location =[144.5937,-38.5047,145.6299,-37.5113] #melbourne
    #location = [5.0770049095, 47.2982950435, 15.0403900146, 54.9039819757] #german
    ## this is approx mebourne location area, maybe?
    fetched_tweets_filename = "tweets.json"

    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(fetched_tweets_filename, location)