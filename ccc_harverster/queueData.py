import queue
import couchdb

keyword_list = queue.Queue(100)
rawdata_list = queue.Queue(100)

customer_keys_list = queue.Queue(10)
customer_secret_list = queue.Queue(10)
access_token_list = queue.Queue(10)
access_token_secret_list = queue.Queue(10)
location_list = queue.Queue(10)

customer_keys_list.put("oFY1p72UPiLol61ITagJEvEcE")
customer_keys_list.put("vAD2x1F8jxweJ6VKBKYQsZQXB")
customer_keys_list.put("UoY0asDOFvgVWzDAwJ9iXruI8")

customer_secret_list.put("jJJRjLn747wF1MNsMGA8YExx9IjqRvXeSpmJuAHik43cCREz6a")
customer_secret_list.put("NIDpWl6cf4zrRtNd4b7GrDbQjeYt2bzv0diOsHO73VV4Najf4o")
customer_secret_list.put("jmoSCfa2z1BcUVE3RjvDFEq5S9Jdjfj9vtqgX491ee3hj1IqLn")

access_token_list.put("1121229845524959233-0VCTkzW11H4ALmEPFHAyFoVzUk0JBL")
access_token_list.put("1126045851430735872-HWq1kk8TdctAlId7EVTpa4ysS2dv6J")
access_token_list.put("1123824289197719554-gagonj3img1zdswthN0LaIlYJF4yOQ")

access_token_secret_list.put("WKTJT16jfijSvuRGFneHHbSdkCi35bQlXnYfWjPJ72QBL")
access_token_secret_list.put("yIyKigZNYqbkQFDoHcwcOecFQKCqkkqH5BZjGYqydwSUs")
access_token_secret_list.put("ajUocRfxqLV66nPiC55ukk4keXaGsVNmpdBinjlBYc6p7")

location1 = [140.957576, -39.134073, 143.97620, -33.996347]
location2 = [143.97620, -39.134073, 146.99246, -33.996347]
location3 = [146.99246, -39.134073, 149.977361, -33.996347]
location_list.put(location1)
location_list.put(location2)
location_list.put(location3)

server = couchdb.Server('http://127.0.0.1:5984/')
try:
    tweets_db = server['tweets_data']
except BaseException:
    tweets_db = server.create('tweets_data')

try:
    raw_tweets_db = server['raw_tweets']
except BaseException:
    raw_tweets_db = server.create('raw_tweets')

try:
    lga_map_db = server['lga_map_data']
except BaseException:
    lga_map_db = server.create('lga_map_data')

try:
    income_data_db = server['income_data']
except BaseException:
    income_data_db = server.create('income_data')

try:
    crime_rate_data_db = server['crime_rate_data']
except BaseException:
    crime_rate_data_db = server.create('crime_rate_data')