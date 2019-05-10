from geojson_utils import point_in_polygon
import json
import couchdb

server = couchdb.Server('http://admin:lmc940523!@127.0.0.1:5984/')
try:
    lga_map_db = server['lga_map_data']
except BaseException:
    lga_map_db = server.create('lga_map_data')

def geo_analysis(tweet_geo):
    result=None
    tweet_coordinates_str = '['+str(tweet_geo[0])+','+str(tweet_geo[1])+']'
    tweet_point_str = '{"type":"Point", "coordinates": '+tweet_coordinates_str+'}'
    tweet_point_str_json = json.loads(tweet_point_str)
    for id in lga_map_db:
        city_name= lga_map_db[id].get('properties_vic_lga__2')
        coordinates= lga_map_db[id].get('geometry_coordinates')
        geometry_type = lga_map_db[id].get('geometry_type')
        coordinates_str=''
        if city_name is not None and coordinates is not None and geometry_type is not None:
            for item in coordinates[0][0]:
                coordinates_str += '['+str(item[1])+','+str(item[0])+'],'
            coordinates_str = '[[['+coordinates_str[:-1]+']]]'
            points_str ='{"type":"'+geometry_type+'", "coordinates": '+coordinates_str+'}'
            points_str_json = json.loads(points_str)
            if point_in_polygon(tweet_point_str_json,points_str_json):
                result = city_name
    print(result)
    return result

def city_analysis(city):
    result=None
    for id in lga_map_db:
        city_name = lga_map_db[id].get('properties_vic_lga__2')
        if city_name is not None:
            if city_name.find(city.upper()) != -1:
                result = city_name
    return result

