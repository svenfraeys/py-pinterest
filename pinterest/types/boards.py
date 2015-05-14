"""
"""
from . import Model
from . import props

class Board(Model):
    """pin for pinterest
    """
    description = props.Property()
    url = props.Property()
    follower_count = props.Property()
    pin_count= props.Property()
    name = props.Property()
    id = props.Property()
    image_thumbnail_url = props.Property()

    def __str__(self):
        return self.name