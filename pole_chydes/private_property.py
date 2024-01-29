class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

person = Person("Oleg", 29)


print("Name:", person.get_name())
print("Age:", person.get_age())

person.set_name("Pavlo")
person.set_age(30)


print("Updated Name:", person.get_name())
print("Updated Age:", person.get_age())

