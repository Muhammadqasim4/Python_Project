class Bank:
    bank_name = "State Bank"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

a = Bank()
b = Bank()
print(a.bank_name)
Bank.change_bank_name("National Bank")
print(b.bank_name)
