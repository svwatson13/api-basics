import requests
path_url = 'https://api.spotify.com/v1/tracks/'
arguments = '6sFIWsNpZYqfjUpaCgueju'
# Build URL
artists = requests.get(path_url+arguments)


# Turn this into a dictionary
dict_response = arguments()
print(dict_response)
