from .. import props

class Model(object):
    """base model class
    """
    @classmethod
    def properties(cls):
        property_list = []

        for attr in dir(cls):
            attr_value = getattr(cls, attr)
            
            if issubclass(type(attr_value), props.Property):
                property_list.append(attr)

        return property_list

    def copy(self):
        """return a copy of the given model
        """
        cls = type(self)
        copy = cls()

        for prop in self.properties():
            value = getattr(self, prop)

            if type(value) is list:
                value = value[:]
            if type(value) is dict:
                value = value.copy()
                
            setattr(copy, prop, value)
            
        return copy

    def __repr__(self):
        """return a representation string
        """
        cls_name = self.__class__.__name__
        prop_list = []

        for prop in self.properties():
            value = getattr(self, prop)
            descriptor = getattr(type(self), prop)
            if value != descriptor.default and value != None:
                repr_value = repr(value)
                prop_list.append('%s=%s' % (prop, repr_value))

        signature = ', '.join(prop_list)
        
        return "{0}({1})".format(cls_name, signature)
