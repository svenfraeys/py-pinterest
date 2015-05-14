"""
"""
from . import Model
from . import props

class Pinner(Model):
    """pin for pinterest
    """
    about = props.Property()
    location = props.Property()
    full_name = props.Property()
    follower_count = props.Property()
    image_small_url = props.Property()
    pin_count = props.Property()
    id = props.Property()
    profile_url = props.Property()

    def __str__(self):
        return 'Pinner %s' % (self.full_name)