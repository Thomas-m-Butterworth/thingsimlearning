import requests
import json

headers = {
    'x-rapidapi-host': "movie-database-imdb-alternative.p.rapidapi.com",
    'x-rapidapi-key': "2d7c539e81msh16f6f09c455ac6dp12b13cjsn93a46006810d"
    }

viewing_history = "NetflixViewingHistory.csv"    

movie_query = input("What are you searching for? ")
# id_query = {"i":imdbID, "type":"movie"}

imdb_api = "https://movie-database-imdb-alternative.p.rapidapi.com/"
search_query = {"s":movie_query, "type":"movie", "page":"1"}

response = requests.request("GET", imdb_api, headers=headers, params=search_query)
imdb = json.loads(response.text)

print(imdb['imdbID'])

# id_response = requests.request("GET", url, headers=headers, params=querystring)
# print(id_response.json)