#This file is developed by Team 28 of COMP90024 of The University of Melbourne
#YING DU : 925566
#XINHUI LU : 965246
#MINCHENG LI : 889903
#MIAN WANG : 948291
#MINGZE XIA : 548737

drink_type_list_without_qiyi = [' liquor', 'beer', 'brandy', 'whisky', 'vodka', 'on the rocks', 'abricotine', 'absinth', 'adovocaat', 'aguardiente', 'akvavit', 'ale', 'alegar', 'aperitif', 'applejack', 'aqua vitae', ' aquavit', 'arrack', ' bacchae', ' bacchant', 'bacchus', ' barleycorn', 'beaujolais', 'black velvet', ' blackstrap', 'blind tiger', 'blood mary', ' bock', 'boilermaker', 'bosa', 'bristol milk', ' fizz', 'bumbo', ' burgundy', ' calvados', 'cassis', 'cerevisia', 'chables', 'chianti', 'cider', 'coffin varnish', ' cognac', 'sneaky pete', 'soave', 'spritzer', 'spumante', 'stoutsuck', 'swizzle', 'tepache', 'tequila', 'teran', 'toddy', 'traminer', 'tuckhelm', 'veeno', 'vermouth', 'vin', 'vineyard', 'vino', 'vinum', 'vodka', 'yquem', 'zabaglione', 'zetinger', 'zuica']

drink_list_final = ['Babycham', 'Brexitovka', 'Byejoe', 'Casamigos', 'Controy', 'Espolon', 'Jiangxiaobai', 'Lambrini', 'Lunazul', 'Ruskova', 'Stolichnaya', 'Zhumir', '4 Copas', '10 Cane', '1519 Tequila', '1800 Tequila', 'After Dark ', 'Agwa de Bolivia', 'Amrut ', 'Antiquity ', 'Arbor Mist', 'Arette ', 'Babycham', 'Bagpiper ', "Beam's Eight Star", 'Beefeater Gin', ' Bejois ', 'Belaya Rus vodka', 'Bernheim Original', 'Blenders Pride', 'Bols ', ' Boodles British Gin', 'Brexitovka', 'Byejoe', 'Cabin Still', 'Cacique Guaro', 'California Cooler', 'Calvert Extra Captain Morgan', 'Casa Dragones', 'Casamigos', 'Chase Vodka', 'Chelsea ', 'Cockspur Rum Comparison of alcopops', 'Controy', 'Cork Dry Gin', 'Cristal ', 'Cruzan Rum', "Director's Special ", 'Don Julio', 'Elijah Craig ', 'Emperador brandy', 'Espolon', 'Evan Williams ', 'Excellia Fighting Cock ', 'Ginebra San Miguel ', "Glen's Vodka Gordon's Gin", "Hamlin's Wizard Oil", 'Hardenberg-Wilthen', 'Heaven Hill', "Hendrick's Gin", 'Hpnotiq Imperial Blue ', "J.P. Wiser's Whisky", 'J.T.S. Brown', 'Jewel Isle', 'Jiangxiaobai', 'Jim Beam Jolly Shandy', 'Jose Cuervo', 'Kentucky Vintage', 'Khortytsia ', 'Kizlyar Brandy Factory Kors Vodka', 'Kraken Rum', 'Kvass Taras ', 'Lambrini', 'Le Tourment Vert', 'Lunazul', 'Maestro Dobel Tequila', 'Malfy Gin', "Masons Gin McDowell's No.1 Celebration", 'Mount Gay Rum', "Noah's Mill", 'Old Fitzgerald', 'Old Grand-Dad', ' Old Monk', 'Paul John ', 'James E. Pepper', 'Peter Scot', 'Phillips Union Whiskey', ' Rebel Yell ', 'Red Knight ', 'Rhythm ', 'Romanov ', "Rowan's Creek Rowson's Reserve", 'Royal Challenge', 'Royal Stag', 'Ruskova', 'Russian Standard ', ' Santera Tequila', 'Savvy Vodka', "Sheridan's", 'Signature ', 'SKYY vodka', 'Smirnoff Sobieski ', 'Stolichnaya', 'Suze ', 'Takamaka Rum', 'Three Olives Vodka', 'Tia Maria Toussaint Coffee Liqueur', 'Tubi 60', 'Vin Mariani', 'Swish Beverages', 'White Mountain Cooler Whitley Neill Gin', 'Wild Turkey ', 'Wodka Gorbatschow', 'Zhumir']



############
def check_keyword(text_string): ## input:string, output:int
    ans = 0
    for drink in drink_type_list_without_qiyi:
        d=drink.lower()
        
        if drink.lower() in text_string.lower():
            ans = 1
    for drink2 in drink_list_final:
        if drink2.lower() in text_string.lower():
            ans = 1
    return ans