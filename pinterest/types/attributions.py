"""
"""
from . import Model
from . import props

class Attribution(Model):
    """pin for pinterest
    """
    title = props.Property()
    url = props.Property()
    provider_icon_url = props.Property()
    author_name = props.Property()
    provider_favicon_url = props.Property()
    author_url = props.Property()
    provider_name = props.Property()

    def __str__(self):
        return 'Attribution %s' % (self.title)