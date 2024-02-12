class ForbiddenAttributesMeta(type):
    def __new__(cls, name, bases, dct):
        for attr_name in dct:

            if attr_name.startswith('__'):
                raise AttributeError(f"Creation of class {name} with '__' prefixed attributes is forbidden.")

        return super().__new__(cls, name, bases, dct)


class MyClass(metaclass=ForbiddenAttributesMeta):
    __attr1 = "This will raise an error"
    attr2 = "This is allowed"