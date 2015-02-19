from .bases import BaseRequestType
from .movies_endpoints import *
from .users_endpoints import *

class MoviesType(BaseRequestType):

    def __init__(self, app_key=None):
        BaseRequestType.__init__(self, app_key)
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

    def movie_parental_guides(self, **kwargs):
        return MovieParentalGuides().request(**kwargs)

    def list_upcoming(self, **kwargs):
        return ListUpcoming().request(**kwargs)

    def like_movie(self, **kwargs):
        kwargs["application_key"] = self.application_key
        return LikeMovie().request(**kwargs)

    def get_movie_bookmarks(self, **kwargs):
        return GetMovieBookmarks().request(**kwargs)

    def add_movie_bookmark(self, **kwargs):
        kwargs["application_key"] = self.application_key
        return AddMovieBookmark().request(**kwargs)

    def delete_movie_bookmark(self, **kwargs):
        kwargs["application_key"] = self.application_key
        return DeleteMovieBookmark().request(**kwargs)

    def make_comment(self, **kwargs):
        kwargs["application_key"] = self.application_key
        return MakeComment().request(**kwargs)

    def like_comment(self, **kwargs):
        kwargs["application_key"] = self.application_key
        return LikeComment().request(**kwargs)

    def report_comment(self, **kwargs):
        kwargs["application_key"] = self.application_key
        return ReportComment().request(**kwargs)

    def delete_comment(self, **kwargs):
        kwargs["application_key"] = self.application_key
        return DeleteComment().request(**kwargs)

class UsersType(BaseRequestType):

    def __init__(self, app_key=None):
        BaseRequestType.__init__(self, app_key)
        self.type_name = "users"

    def user_details(self, **kwargs):
        return UserDetails().request(**kwargs)

    def user_get_key(self, **kwargs):
        kwargs["application_key"] = self.application_key
        return UserGetKey().request(**kwargs)

    def user_forgot_password(self, **kwargs):
        kwargs["application_key"] = self.application_key
        return UserForgotPassword().request(**kwargs)

    def user_profile(self, **kwargs):
        return UserProfile().request(**kwargs)

    def user_edit_settings(self, **kwargs):
        kwargs["application_key"] = self.application_key
        return UserEditSettings().request(**kwargs)

    def user_register(self, **kwargs):
        kwargs["application_key"] = self.application_key
        return UserRegister().request(**kwargs)

    def user_reset_password(self, **kwargs):
        kwargs["application_key"] = self.application_key
        return UserResetPassword().request(**kwargs)

    def make_request(self, **kwargs):
        kwargs["application_key"] = self.application_key
        return MakeRequest().request(**kwargs)