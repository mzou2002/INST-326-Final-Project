import sqlite3
import pandas as pd
import sys
from argparse import ArgumentParser
import random 

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
        #call method if keyword matches
        if self.keyword1 == "genre":
            result = self.genre()
        elif self.keyword1 == "year":
            result = self.year()
        elif self.keyword1 == "movie rating":
            result = self.movie_rating()
        elif self.keyword1 == "movie duration":
            result = self.movie_duration()
        elif self.keyword1 == "movie name":
            result = self.movie_name()
        elif self.keyword1 == "content rating":
            result = self.content_rating()
        elif self.keyword1 == "recommendation":
            result = self.recommendation()
        else:
            result = "That's not one of the options. Please try again."
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
        year_search = self.data[self.data['year'].str.contains(self.keyword2)]
        return year_search

    def movie_rating(self):
        """Movie_rating
        Data: movie data csv file
        Args:
        Data - movie data csv file

        Returns:
        List of movies with matching rating
        """
        movie_rating_search = self.data[self.data['rating']]
        movie = []
        for rating in movie_rating_search:
            if rating == self.keyword2:
                movie.append(rating)
        return movie
    

    def movie_duration(self):
        """
        Returns list of 10 longest or shortest movies in terms of duration
        Data: movie data csv file

        Args:
        Data - movie data csv file

        Returns:
        List of movies
        """
        movie_duration_search = self.data[self.data['runtime']]
        movie = []
        for movie in movie_duration_search: 
            if movie_duration_search <= self.keyword2: #if runtime in mins is less than or equal to given runtime
                movie.append(movie_duration_search)
        return movie


    def movie_name(self):
        """Movie_name
        Data: movie data csv file
        Returns: Information about movie with matching name
        """
        movie_name_search = self.data[self.data['title'].str.contains(self.keyword1)]
        return movie_name_search

    def content_rating(self):
        """Content_rating
        What age rating is the movie. For example, PG-13, R, etc.
        Args:
        Data - csv file with movie data

        Returns:
        Movies with filtered age rating
        """
        content_rating_search = self.data[self.data['content rating'].str.contains(self.keyword2)]
        return content_rating_search
    

    def recommendation(self):
        """Movie_recommendation
        Return a short list of movies that we recommend

        Args:
        Data - csv file

        Return:
        List of movies we recommend, based on how many recommendation you want
        """
        recommendations = [] 
        for _ in range(self.keyword2):
            ran_num = random.randint(0, len(self.data) - 1)
            movie = self.data.iloc[ran_num]  # Get the movie at the random index
            recommendations.append(movie)
       
        return recommendations

def parse_args(arglist):
    """Parse command-line arguments"""
    parser = ArgumentParser()
    parser.add_argument("movie_database_csv", help="movie data CSV file")
    parser.add_argument("keyword1", help="which preference filter to use")
    parser.add_argument("keyword2", help="additional word used to search inside the filter")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    #data = movie database ready for searching
    data = movie_database(args.movie_database_csv)
    search = Search(data, args.keyword1, args.keyword2)
    result = search.findmethod()
    print(result)

