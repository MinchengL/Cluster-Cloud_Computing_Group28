


def filter_city(db, results):
    final_results = {}

    for item in results:
        if item is not None:
            city_name = item.upper()
            for row in db.view('lga_map/lga_map_cities',group=True):
                if row.key.find(city_name) != -1:
                    final_results[item] = results[item]
    return final_results