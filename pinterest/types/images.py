"""
"""
from . import Model
from . import props

class Image(Model):
    """image for pinterest
    """
    width = props.Property()
    height = props.Property()
    url = props.Property()

    def __str__(self):
        return 'Images %s' % (self.full_name)