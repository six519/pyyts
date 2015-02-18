from .defaults import *
from .request_types import *

class YTSClient(object):

    def __init__(self, application_key=None):
        self.application_key = application_key
        self.movies = MoviesType(application_key)
        self.users = UsersType(application_key)