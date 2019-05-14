#This file is developed by Team 28 of COMP90024 of The University of Melbourne
#YING DU : 925566
#XINHUI LU : 965246
#MINCHENG LI : 889903
#MIAN WANG : 948291
#MINGZE XIA : 548737

import queue
import time
import threading
from threading import Thread
import stream_harvester
import search_harvester
import sentiment_alnayzer
import queueData
import data_importer
import geo_analyzer

twitterSearcher = search_harvester.TwitterSearcher()
twitterStreamer = stream_harvester.TwitterStreamer()
search_api_job_num = 5;
sentiment_analysis_job_num = 5;
stream_api_job_num = 5;

def do_search_api_job():
    while True:
        keyword = queueData.keyword_list.get()
        time.sleep(1)
        twitterSearcher.searchTweets(keyword)
        print('search_api_job  index, current: %s' % (threading.current_thread()))
        queueData.keyword_list.task_done()

def do_sentiment_analysis_job():
    while True:
        rawdata = queueData.rawdata_list.get()
        time.sleep(1)
        sentiment_alnayzer.dataProcesser(rawdata)
        print('sentiment_analysis_job  type: %s, current: %s' % (type(rawdata),threading.current_thread()))
        queueData.rawdata_list.task_done()

def do_stream_api_job():
    while True:
        customer_key = queueData.customer_keys_list.get()
        customer_secret = queueData.customer_secret_list.get()
        access_token = queueData.access_token_list.get()
        access_token_secret = queueData.access_token_secret_list.get()
        location = queueData.location_list.get()
        time.sleep(1)
        twitterStreamer.stream_tweets(customer_key, customer_secret, access_token, access_token_secret, location)
        print('sentiment_analysis_job, current: %s' % (threading.current_thread()))
        queueData.customer_keys_list.task_done()
        queueData.customer_secret_list.task_done()
        queueData.access_token_list.task_done()
        queueData.access_token_secret_list.task_done()


if __name__ == '__main__':
    data_importer.importGlaMapData()
    data_importer.importIncomeData()
    data_importer.importCriminalData()
    print("data imported")

    for i in range(search_api_job_num):
        t = Thread(target = do_search_api_job)
        t.daemon = True
        t.start()

    for i in range(sentiment_analysis_job_num):
        t = Thread(target = do_sentiment_analysis_job)
        t.daemon = True
        t.start()

    for i in range(stream_api_job_num):
        t = Thread(target = do_stream_api_job())
        t.daemon = True
        t.start()

    time.sleep(3)

    queueData.keyword_list.join()
    queueData.rawdata_list.join()
    queueData.customer_keys_list.join()
    queueData.customer_secret_list.join()
    queueData.access_token_list.join()
    queueData.access_token_secret_list.join()