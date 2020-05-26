# Valerie Nayak
# 4/15/2020
# Corey Schafer Object Oriented Programming YouTube Tutorial
# https://www.youtube.com/watch?v=BJ-VvGyQxho

class Employee:

    raise_amount = 1.04     # class variable

    def __init__(self, first, last, pay): # this is the constructor
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
    
    def fullname(self): # instance method
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

emp1 = Employee('Corey', 'Schafer', 50000)
emp2 = Employee('Test', 'User', 60000) 

print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)

# can access class variable from either the class or the instance
print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

# prints all the instance attributes
print(emp1.__dict__)

# print class attributes
print(Employee.__dict__)

# set Employee's raise amount
Employee.raise_amount = 1.05
# reprint
print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)