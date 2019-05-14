#This file is developed by Team 28 of COMP90024 of The University of Melbourne
#YING DU : 925566
#XINHUI LU : 965246
#MINCHENG LI : 889903
#MIAN WANG : 948291
#MINGZE XIA : 548737

import time
import tweepy
from tweepy import OAuthHandler
import twitter_credentials
import json
import couchdb
import queueData
from tweepy.parsers import JSONParser
from tweepy import models

auth = None
api = None

class TwitterSearcher():

   def searchTweets(self, keyword):
      auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
      auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
      api = tweepy.API(auth)
      for item in tweepy.Cursor(api.user_timeline, id=keyword,lang ='en').items():
         x=json.dumps(item._json)
         queueData.rawdata_list.put(x)
