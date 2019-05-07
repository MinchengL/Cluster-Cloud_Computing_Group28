import  json

keywords_list =[]
def get_keyword(json_object):
    try:
        keyword_list = ['Whiskey', 'Vodka', 'Brandy', 'Vermouth','Cognac','Beer','Wine','Rum','Gin']
        #  db.save(write_data) # write data into database   data MUST BE DICT WHEN ADD IN DB!!
        dic = json.loads(json_object)
        text = dic['text']
        print(type(text))
        split_text = text.split()
        print(split_text)
        for item in split_text:
            if item in keyword_list:
                keywords_list.append(item)

    except BaseException as e :
        print(e)




