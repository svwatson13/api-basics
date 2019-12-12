import requests
import time


path_url = 'http://api.postcodes.io/postcodes/'
arguments = 'N44SS'
post_codes = requests.get(path_url+arguments)
dict_response = post_codes.json()
print(dict_response)

def latitude():
    path_url = 'http://api.postcodes.io/postcodes/'
    argument = input('Whats your postcode? ').strip()
    post_code = requests.get(path_url + argument)
    dict_response = post_code.json()
    print('Working out latitude...')
    time.sleep(2)
    print(dict_response['result']['latitude'])

def longitude():
    path_url = 'http://api.postcodes.io/postcodes/'
    argument = input('Whats your postcode? ').strip()
    post_code = requests.get(path_url + argument)
    dict_response = post_code.json()
    print('Working out longitude...')
    time.sleep(2)
    print(dict_response['result']['longitude'])

def postcode_info_txt():
    path_url = 'http://api.postcodes.io/postcodes/'
    argument = input('Whats your postcode? ').strip()
    post_code = requests.get(path_url + argument)
    dict_response = post_code.json()
    try:
        with open(f"{argument}.txt", 'w+') as file_to_make:
            file_to_make.write(f"Postcode: {dict_response['result']['postcode']}"
                            f"\nLongitude: {dict_response['result']['longitude']}"
                            f"\nLatitude: {dict_response['result']['latitude']}"
                            f"\nNuts: {dict_response['result']['nuts']}"
                            f"\nAdmin_Ward: {dict_response['result']['admin_ward']}")
    except KeyError:
        print('That was not a valid postcode')
    finally:
        print('Run the code again')


# latitude()
# longitude()
postcode_info_txt()








# # Task
# 1- play around with API and getting data
# 2- from postcode retrieve following data -Long -Lat -nuts -admin_ward
# 3- build a function that returns the lat of a postcode
# 4- build another function that returns long of postcode
# 5- allows me to search a postcode and get the following data exported to a text fie:
# postcode, lat, long, nuts, admin_ward

