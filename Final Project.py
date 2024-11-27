import re
import sqlite3
import pandas as pd
import csv
import sys
from argparse import ArgumentParser

def movie_database(movies, keyword):
    """
    Turns movies_list csv into a dataframe object
        
    Args:
    Data: movie data csv file
    keyword(str): which search option to search for
        
    Return:
    movies list dataframe
    """
    search = Search()
    
    # Movie data file
    mdf = pd.read_csv(movies)
    
    # Connects to database
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()
    
    # CREATES TABLE OF MOVIES
    create = '''CREATE TABLE IF NOT EXISTS movies ()
                position INTEGER PRIMARY KEY, title TEXT, url TEXT, rating REAL, runtime INTEGER, year INTEGER, genre TEXT, directors TEXT, content_rating TEXT
                )'''
    cursor.execute(create)
    
    # SHOULD INSERT ALL ROWS FROM CSV INTO TABLE
    insert = '''INSERT INTO movies VALUES (?,?,?,?,?,?,?,?,?)'''
        
    for row in mdf.itertuples(index = False, name = None):
        cursor.executemany(insert, row)





    if keyword == "genre":
        search.genre(movies)
    elif keyword == "year":
        search.year(movies)
    elif keyword == "ratings":
        search.movie_rating(movies)
    elif keyword == "duration":
        search.movie_duration(movies)
    elif keyword == "name":
        search.movie_name(movies)
    elif keyword == "content ratings":
        search.content_rating(movies)
    elif keyword == "recommendation":
        search.recommendation(movies)
    else:
        print("That's not one of the options.")
  


class Search:
    def __init__ (self, data, keyword):
        self.data = data
        self.keyword = keyword

    def genre(self):
        """
        Searches movies by genre
        
        Args:
        Data: movie data csv file
        
        Return:
        List of movies with matching genre
        """
        movie_file = movie_database(self.data)

    def year(self):
        pass

    """Year
    Searches movie by the year.

    Args:
    Data - movie data csv file

    Returns:
    List of movies with matching year
    """

    def movie_rating(self):
        pass
    """Movie_rating
    Data: movie data csv file
    Args:
    Data - movie data csv file

    Returns:
    List of movies with matching rating
    """

    def movie_duration(self, keyword):
        pass

    """
    Returns list of 10 longest or shortest movies in terms of duration
    Data: movie data csv file

    Args:
    Data - movie data csv file

    Returns:
    List of movies
    """

    def movie_name(self):
        pass


    """Movie_name
    Data: movie data csv file
    Returns: Information about movie with matching name
    """

    def content_rating(self):
        pass
    """Content_rating
    What age rating is the movie. For example, PG-13, R, etc.
    Args:
    Data - csv file with movie data

    Returns:
    Movie with 
    """

    def recommendation(self):
        pass
    """Movie_recommendation
    Return a short list of movies that we recommend

    Args:
    Data - csv file

    Return:
    List of movies we recommend
    """

def parse_args(arglist):
    """Parse command-line arguments

    Args:
    arglist(list of str): list of command-line arguments

    Returns:
    namespace: the parsed command-line arguments as a namespace 
    with movie data csv file
    """
    parser = ArgumentParser()
    parser.add_argument("movieslist_csv", type = csv, help="movie data CSV file")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    movie_db = movie_database(args.movieslist_csv, args.keyword)
