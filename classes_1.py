class Parrot:
    def __init__(self):
        self.is_hungry = True


class Human:
    def get_food(self, parrot):
        if parrot.is_hungry:
            parrot.is_hungry = False


parrot1 = Parrot()
parrot2 = Parrot()

human = Human()

human.get_food(parrot1)

print(parrot1.is_hungry)
print(parrot2.is_hungry)
