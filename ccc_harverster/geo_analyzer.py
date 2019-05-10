from geojson_utils import point_in_multipolygon
import json
import couchdb

server = couchdb.Server('http://admin:lmc940523!@127.0.0.1:5984/')
try:
    lga_map_db = server['lga_map_data']
except BaseException:
    lga_map_data = server.create('lga_map_data')

def geo_analysis(tweet_geo):
    result=None
    for id in lga_map_db:
        city_name= lga_map_db[id].get('properties_vic_lga__2')
        coordinates= lga_map_db[id].get('geometry_coordinates')
        geometry_type = lga_map_db[id].get('geometry_type')
        points = {
            "type": geometry_type,
            "coordinates": coordinates[0]
        }
        points_json = json.loads(points)
        tweet_geo_json = json.loads(tweet_geo)
        if point_in_multipolygon(tweet_geo_json,points_json):
            result = city_name
    return result
