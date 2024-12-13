class TestMovieRecommendor(Search):
    def test_findgenre(self):
        """
        UNIT TEST FOR genre method
        Args:
        Data: movie data csv file
        Return:
        if unit test has been passed ("Test Passed!" if has, AssertionError if not)
        """
        genre = self.genre()
        assert not genre.empty, "Genre search returned empty dataframe"
        return "Test Passed!"
    
    def test_movie_name(self):
        """
        UNIT TEST FOR movie_name method
        Args:
        Data: movie data csv file
        Return:
        if unit test has been passed ("Test Passed!" if has, AssertionError if not)
        """
        movie_name_search = self.movie_name()
        assert not movie_name_search.empty, "No movies were found"
        assert self.keyword2.lower() in movie_name_search.iloc[0]['title'].lower(), f"{self.keyword2} not found in movie title"
        return "Test Passed!"

if __name__ == "__main__":
    test = TestMovieRecommendor() #pass a Search object to test method
    result = test.findgenre() #or tests any method you would like to test
    print(result)