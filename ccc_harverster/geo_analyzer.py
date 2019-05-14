#This file is developed by Team 28 of COMP90024 of The University of Melbourne
#YING DU : 925566
#XINHUI LU : 965246
#MINCHENG LI : 889903
#MIAN WANG : 948291
#MINGZE XIA : 948737

from geojson_utils import point_in_polygon
import json
import couchdb
import queueData

def geo_analysis(tweet_geo):
    result=None
    tweet_coordinates_str = '['+str(tweet_geo[0])+','+str(tweet_geo[1])+']'
    tweet_point_str = '{"type":"Point", "coordinates": '+tweet_coordinates_str+'}'
    tweet_point_str_json = json.loads(tweet_point_str)
    for id in queueData.lga_map_db:
        city_name= queueData.lga_map_db[id].get('properties_vic_lga__2')
        coordinates= queueData.lga_map_db[id].get('geometry_coordinates')
        geometry_type = queueData.lga_map_db[id].get('geometry_type')
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
    for id in queueData.lga_map_db:
        city_name = queueData.lga_map_db[id].get('properties_vic_lga__2')
        if city_name is not None:
            if city_name.find(city.upper()) != -1:
                result = city_name
    return result

