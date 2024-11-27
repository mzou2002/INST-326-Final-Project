import re
import pandas as pd
import csv
import sys
from argparse import ArgumentParser

def movie_database(movies):
    """
    Turns movies_list csv into a dataframe object
        
    Args:
    Data: movie data csv file
        
    Return:
    movies list dataframe
    """
    mdf = pd.read_csv(movies)
    return mdf


class Search:
    def __init__ (self, data, keyword):
<<<<<<< HEAD
        self.data = data
        self.keyword = keyword
        
=======
        data = self.data
        keyword = self.keyword
        pass
>>>>>>> 36c7313de9e8408975f54c73ac3207489696cdb3

    def genre(self):
        """
        Searches movies by genre
        
        Args:
        Data: movie data csv file
        
        Return:
        List of movies with matching genre
        """
<<<<<<< HEAD
        
=======


>>>>>>> 36c7313de9e8408975f54c73ac3207489696cdb3
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
<<<<<<< HEAD
    parser.add_argument("movieslist_csv", type = csv, help="movie data CSV file")
=======
    parser.add_argument("movieslist_csv", help="movie data CSV")
    parser.add_argument("input_choice", help="how user plans to search movie data")
>>>>>>> 36c7313de9e8408975f54c73ac3207489696cdb3
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    movie_db = movie_database(args.movieslist_csv)
    input_choice = args.input_choice
    print("Welcome to Movie Recommender, press option you would like to search our database based on!" +
          "Input 1 to search based on genre"
          "Input 2 to search based on year of release"
          "Input 3 to search based on movie rating"
          "Input 4 to search based on movie duration"
          "Input 5 to search based on content rating"
          "Input 6 to search based on random recommendation")
    match input_choice:
        case 1:
            print(Search(movie_db).genre)
        case 2:
            print(Search(movie_db).year)
        case 3:
            print(Search(movie_db).movie_rating)
        case 4:
            print(Search(movie_db).movie_duration)
        case 5:
            print(Search(movie_db).content_rating)
        case 6:
            print(Search(movie_db).recommendation)

    
