import requests
from .defaults import *

class BaseEndpoint(object):

    def __init__(self, *args, **kwargs):
        self.request_param = kwargs.get("request_param", {})
        self.request_url = kwargs.get("request_url", YTS_API_URL)
        self.request_name = kwargs.get("request_name", "")
        self.request_type = kwargs.get("request_type", "get")
        self.request_response_format = kwargs.get("request_response_format", YTS_DEFAULT_RESPONSE_FORMAT)

        #OVERRIDE DEFAULT VALUES
        self.init()

    def init(self, **kwargs):
        raise NotImplementedError("Please override init")

    def __repr__(self):

        return self.request_name

    def request(self, **kwargs):

        ret = YTS_RESPONSE
        res = None

        if len(kwargs) > 0:
            self.request_param.update(kwargs)

        try:
            if self.request_type == "post":
                res = getattr(requests, self.request_type)("%s%s.%s" % (self.request_url, self.request_name, self.request_response_format), data=self.request_param)
            elif self.request_type == "get":
                res = getattr(requests, self.request_type)("%s%s.%s" % (self.request_url, self.request_name, self.request_response_format), params=self.request_param)
            else:
                raise Exception("Invalid request type!!")

            ret = res.json()
        except Exception as e:
            ret["status_message"] = str(e)

        return ret

    def listParams(self):
        print ", ".join(self.request_param.viewkeys())       

class BaseRequestType(object):

    def __init__(self, app_key=None):
        self.application_key = app_key
        self.type_name = ""

    def __repr__(self):
        return self.type_name