import sqlite3
import pandas as pd
import sys
from argparse import ArgumentParser

def movie_database(movies):
    """
    Turns movies_list csv into a SQLite database
    Args:
    movies (str): path to movie data csv file
    Return:
    List of tuples containing the first 5 rows of the movies table
    """
    try:
        # Movie data file
        mdf = pd.read_csv(movies)
        
        # Connects to database
        conn = sqlite3.connect('movies.db')
        
        # CREATES TABLE OF MOVIES
        create = '''CREATE TABLE IF NOT EXISTS movies (
                    position INTEGER PRIMARY KEY, 
                    title TEXT, 
                    url TEXT, 
                    rating REAL, 
                    runtime INTEGER, 
                    year INTEGER, 
                    genre TEXT, 
                    directors TEXT, 
                    content_rating TEXT
                    )'''
        conn.execute(create)
        
        # Insert data efficiently
        mdf.to_sql('movies', conn, if_exists='replace', index=False)

        # Read and return 
        read = '''SELECT * 
                  FROM movies'''
        test = conn.execute(read).fetchall()
        columns = ['position', 'title', 'url', 'rating', 'runtime', 
                   'year', 'genre', 'directors', 'content_rating']
        moviedf = pd.DataFrame(test, columns=columns)
        return moviedf

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

    finally:
        if conn:
            conn.close()

class Search:
    def __init__ (self, data, keyword1, keyword2):
        self.data = data
        self.keyword1 = keyword1
        self.keyword2 = keyword2
    
    def findmethod(self):
        #call genre method if keyword matches
        if self.keyword1 == "genre":
            result = self.genre()
        return result

    def genre(self):
        """
        Searches movies by genre
        Args:
        Data: movie data csv file
        Return:
        List of movies with matching genre
        """
        genre_search = self.data[self.data['genre'].str.contains(self.keyword2)]
        return genre_search
    
    def year(self):
        """Year
        Searches movie by the year.

        Args:
        Data - movie data csv file

        Returns:
        List of movies with matching year
        """
        pass

    def movie_rating(self):
        """Movie_rating
        Data: movie data csv file
        Args:
        Data - movie data csv file

        Returns:
        List of movies with matching rating
        """
        pass
    

    def movie_duration(self, keyword):
        """
        Returns list of 10 longest or shortest movies in terms of duration
        Data: movie data csv file

        Args:
        Data - movie data csv file

        Returns:
        List of movies
        """
        pass

    

    def movie_name(self):
        """Movie_name
        Data: movie data csv file
        Returns: Information about movie with matching name
        """
        pass

    def content_rating(self):
        """Content_rating
        What age rating is the movie. For example, PG-13, R, etc.
        Args:
        Data - csv file with movie data

        Returns:
        Movie with 
        """
        pass
    

    def recommendation(self):
        """Movie_recommendation
        Return a short list of movies that we recommend

        Args:
        Data - csv file

        Return:
        List of movies we recommend
        """
        pass
    

def parse_args(arglist):
    """Parse command-line arguments"""
    parser = ArgumentParser()
    parser.add_argument("movie_database_csv", help="movie data CSV file")
    parser.add_argument("keyword1", help="type of search")
    parser.add_argument("keyword2", help="additional word needed for search")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    #data = movie database ready for searching
    data = movie_database(args.movie_database_csv)
    search = Search(data, args.keyword1, args.keyword2)
    result = search.findmethod()
    print(result)

