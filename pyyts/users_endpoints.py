from .bases import *

class UserDetails(BaseEndpoint):

    def init(self):
        self.request_name = "user_details"
        self.request_param = {
            "user_id": None,
            "with_recently_downloaded": None
        }

class UserForgotPassword(BaseEndpoint):

    def init(self):
        self.request_name = "user_forgot_password"
        self.request_type = "post"
        self.request_param = {
            "email": None,
            "application_key": None
        }