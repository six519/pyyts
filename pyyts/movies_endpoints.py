from .bases import *

class ListMovies(BaseEndpoint):

    def init(self):
        self.request_name = "list_movies"
        self.request_param = {
            "limit": None,
            "page": None,
            "quality": None,
            "minimum_rating": None,
            "query_term": None,
            "genre": None,
            "sort_by": None,
            "order_by": None,
            "with_rt_ratings": None
        }

class MovieDetails(BaseEndpoint):

    def init(self):
        self.request_name = "movie_details"
        self.request_param = {
            "movie_id": None,
            "with_images": None,
            "with_cast": None,
        }

class MovieSuggestions(BaseEndpoint):

    def init(self):
        self.request_name = "movie_suggestions"
        self.request_param = {
            "movie_id": None
        }

class MovieComments(BaseEndpoint):

    def init(self):
        self.request_name = "movie_comments"
        self.request_param = {
            "movie_id": None
        }

class MovieReviews(BaseEndpoint):

    def init(self):
        self.request_name = "movie_reviews"
        self.request_param = {
            "movie_id": None
        }

class MovieParentalGuides(BaseEndpoint):

    def init(self):
        self.request_name = "movie_parental_guides"
        self.request_param = {
            "movie_id": None
        }

class ListUpcoming(BaseEndpoint):

    def init(self):
        self.request_name = "list_upcoming"
        self.request_param = {}