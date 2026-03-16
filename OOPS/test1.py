'''
Creating  a class and objects from it
'''
class Bank:
    bank_name='SBI'
    bank_branch='Bengaluru'
    bank_ROI=5
    def __init__(self,cn,an,b):
        self.cname=cn
        self.account_number=an
        self.balance=b
    def customer_details(self):
        print(f'name of the customer is {self.cname}')
        print(f'account_number of the customer is {self.account_number}')
        print(f'balance of the customer is {self.balance}')
    def withdraw(self):
        amount=int(input('enter amount:'))
        if amount<=self.balance:
            self.balance-=amount
            print('withdraw successful')
        else:
            print('insufficient balance')
        print(f'available balance is {self.balance},Thank you')
    def deposite(self):
        amount=int(input('enter amount:'))
        self.balance+=amount
        print('deposite successful')



Sachin=Bank('Sachin Nayak',12345,100000)
Andy=Bank('Anandita Singh',45678,200000)
Sachin.withdraw()