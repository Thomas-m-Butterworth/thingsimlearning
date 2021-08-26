import requests
import json

movie_query = input("What are you searching for? ")

url = "https://movie-database-imdb-alternative.p.rapidapi.com/"

querystring = {"s":movie_query, "type":"movie"}

headers = {
    'x-rapidapi-host': "movie-database-imdb-alternative.p.rapidapi.com",
    'x-rapidapi-key': "2d7c539e81msh16f6f09c455ac6dp12b13cjsn93a46006810d"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
response.json()
imdb = response.json()['imdbID']
id_query = {"i":imdb, "type":"movie"}

id_response = requests.request("GET", url, headers=headers, params=querystring)

    
print(id_response.text)