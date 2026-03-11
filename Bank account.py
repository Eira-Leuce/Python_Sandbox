class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = 0
        self.account_number = 0.01
        self.account_number = account_number
        self.balance = balance

    def add(self, incoming):
        self.balance = self.balance + incoming
        print(f"Сумма успешно зачислена. Текущий баланс: " + str(self.balance))
        return self.balance

    def withdraw(self, outcoming):
        if outcoming > self.balance:
            print("На счете недостаточно средств. Текущий баланс: " + str(self.balance))
            return None
        else:
            self.balance = self.balance - outcoming
            print(f"Сумма успешно снята. Текущий баланс: " + str(self.balance))
            return self.balance


bal1 = BankAccount(1, 1000)
bal1.add(1000)
bal1.withdraw(100)
bal1.withdraw(5000)