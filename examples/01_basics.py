import sys
sys.path.append("C:\\sven_tools\\sven_tools\\py-pinterest")
sys.path.append("C:\\sven_tools\\third_parties\\requests")

import requests
import pinterest

pt = pinterest.Pinterest()


api = pinterest.PinterestRest()
pins = api.user_pins("giulia")

for pin in pins:
    # print repr(pin)
    print pin
    break

