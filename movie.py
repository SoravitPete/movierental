"""Manage Movie and PriceCode class."""
from typing import List

import csv


class Movie:
    """
    A movie available for rent.
    """

    def __init__(self, title: str, year: int, genre: List[str], price_code):
        # Initialize a new movie.
        self._title = title
        self.price_code = price_code
        self._genre = genre
        self._year = year

    def get_price_code(self):
        """get the price code."""
        return self.price_code

    def get_title(self):
        """Get the title."""
        return self._title

    def get_year(self):
        """Get the year."""
        return self._year

    def get_genre(self):
        """Get the genre."""
        return self._genre

    def is_genre(self, genre: str):
        """Check if the genre is the same."""
        return genre in self._genre

    def __str__(self):
        return self._title


class MovieCatalog:
    source = 'movie.csv'

    def __init__(self):
        self.movie_list = {}
        with open(self.source) as file:
            reader = csv.DictReader(file)
        for each_movie in reader:
            self.movie_list[each_movie["title"]] = {
                "#id": each_movie["#id"],
                "year": each_movie["year"],
                "genre": [genre for genre in each_movie["genres"].split("|")]
            }

    def get_movie(self, title):
        movie_list = self.movie_list[title]
        return Movie(title, movie_list["year"], movie_list["genre"])