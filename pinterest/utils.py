"""pinterest api
"""
from pprint import pprint
import requests
import json
from . import types

access_token = 'MTQzMTU5NDo0MDEzMTMxNTQyMDM2NjM0NTU6OTIyMzM3MjAzNjg1NDc3NTgwN3wxNDMxNjIwNjczOjI1OTIwMDAtLWE2ZTk2ODVmNDc2MTcyYjA5ZTEzMjYxZTExZmI2N2Ni'

def load_model_settings(model, data):
    """load given data dict in the pin object
    """
    model_properties = model.properties()
    for prop in data:
        value = data[prop]
        if prop in model_properties:
            setattr(model, prop, value)
        else:
            print("warning : load data for model %r cant set prop %r with value %r" % (model, prop, value))

class PinterestRest(object):
    """managing the rest api
    """
    api_url = "https://api.pinterest.com/v3"

    def translate_data_dict(self, data):
        """translate given data dict
        """
        translated_data_dict = {}

        for key in data:
            if key == 'pins':
                translated_data_dict['pins'] = []
                for pin_data in data["pins"]:
                    pin = types.Pin()
                    load_model_settings(pin, pin_data)
                    translated_data_dict['pins'].append(pin)
            elif key == 'user':
                model = types.Pinner()
                model_data = data["user"]
                load_model_settings(model, model_data)
                translated_data_dict['user'] = model
            elif key == 'board':
                model = types.Board()
                model_data = data["board"]
                load_model_settings(model, model_data)
                translated_data_dict['board'] = model
                
            else:
                print("warning : did not parse key %s" % key)

        return translated_data_dict

    def user_pins(self, username):
        """return pins of given user
        """
        
        url = self.api_url + "/pidgets/users/" + username + "/pins/?total=1"
        data = self.load_from_url(url)
        return data['pins']
        
    def load_from_url(self, url):
        """load
        """
        print('url = %s' % url)
        req = requests.request("GET", url)
        data = json.loads(req.content)
        pprint(data)
        pinterest_data = data["data"]
        # print('pinterest_data=%s' % pinterest_data)

        if pinterest_data:
            pinterest_data = self.translate_data_dict(pinterest_data)
        return pinterest_data

class Pinterest(object):
    """pinterest main object
    """
    def __init__(self, username=None):
        """construct
        """
        self.username = username

    @property
    def pins(self):
        """return all pins of current user
        """
        api = PinterestRest()
        # return self._pins
        return api.user_pins(self.username)

    def pins_from_board(self, board_name):
        """
        """
        api = PinterestRest()
        # return self._pins
        return api.load_from_url('https://api.pinterest.com/v3/pidgets/boards/365daysofbaking/wow/pins/?page_size=20&access_token=%s' % access_token)['pins']