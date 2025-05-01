class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name              # public
        self._salary = salary         # protected
        self.__ssn = ssn              # private

e = Employee("Ahmed", 50000, "123-45-6789")
print(e.name)          # Public: Accessible
print(e._salary)       # Protected: Accessible (but discouraged)
# print(e.__ssn)       # Private: Not directly accessible
print(e._Employee__ssn)  # Name mangling for private access
