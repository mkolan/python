class Bank:
    def __init__(self, name, money):
        self.__name = name
        self.__balance = money


    def deposit(self, money):
        self.__balance += money


    def withdraw(self, money):
        if self.__balance > money:
            self.__balance -= money
            return money
        else:
            return "Insufficient funds"

    def checkbalance(self):
        return self.__balance



a = Bank("madhu", 2000)
print(a.checkbalance())
a.deposit(1000)
print (a.withdraw(1000))
print(a.checkbalance())


