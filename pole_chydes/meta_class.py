class Meta(type):
    def __new__(cls, name, bases, dct):
        print(f"create new class: {name}")
        return super(). __new__(cls, name, bases, dct)

class MyClass(metaclass=Meta):
    pass

obj = MyClass()
