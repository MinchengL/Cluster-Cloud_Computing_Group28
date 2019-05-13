import couchdb


server = couchdb.Server('http://127.0.0.1:5984')
tweets_db = server['tweets_data']
lga_map_db = server['lga_map_data']

tweets = tweets_db.view('get_sen_count/tweet_sum',group = True)
drinks = tweets_db.view('get_sen_count/drink_count_C',group = True)
results = {}
final_results ={}



for tweets_count in tweets:
    name = tweets_count.key
    num = tweets_count.value
    #print(num)
    for drinks_C in drinks:
        num1 = drinks_C.value
        percentage = num1/num
        results[name] = percentage



def filter_city(results):
    for item in results:
        if item is not None:
            city_name = item.upper()
            for row in lga_map_db.view('lga_map/lga_map_cities',group=True):
                if row.key.find(city_name) != -1:
                    final_results[item] = results[item]
    return final_results

final_results = filter_city(results)

print(final_results)