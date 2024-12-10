import re
import sqlite3
import pandas as pd
import csv
import sys
from argparse import ArgumentParser

def movie_database(movies):
    """
    Turns movies_list csv into a dataframe object
        
    Args:
    Data: movie data csv file
    keyword(str): which search option to search for
        
    Return:
    movies list dataframe
    """

    # Movie data file
    mdf = pd.read_csv(movies)
    
    # Connects to database
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()
    
    # CREATES TABLE OF MOVIES
    create = '''CREATE TABLE IF NOT EXISTS movies (
                position INTEGER PRIMARY KEY, title TEXT, url TEXT, rating REAL, runtime INTEGER, year INTEGER, genre TEXT, directors TEXT, content_rating TEXT
                )'''
    cursor.execute(create)
    
    # SHOULD INSERT ALL ROWS FROM CSV INTO TABLE
    insert = '''INSERT INTO movies VALUES (?,?,?,?,?,?,?,?,?)'''
        
    for row in mdf.itertuples(index = False, name = None):
        cursor.executemany(insert, row)

    conn.commit()

    read = '''SELECT position, title, url, rating, runtime, year, genre, directors, content_rating FROM movies'''
    test = cursor.execute(read).fetchall()
    print(test)

class Search:
    def __init__ (self, data, keyword):
        self.data = movie_database(data)
        self.keyword = keyword.lower()
        result = ""
        if keyword == "genre":
            result.genre(data)
        elif keyword == "year":
            result.year(data)
        elif keyword == "ratings":
            result.movie_rating(data)
        elif keyword == "duration":
            result.movie_duration(data)
        elif keyword == "name":
            result.movie_name(data)
        elif keyword == "content ratings":
            result.content_rating(data)
        elif keyword == "recommendation":
            result.recommendation(data)
        else:
            print("That's not one of the options. Please try again.")

        return result
    
    def genre(self):
        """
        Searches movies by genre
        
        Args:
        Data: movie data csv file
        
        Return:
        List of movies with matching genre
        """
        movie_file = movie_database(self.data)

        return movie_file

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
    Movie with the correct ratings
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
    parser.add_argument("movies database.csv", type = csv, help="movie data CSV file")
    return parser.parse_args(arglist)



if __name__ == "__main__":
    #args = parse_args(sys.argv[1:])
    #movie_db = movie_database(args.movieslist_csv, args.keyword)
    #movie_db = movie_database(args.movieslist_csv)
    test = Search('movie database.csv','genre')
    print (test)

 