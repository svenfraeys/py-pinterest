"""
"""
from . import Model
from . import props

class Pin(Model):
    """pin for pinterest
    """
    attribution = props.AttributionProperty()
    board = props.BoardProperty()
    description = props.Property()
    dominant_color = props.Property()
    embed = props.Property()
    id = props.Property()
    images = props.Property()
    is_video = props.Property()
    like_count = props.Property()
    link = props.Property()
    pinner = props.PinnerProperty()
    repin_count = props.Property()

    def __str__(self):
        return 'Pin %s' % (self.id)