from .defaults import *
from .request_types import *

class YTSClient(object):

    def __init__(self):
        self.movies = MoviesType()
        self.users = UsersType()