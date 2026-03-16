class Car:
    def __init__(self,brand,model,color):
        self.brand=brand
        self.model=model
        self.color=color
    def __str__(self):
        return f'its a {self.brand} {self.model} car of {self.color} color'
    def __del__(self):
        print(f'{self.brand} {self.model} is out of stock')

c1=Car('BMW','X7','white')
print(c1)
del c1

c2=Car('Mercedes','gls600','black')
print(c2)
c2=None