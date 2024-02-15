class ForbiddenAttributesMeta(type):
    def __new__(cls, name, bases, dct):

        for attr_name in dct:


            if attr_name.startswith('__') and not attr_name.endswith('__'):
                raise AttributeError(f"Creation of class {name} with '__' prefixed attributes is forbidden.")

        return super().__new__(cls, name, bases, dct)


class MyClass(metaclass=ForbiddenAttributesMeta):
    __attr1 = "This will raise an error"
    _attr2 = "This is allowed, because it starts with one underscore"
    attr3 = "This is allowed, because it doesn't start with underscores"