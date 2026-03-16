class BankAccount:
    def __init__(self,b):
        self.__balance=b
    def deposite(self,amt):
        self.__balance+=amt
    def withdraw(self,amt):
        self.__balance-=amt
    def show_bal(self):
        print('Balance:',self.__balance)
Sachin=BankAccount(200000)
# Sachin.balance #error
Sachin.show_bal()