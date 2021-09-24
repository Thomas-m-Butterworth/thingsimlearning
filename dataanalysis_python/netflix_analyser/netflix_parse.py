import csv

viewing_history = "NetflixViewingHistory.csv"

def parse_telly():
    row_count = 0

    with open(viewing_history, 'r') as csv_history:
        csv_reader = csv.reader(csv_history)

        with open("NetflixParsed.csv", "w") as new_file:
            csv_writer = csv.writer(new_file)

            for x in csv_reader:
                if "Season" in str(x):
                    pass
                elif "Series" in str(x):
                    pass
                elif " :  " in str(x):
                    pass
                elif "RuPaul" in str(x):
                    pass
                elif "Part 1" in str(x):
                    pass
                elif "Part 2" in str(x):
                    pass
                elif "Part 3" in str(x):
                    pass
                elif "Stranger Things" in str(x):
                    pass
                elif "COMEDIANS of the world" in str(x):
                    pass
                elif "American Horror Story" in str(x):
                    pass
                elif "Louis Theroux's Weird Weekends" in str(x):
                    pass
                elif "Black Mirror" in str(x):
                    pass
                elif "Unsolved Mysteries" in str(x):
                    pass
                elif "Nailed It!" in str(x):
                    pass
                elif "The Haunting of Hill House" in str(x):
                    pass
                elif "The Comedy Lineup" in str(x):
                    pass
                elif "Chilling Adventures of Sabrina" in str(x):
                    pass
                elif "Disenchantment" in str(x):
                    pass
                else:
                    row_count += 1
                    csv_writer.writerow(x)
                    print(f"{row_count} rows created.")

parse_telly()