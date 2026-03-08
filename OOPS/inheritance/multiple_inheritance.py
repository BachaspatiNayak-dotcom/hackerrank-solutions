class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
class Employee:
    def __init__(self, salary):
        self.salary = salary

    def work(self):
        print("Employee is working")
class Manager(Person, Employee):
    def __init__(self, name, age, salary):
        Person.__init__(self, name, age)
        Employee.__init__(self, salary)
    def manage(self):
        print(self.name, "is managing the team")


m = Manager("Rahul", 35, 90000)

print(m.name)
print(m.age)
print(m.salary)

m.work()
m.manage()