import queue
import os
import threading

keyword_list = queue.Queue(100)
rawdata_list = queue.Queue(100)

keyword_list.put('Whiskey')
keyword_list.put('Vodka')
keyword_list.put('Brandy')
keyword_list.put('Vermouth')
keyword_list.put('Cognac')
keyword_list.put('Beer')
keyword_list.put('Wine')
keyword_list.put('Rum')
keyword_list.put('Gin')

