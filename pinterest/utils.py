"""pinterest api
"""
from pprint import pprint
import requests
import json

class PinterestRest(object):
    """managing the rest api
    """
    api_url = "https://api.pinterest.com/v3"

    def user_pins(self, username):
        """return pins of given user
        """
        url = self.api_url + "/pidgets/users/" + username + "/pins/"
        print url
        req = requests.request("GET", url)
        data = json.loads(req.content)
        pprint(data)
        for pin in data["data"]["pins"]:
            print pin["images"]
        print len(data["data"]["pins"])
        print data["data"]["user"]
        return 

class Pinterest(object):
    """pinterest main object
    """
    def __init__(self):
        """construct
        """