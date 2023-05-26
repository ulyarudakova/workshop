class MyClass:
    def public_method(self):
        self.__private_method()
        print("This is a public method")


    def __private_method(self):
        print("This is a private method")


my_object = MyClass()
my_object.public_method()
my_object.__private_method()
