import sys
sys.path.append("C:\\sven_tools\\sven_tools\\py-pinterest")
sys.path.append("C:\\sven_tools\\third_parties\\requests")
from pprint import pprint
import requests
import pinterest

pt = pinterest.Pinterest('sfraeys')
# for pin in pt.pins:
    # print pin.description
print len(pt.pins)
# pins = pt.pins_from_board('Arrow')

# api = pinterest.PinterestRest()
# api.load_from_url('https://api.pinterest.com/v3/pidgets/users/giulia/boards/')
# result_dict = api.load_from_url('https://api.pinterest.com/v3/pidgets/boards/giulia/world/pins/')
# board = result_dict['board']
# print repr(result_dict)

# help(board)
# print repr(board)