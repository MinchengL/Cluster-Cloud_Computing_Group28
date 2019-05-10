import couchdb
import json

server = couchdb.Server('http://admin:lmc940523!@127.0.0.1:5984/')
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

def importGlaMapData():
    isExist = False
    with open("/Users/limincheng/gla_final.json",'r') as file:
        json_file=json.loads(file.read())
        for item in json_file['features']:
            write_data = {
                'type': None,
                'id': None,
                'geometry_type': None,
                'geometry_coordinates':None,
                'geometry_name':None,
                'properties_lg_ply_pid':None,
                'properties_dt_create':None,
                'properties_dt_retire':None,
                'properties_lga_pid':None,
                'properties_vic_lga_sh':None,
                'properties_vic_lga__1':None,
                'properties_vic_lga__2':None,
                'properties_vic_lga__3':None,
                'properties_vic_lga__4':None,
                'properties_vic_lga__5':None
            }
            write_data['type']=item['type']
            write_data['id']=item['id']
            write_data['geometry_type']=item['geometry']['type']
            write_data['geometry_coordinates']=item['geometry']['coordinates']
            write_data['geometry_name']=item['geometry_name']
            write_data['properties_lg_ply_pid']=item['properties']['lg_ply_pid']
            write_data['properties_dt_create']=item['properties']['dt_create']
            write_data['properties_dt_retire']=item['properties']['dt_retire']
            write_data['properties_lga_pid']=item['properties']['lga_pid']
            write_data['properties_vic_lga_sh']=item['properties']['vic_lga_sh']
            write_data['properties_vic_lga__1']=item['properties']['vic_lga__1']
            write_data['properties_vic_lga__2'] = item['properties']['vic_lga__2']
            write_data['properties_vic_lga__3'] = item['properties']['vic_lga__3']
            write_data['properties_vic_lga__4'] = item['properties']['vic_lga__4']
            write_data['properties_vic_lga__5'] = item['properties']['vic_lga__5']

            for row in lga_map_db.view('lga_map/lga_map_check',group=True):
                if row.key == item['id']:
                    isExist = True
            if isExist == False:
                lga_map_db.save(write_data)

def importIncomeData():
    isExist = False
    with open("/Users/limincheng/income_au.json",'r') as file:
        json_file=json.loads(file.read())
        for item in json_file['features']:
            write_data = {
                'type': None,
                'id':None,
                'properties_income_aud_2011_12':None,
                'properties_income_aud_2014_15':None,
                'properties_income_aud_2010_11':None,
                'properties_income_aud_2013_14':None,
                'properties_income_aud_2012_13':None,
                'properties_lga_code_2016':None,
                'properties_lga_name16':None
            }
            write_data['type']=item['type']
            write_data['id']=item['id']
            write_data['properties_income_aud_2012_13']=item['properties']['income_aud_2011_12']
            write_data['properties_income_aud_2014_15']=item['properties']['income_aud_2014_15']
            write_data['properties_income_aud_2010_11']=item['properties']['income_aud_2010_11']
            write_data['properties_income_aud_2013_14']=item['properties']['income_aud_2013_14']
            write_data['properties_income_aud_2012_13']=item['properties']['income_aud_2012_13']
            write_data['properties_lga_code_2016']=item['properties']['lga_code_2016']
            write_data['properties_lga_name16'] = item['properties']['lga_name16']

            for row in income_data_db.view('income_data/income_data_check', group=True):
                if row.key == item['id']:
                    isExist = True
            if isExist == False:
                income_data_db.save(write_data)

def importCriminalData():
    isExist = False
    years = [2010, 2011, 2012, 2013, 2014, 2015]
    for i in years:
        num = str(i)
        name = "crime_rate_" + num
    with open("/Users/limincheng/"+name+".json","r") as crime_file:
        crimes = json.load(crime_file)
    for crime in crimes['features']:
            write_data = {
                'type': None,
                'id': None,
                'lga_name': None,
                'lga_code': None,
                'sexual_offences': None,
                'homicide__and__related_offences': None,
                'regulatory_driving_offences': None,
                'reference_period': None
            }
            write_data['type'] = crime['type']
            write_data['id'] = crime['id']
            write_data['lga_name'] = crime['properties']['lga_name11']
            write_data['lga_code'] = crime['properties']['lga_code']
            write_data['sexual_offences'] = crime['properties']['a30_sexual_offences']
            write_data['homicide__and__related_offences'] = crime['properties']['a10_homicide__and__related_offences']
            write_data['regulatory_driving_offences'] = crime['properties']['f10_regulatory_driving_offences']
            write_data['reference_period'] = crime['properties']['reference_period']

            for row in crime_rate_data_db.view('crime_rate_data/crime_rate_data_check', group=True):
                if row.key == crime['id']:
                    isExist = True
            if isExist == False:
                crime_rate_data_db.save(write_data)

if __name__ =="__main__":
    importGlaMapData()
    importIncomeData()
    importCriminalData()
    print("data imported")