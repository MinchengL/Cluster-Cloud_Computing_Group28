import queue
import os
import threading

keyword_list = queue.Queue(100)
rawdata_list = queue.Queue(100)

