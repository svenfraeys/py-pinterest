import sys
sys.path.append("/Users/Giu/Documents/svenneke/inhouse/pinterest-api")
sys.path.append("/Users/Giu/Documents/svenneke/third_party/requests")

import pinterest

pt = pinterest.Pinterest()

api = pinterest.PinterestRest()
print api.user_pins("giulia")
