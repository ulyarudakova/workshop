class Cat:
    def __init__(self, name, breed, age, color):
        self.name = name
        self.breed = breed
        self.age = age
        self.color = color


cat1 = Cat("mr. Sam", "mongrel", "5 months", "tortoiseshell")
cat2 = Cat("Cookie", "british", "1 year", "grey")
cat3 = Cat("Apollo", "sphinx", "3 years", "white")

print(cat1.breed)
print(cat2.color)
print(cat3.age)
