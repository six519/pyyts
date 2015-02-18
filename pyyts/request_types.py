from .bases import BaseRequestType
from .movies_endpoints import *

class MoviesType(BaseRequestType):

    def __init__(self):
        self.type_name = "movies"

    def list_movies(self, **kwargs):
        return ListMovies().request(**kwargs)

    def movie_details(self, **kwargs):
        return MovieDetails().request(**kwargs)

    def movie_suggestions(self, **kwargs):
        return MovieSuggestions().request(**kwargs)

    def movie_comments(self, **kwargs):
        return MovieComments().request(**kwargs)

    def movie_reviews(self, **kwargs):
        return MovieReviews().request(**kwargs)

class UsersType(BaseRequestType):

    def __init__(self):
        self.type_name = "users"