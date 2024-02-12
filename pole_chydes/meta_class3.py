class CamelCaseMeta(type):
    def __new__(cls, name, bases, dct):

        if not name[0].isupper():
            raise TypeError(f"Class name '{name}' is not in CamelCase format.")

        return super().__new__(cls, name, bases, dct)


class MyClass(metaclass=CamelCaseMeta):
    pass

class AnotherClass(metaclass=CamelCaseMeta):
    pass


class lowercaseclass(metaclass=CamelCaseMeta):
    pass