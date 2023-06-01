class User:
    def __init__(self, name, age, passport):
        self.name = name
        self._age = age
        self.__passport = passport


u = User("Henry", 20, 457892)
print(u.name)
print(u._age)
print(u.__passport)
