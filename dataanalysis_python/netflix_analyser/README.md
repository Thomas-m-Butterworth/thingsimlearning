### Notes
- This will need a way to know that the CSV entry and the search result are an exact match, since the information pool is so limited. (e.g. Searching *'Cats'* on the API doesn't return the 2019 result first)
```if netview == title```

## To Do: Making the Data Useful
The data we have is very limited (only two fields - title, date viewed). This means that it must be parsed to not contain any TV entries using Netflix's standard structure of titling a TV episode ("{title} - {season #}{episode #}) 

- Parse NetflixViewingHistory.csv.
    - Remove cells containing the word "Season" - eliminates TV easily
    - Place parsed copy into a new CSV.
        - Full new CSV can still be used to gather limited data from a wider time frame (repetitions, counts, etc.), but expanded data cannot be taken from all of it.
- Take new_csv and search the API for them to collect more data.
    - Limit to 400 so we don't go over RapidAPI's free use quota
- Input data to a new CSV file
- New data analysed/visualised later.

## Minor Issues
- **KeyError** when the search only returns one result. Should be solvable by using .get() to set a default key.
- Multiple *elif* statements in **netflix_parse.py** a little ugly. Look for cleaner solutions.
