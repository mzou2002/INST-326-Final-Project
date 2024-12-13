class TestMovieRecommendor(Search):
    def __init__ (self, data, keyword1, keyword2):
        self.data = data
        self.keyword1 = keyword1.lower()
        self.keyword2 = keyword2.lower()

    def test_findgenre(self):
        """
        UNIT TEST FOR genre method
        Args:
        Data: movie data csv file
        Return:
        if unit test has been passed ("Test Passed!" if has, AssertionError if not)
        """
        genre = super().self.genre()
        assert not genre.empty, "Genre search returned empty dataframe"
        return "Test Passed!"
    
    def test_year(self):
        """
        UNIT TEST FOR year method
        Args:
        Data: movie data csv file
        Return:
        if unit test has been passed ("Test Passed!" if has, AssertionError if not)
        """
        year_search = super().self.year()
        assert self.keyword2 in year_search.iloc[0]['year'], "Year was not found"
        return "Test Passed!"

    def test_movie_rating(self):
        """
        UNIT TEST FOR movie_rating method
        Args:
        Data: movie data csv file
        Return:
        if unit test has been passed ("Test Passed!" if has, AssertionError if not)
        """
        movie_rating_search = super().self.movie()
        assert not movie_rating_search.empty, "Movie rating search returned empty dataframe"
        return "Test Passed!"

    def test_movie_duration(self):
        """
        UNIT TEST FOR movie_duration method
        Args:
        Data: movie data csv file
        Return:
        if unit test has been passed ("Test Passed!" if has, AssertionError if not)
        """
        movie_duration_search = super().self.movie_duration()
        assert self.keyword2 <= movie_duration_search.iloc[0]['runtime'], "Run time was not found"
        return "Test Passed!"

    def test_content_rating(self):
        """
        UNIT TEST FOR content_rating method
        Args:
        Data: movie data csv file
        Return:
        if unit test has been passed ("Test Passed!" if has, AssertionError if not)
        """
        content_rating_search = super().self.content_rating()
        assert not content_rating_search.empty, "No content rating was found"
        assert self.keyword2.lower() in content_rating_search.iloc[0]['content_rating'].lower(), f"{self.keyword2} not found in content rating"
        return "Test Passed!"

    def test_recommendation(self):
        """
        UNIT TEST FOR recommendation method
        Args:
        Data: movie data csv file
        Return:
        if unit test has been passed ("Test Passed!" if has, AssertionError if not)
        """
        recommendation_search = super().self.recommendation()
        assert not recommendation_search.empty, "No recommendation was found"
        return "Test Passed!"
    
    def test_movie_name(self):
        """
        UNIT TEST FOR movie_name method
        Args:
        Data: movie data csv file
        Return:
        if unit test has been passed ("Test Passed!" if has, AssertionError if not)
        """
        movie_name_search = super().self.movie_name()
        assert not movie_name_search.empty, "No movies were found"
        assert self.keyword2.lower() in movie_name_search.iloc[0]['title'].lower(), f"{self.keyword2} not found in movie title"
        return "Test Passed!"

if __name__ == "__main__":
    test = TestMovieRecommendor() #pass a Search object to test method
    result = test.findgenre() #or tests any method you would like to test
    print(result)