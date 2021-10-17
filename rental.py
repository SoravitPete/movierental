"""Manage rental of the movie."""
from movie import PriceCode


class Rental:
    """
    A rental of a movie by customer.
    From Fowler's refactoring example.

    A realistic Rental would have fields for the dates
    that the movie was rented and returned, from which the
    rental period is calculated.
    But for simplicity of the example only a days_rented
    field is used.
    """

    def __init__(self, movie, days_rented):
        """
        Initialize a new movie rental object for a movie.

        with known rental period (daysRented).
        """
        if not isinstance(movie.get_price_code(), PriceCode):
            raise TypeError("Unrecognized priceCode.")
        self.movie = movie
        self.days_rented = days_rented

    def get_movie(self):
        """Get movie object."""
        return self.movie

    def get_days_rented(self):
        """Get day rented that client rent the movie."""
        return self.days_rented

    def get_frequent_renter_points(self):
        """Get frequent renter point."""
        return self.movie.get_price_code().get_renter_point(self.days_rented)

    def get_price(self):
        """Get amount of rental."""
        return self.movie.get_price_code().price(self.days_rented)
