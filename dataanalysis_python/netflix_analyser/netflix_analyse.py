import requests
import json

headers = {
    'x-rapidapi-host': "movie-database-imdb-alternative.p.rapidapi.com",
    'x-rapidapi-key': "2d7c539e81msh16f6f09c455ac6dp12b13cjsn93a46006810d"
    }

viewing_history = "NetflixViewingHistory.csv"    

movie_query = input("What are you searching for? ")

imdb_api = "https://movie-database-imdb-alternative.p.rapidapi.com/"
search_query = {"s":movie_query, "type":"movie", "page":"1"}

response = requests.request("GET", imdb_api, headers=headers, params=search_query)
imdb = json.loads(response.text)

for x in imdb["Search"]:
    movie_query = movie_query.capitalize()
    if x['Title'] == movie_query:
        imdbid = (x['imdbID'])
        break

id_query = {"i":imdbid, "type":"movie"}
id_response = requests.request("GET", imdb_api, headers=headers, params=id_query)
final_data = json.loads(id_response.text)

title = final_data['Title']
genre = final_data['Genre']
release_year = final_data['Year']
rating = final_data['imdbRating']
print(title)
print(f"Release Year: {release_year}")
print(genre)
print(f"Rated {rating} stars!")