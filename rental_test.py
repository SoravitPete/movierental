"""Test rental.py."""
import unittest
from rental import Rental, PriceCode
from movie import Movie


class RentalTest(unittest.TestCase):
    """Test rental class."""

    def setUp(self):
        self.new_movie = Movie("Mulan", 2020, ["Action", "Adventure", "Children"], PriceCode.new_release)
        self.regular_movie = Movie("Jurassic World", 2015, ["Action", "Adventure", "Drama", "Sci-Fi", "Thriller"],
                                   PriceCode.regular)
        self.children_movie = Movie("Weathering With You", 2020, ["Animation", "Drama", "Children"], PriceCode.children)

    def test_movie_attributes(self):
        """Test to catch refactoring errors or change in API of Movie."""
        m = Movie("La La Land", 2016, ["Comedy", "Drama", "Romance"], PriceCode.regular)
        self.assertEqual("La La Land", m.get_title())
        self.assertEqual(PriceCode.regular, m.get_price_code())

    def test_rental_price(self):
        """Test rental to get price."""
        rental = Rental(self.new_movie, 1)
        self.assertEqual(rental.get_price(), 3.0)
        rental = Rental(self.new_movie, 5)
        self.assertEqual(rental.get_price(), 15.0)
        rental = Rental(self.regular_movie, 1)
        self.assertEqual(rental.get_price(), 2.0)
        rental = Rental(self.regular_movie, 4)
        self.assertEqual(rental.get_price(), 5.0)
        rental = Rental(self.children_movie, 1)
        self.assertEqual(rental.get_price(), 1.5)
        rental = Rental(self.children_movie, 6)
        self.assertEqual(rental.get_price(), 6.0)

    def test_rental_points(self):
        """Test rental to get rental points."""
        rental = Rental(self.new_movie, 1)
        self.assertEqual(rental.get_frequent_renter_points(), 1)
        rental = Rental(self.new_movie, 5)
        self.assertEqual(rental.get_frequent_renter_points(), 5)
        rental = Rental(self.new_movie, 8)
        self.assertEqual(rental.get_frequent_renter_points(), 8)
        rental = Rental(self.regular_movie, 4)
        self.assertEqual(rental.get_frequent_renter_points(), 1)
        rental = Rental(self.children_movie, 6)
        self.assertEqual(rental.get_frequent_renter_points(), 1)
