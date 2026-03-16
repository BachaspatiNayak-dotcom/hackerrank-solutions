'''
StaticMethods are used for getting similar kind of data as input
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
    @staticmethod
    def get_int_val():
        intval=int(input())
        return intval
    def withdraw(self):
        print('enter amount to withdraw:')
        amount=self.get_int_val()
        if amount<=self.balance:
            self.balance-=amount
            print('withdraw successful')
        else:
            print('insufficient balance')
        print(f'available balance is {self.balance},Thank you')
    def deposite(self):
        print('enter amount to deposite:')
        amount=self.get_int_val()
        self.balance+=amount
        print('deposite successful')
    @classmethod
    def modify_roi(cls):
        print('enter new ROI:')
        newroi=cls.get_int_val()
        cls.bank_ROI=newroi
        print('ROI is updated')

Sachin=Bank('Sachin Nayak',12345,100000)
Andy=Bank('Anandita Singh',45678,200000)
Sachin.withdraw()