"""properties
"""
from weakref import WeakKeyDictionary

class Property(object):
    """property
    """
    def __init__(self, default=None):
        self.default = default
        self.data = WeakKeyDictionary()
        
    def __get__(self, instance, owner):
        if instance is None:
            return self
        if instance in self.data:
            return self.data.get(instance, self.default)
        else:
            return self.default
    
    def __set__(self, instance, value):
        if issubclass(type(value), dict):
            prop_name = None
            for prop in instance.properties():
                prop_descriptor = getattr(type(instance), prop)
                if prop_descriptor == self:
                    prop_name = prop
                    
            if prop_name not in ['images']:
                print("warning : type %s property %s is set to value %s" % (type(instance).__name__, prop_name, value))
        self.data[instance] = value

class ModelProperty(Property):
    cls = None
    def __init__(self, default=None):
        """construct

        cls (Model): model type it needs to contain
        """
        super(ModelProperty, self).__init__(default)
        
    def __set__(self, instance, value):
        from . import utils
        from . import types
        if issubclass(type(value), dict):
            model = self.cls()
            utils.load_model_settings(model, value)
            value = model

        self.data[instance] = value

class BoardProperty(ModelProperty):
    """property containing a board
    """
    def __set__(self, instance, value):
        from . import types
        self.cls = types.Board
        super(BoardProperty, self).__set__(instance, value)

class PinProperty(ModelProperty):
    """property containing a board
    """
    def __set__(self, instance, value):
        from . import types
        self.cls = types.Pin
        super(BoardProperty, self).__set__(instance, value)

class PinnerProperty(ModelProperty):
    """property containing a board
    """
    def __set__(self, instance, value):
        from . import types
        self.cls = types.Pinner
        super(PinnerProperty, self).__set__(instance, value)

class AttributionProperty(ModelProperty):
    """property containing a attribution, used in pins
    """
    def __set__(self, instance, value):
        from . import types
        self.cls = types.Attribution
        super(AttributionProperty, self).__set__(instance, value)