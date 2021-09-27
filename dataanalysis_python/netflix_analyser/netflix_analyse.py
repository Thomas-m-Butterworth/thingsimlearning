import json
import csv
import requests

row_count = 0

headers = {
    'x-rapidapi-host': "movie-database-imdb-alternative.p.rapidapi.com",
    'x-rapidapi-key': "2d7c539e81msh16f6f09c455ac6dp12b13cjsn93a46006810d"
    }  
parsed_history = "NetflixParsed.csv"
expanded_history = "NetflixExpanded.csv"
imdb_api = "https://movie-database-imdb-alternative.p.rapidapi.com/"

def check_title():
    global row_count
    a_dict = {}
    a_dict.setdefault('missing_key', 'default value')

    with open(parsed_history, "r") as csv_history:
        csv_reader = csv.DictReader(csv_history)

        with open(expanded_history, "w") as new_file:
            fieldnames = ["title", "release_year", "imdb_id", "genre", "imdb_rating", "date_watched"]
            csv_writer = csv.DictWriter(new_file, fieldnames = fieldnames)
            csv_writer.writeheader()

            next(csv_reader)
            for x in csv_reader:
                date_watched = x.get("Date")
                movie_query = x.get("Title")

                search_query = {"s":movie_query, "type":"movie", "page":"1"}

                response = requests.request("GET", imdb_api, headers=headers, params=search_query)
                imdb = json.loads(response.text)

                for x in imdb.get("Search"):
                    if x.get('Title') == movie_query:
                        imdbid = x.get('imdbID')
                        id_query = {"i":imdbid, "type":"movie"}
                        id_response = requests.request("GET", imdb_api, headers=headers, params=id_query)                            
                        final_data = json.loads(id_response.text)

                        title = final_data['Title']
                        genre = final_data['Genre']
                        release_year = final_data['Year']
                        rating = final_data['imdbRating']
                        rows = {
                            "title": title,
                            "release_year": release_year,
                            "imdb_id": imdbid,
                            "genre": genre,
                            "imdb_rating": rating,
                            "date_watched": date_watched
                            }
                        row_count += 1
                        csv_writer.writerow(rows)
                        print(f"{row_count} rows created in {expanded_history}.")
                        break
                    else:
                        pass

check_title()