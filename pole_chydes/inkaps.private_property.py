class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def set_name(self, new_name):
        if not any (char.isdigit() for char in new_name):
            self._name = new_name
        else:
            print("Error: Name cannot contain digits.")

    def set_age(self, new_age):
        if 0 <= new_age <= 120:
            self._age = new_age
        else:
            print("Error: Age must be between 0 and 120")

person = Person("Oleg", 29)


print("Name:", person.get_name())
print("Age:", person.get_age())


person.set_name("Pavlo")
person.set_age(30)

print("Updated Name:", person.get_name())
print("Updated Age:", person.get_age())


person.set_name("Taras")
person.set_age(121)




