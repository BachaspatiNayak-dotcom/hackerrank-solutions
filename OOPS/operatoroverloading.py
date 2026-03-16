class Book:
    def __init__(self,bn,bp,ba):
        self.name=bn
        self.price=bp
        self.author=ba
    def __add__(self,other):
        return f'total price of 2 books is {self.price+other.price}'
    def __sub__(self,other):
        return f'{self.name} is {self.price-other.price} rupees more than {other.name}'

b1=Book('Python',10000,'Guido Van Russom')
b2=Book('Django',5000,'Simon Willison')

print(b1+b2)
print(b1-b2)

class Rectangle:
    def __init__(self,L,B):
        self.L=L
        self.B=B
        self.area=L*B
    def __gt__(self,other):
        return self.area>other.area
r1=Rectangle(100,200)
r2=Rectangle(50,250)

print(r1>r2)
        
    
