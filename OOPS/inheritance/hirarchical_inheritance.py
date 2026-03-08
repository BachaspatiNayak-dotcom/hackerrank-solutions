'''
Inheritance is a process of acquiring the properties of one class in another class.
In hirarchical inheritance there is one parent class and multiple child class
'''
class Employee:
    def __init__(self,name,sal):
        self.name=name
        self.sal=sal
    def work(self):
        print(f'{self.name} is working')
class Developer(Employee):
    def write_code(self):
        print(f'{self.name} is writting code')
class Tester(Employee):
    def testing(self):
        print(f'{self.name} is testing an application')
class Manager(Employee):
    def conduct_meeting(self):
        print(f'{self.name} is conducting a meeting')

d1=Developer('Sachin',200000)
d1.write_code()
t1=Tester('Anandita',50000)
t1.testing()
m1=Manager('Aditya',1000000)
m1.conduct_meeting()