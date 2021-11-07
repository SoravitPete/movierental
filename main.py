# Demonstrate the movie rental code.
# Create a customer with some movies and print a statement.

from movie import Movie, PriceCode, MovieCatalog
from rental import Rental
from customer import Customer


def make_movies():
    catalog = MovieCatalog()
    movies = [
        catalog.get_movie("Batman v Superman: Dawn of Justice"),
        catalog.get_movie("Weathering With You"),
        catalog.get_movie("The Legend of Sarila"),
        catalog.get_movie("Jurassic World"),
        catalog.get_movie("Fifty Shades of Grey"),
    ]
    return movies


if __name__ == '__main__':
    # Create a customer with some rentals
    customer = Customer("Edward Snowden")
    days = 1
    for movie in make_movies():
        customer.add_rental(Rental(movie, days))
        days += 1
    print(customer.statement())
