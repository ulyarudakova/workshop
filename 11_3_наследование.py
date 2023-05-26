class Employee:
    def __init__(self, name, status, salary):
        self.name = name
        self.status = status
        self.salary = salary

    def get_info(self):
        return "Name: {}, Position: {}, Salary: {}".format(self.name, self.status, self.salary)


class Orderly(Employee):
    def __init__(self, name, salary):
        super().__init__(name, "Orderly", salary)

    def get_info(self):
        return "Name: {}, Position: {}, Salary: {}".format(self.name, self.status, self.salary)


class Nurse(Employee):
    def __init__(self, name, salary, responsibility):
        super().__init__(name, "Nurse", salary)
        self.responsibility = responsibility

    def get_info(self):
        return "Name: {}, Position: {}, Salary: {}, Programming Language: {}".format(self.name, self.status, self.salary, self.responsibility)


class Doctor(Employee):
    def __init__(self, name, salary, qualification):
        super().__init__(name, "Doctor", salary)
        self.qualification = qualification

    def get_info(self):
        return "Name: {}, Position: {}, Salary: {}, Design Tool: {}".format(self.name, self.status, self.salary, self.qualification)


orderly1 = Orderly("Sem Smith", 10000)
nurse1 = Nurse("Alice Johnson", 50000, "patient care")
doctor1 = Doctor("Bob Williams", 100000, "higher")

print(orderly1.get_info())
print(nurse1.get_info())
print(doctor1.get_info())
