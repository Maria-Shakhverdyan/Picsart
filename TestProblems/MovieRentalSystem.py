from typing import List
from abc import ABC, abstractmethod

class Movie:
    def __init__(self, title, genre, rating):
        self.title = title
        self.genre = genre
        self.rating = rating
    
    @property
    def title(self):
        return self.__title
    
    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise TypeError("Title must be string")
        if value == "":
            raise ValueError("Title cannot be empty")
        self.__title = value
    
    @property
    def genre(self):
        return self.__genre
    
    @genre.setter
    def genre(self, value):
        if not isinstance(value, str):
            raise TypeError("Genre must be string")
        if value == "":
            raise ValueError("Genre cannot be empty")
        self.__genre = value
    
    @property
    def rating(self):
        return self.__rating
    
    @rating.setter
    def rating(self, value):
        if not isinstance(value, str):
            raise TypeError("Rating must be string")
        if value == "":
            raise ValueError("Rating cannot be empty")
        self.__rating = value
    
    def movie_info(self):
        return f"{self.title} ({self.genre}, Rating: {self.rating})"
    
class Customer:
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info
        self.rental_history: List[Rental] = []
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be string")
        if value == "":
            raise ValueError("Name cannot be empty")
        self.__name = value
    
    @property
    def contact_info(self):
        return self.__contact_info
    
    @contact_info.setter
    def contact_info(self, value):
        if not isinstance(value, str):
            raise TypeError("Contact info must be string")
        if value == "":
            raise ValueError("Contact info cannot be empty")
        self.__contact_info = value
    
    def add_movie(self, rental):
        self.rental_history.append(rental)
    
    def show_rental_history(self):
        return [rental.rental_info() for rental in self.rental_history]

class Rental:
    def __init__(self, customer, movie, duration):
        self.customer = customer
        self.movie = movie
        self.duration = duration

    @property
    def customer(self):
        return self.__customer
    
    @customer.setter
    def customer(self, value):
        if not isinstance(value, Customer):
            raise TypeError("Customer must be an instance of Customer")
        self.__customer = value

    @property
    def movie(self):
        return self.__movie
    
    @movie.setter
    def movie(self, value):
        if not isinstance(value, Movie):
            raise TypeError("Movie must be an instance of Movie")
        self.__movie = value
    
    @property
    def duration(self):
        return self.__duration
    
    @duration.setter
    def duration(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Duration must be number")
        if value <= 0:
            raise ValueError("Duration must be greater than 0")
        self.__duration = value

    def rental_info(self):
        return f"{self.customer.name} rented '{self.movie.title}' for {self.duration} days."

class MovieType(ABC):
    @abstractmethod
    def show_movie_type(self):
        pass

class Comedy(MovieType):
    def show_movie_type(self):
        return "Comedy"

class Drama(MovieType):
    def show_movie_type(self):
        return "Drama"

class Anime(MovieType):
    def show_movie_type(self):
        return "Anime"
    

movie1 = Movie("Nachalo", "Drama", "8/10")
movie2 = Movie("Howl's Moving Castle", "Anime", "9.5/10")

customer1 = Customer("Maria", "maria@example.com")
customer2 = Customer("Anna", "anna@example.com")

rental1 = Rental(customer1, movie1, 105)
rental2 = Rental(customer2, movie2, 100)

customer1.add_movie(rental1)
print(customer1.show_rental_history())

customer2.add_movie(rental2)
print(customer2.show_rental_history())