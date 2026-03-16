class Grandfather:
    land='100 acre'
    car='Ambassodor'

class Father(Grandfather):
    house='3BHK'
    car='BMW'

class Son(Grandfather):
    bike='KTM'
class Grandson(Son,Father):
    pass
    

g=Grandson()
print(g.car)
print(Grandson.mro())