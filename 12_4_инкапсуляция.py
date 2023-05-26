class Person:
    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str):
        self.__name = name

    def get_age(self) -> int:
        return self.__age

    def set_age(self, age: int):
        if age >= 0:
            self.__age = age
        else:
            print("Возраст не может быть отрицательным!")


person = Person("John", 30)

print(person.get_name())

person.set_name("Mike")

print(person.get_name())
print(person.get_age())

person.set_age(-5)

print(person.get_age())
