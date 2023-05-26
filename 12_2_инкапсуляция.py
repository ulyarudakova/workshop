class BankAccount:
    def __init__(self, name, account, balance, password):
        self.name = name
        self.account = account
        self.__balance = balance
        self.__password = password

    def get_balance(self, password):
        if password == self.__password:
            return self.__balance
        else:
            return "Incorrect password"

    def set_balance(self, new_balance, password):
        if password == self.__password:
            self.__balance = new_balance
            return "Balance updated"
        else:
            return "Incorrect password"


account1 = BankAccount("John Smith", "1205", 5000, "password123")

print(account1.get_balance("password123"))
print(account1.set_balance(6000, "password123"))
print(account1.get_balance("password123"))
print(account1.get_balance("wrongpassword"))
