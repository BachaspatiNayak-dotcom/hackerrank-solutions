'''
creating one child class from another child class
'''
class Grandfather:
    def __init__(self,land):
        self.assests1=land

class Father(Grandfather):
    def __init__(self,land,house):
        super().__init__(land)
        self.assests2=house

class Son(Father):
    def __init__(self, land, house,bike):
        super().__init__(land,house)
        self.assests3=bike

Mohan=Grandfather('100 acre')
Dhanu=Father('150 acre','3BHK')
Sachin=Son('150 acre','3BHK','KTM')
print(Sachin.assests1,Sachin.assests2,Sachin.assests3)


