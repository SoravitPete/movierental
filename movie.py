"""Manage Movie and PriceCode class."""
from typing import List


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
