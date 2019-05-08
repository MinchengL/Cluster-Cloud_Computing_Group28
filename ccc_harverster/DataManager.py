import queue
import time
import threading
from threading import Thread
import threadpool
import stream_harvester
import search_harvester
import sentiment_alnayzer
import queueData

twitterSearcher = search_harvester.TwitterSearcher()
twitterStreamer = stream_harvester.TwitterStreamer()
search_api_job_num = 5;
sentiment_analysis_job_num = 5;

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

if __name__ == '__main__':

    for i in range(search_api_job_num):
        t = Thread(target = do_search_api_job)
        t.daemon = True
        t.start()

    for i in range(sentiment_analysis_job_num):
        t = Thread(target = do_sentiment_analysis_job)
        t.daemon = True
        t.start()

    twitterStreamer.stream_tweets()

    time.sleep(3)

    queueData.keyword_list.join()
    queueData.rawdata_list.join()