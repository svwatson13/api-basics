import requests

# Base ur;
path_url = 'http://api.postcodes.io/postcodes/'
arguments = 'e146gt'

# Build URL
post_codes = requests.get(path_url+arguments)
print(type(post_codes))

# Turn this into a dictionary
dict_response = post_codes.json()
print(dict_response)

# Finding out keys in dictionary
print(dict_response.keys())
# Printing status and result
print(dict_response['status'])
print(dict_response['result'])
# Finding keys with results and printing specific info
print(dict_response['result'].keys())
print(dict_response['result']['admin_district'])

for key in dict_response['result']:
    print(key, '-->', dict_response['result'][key])