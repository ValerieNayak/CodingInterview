# Valerie Nayak
# 4/15/2020
# Corey Schafer Object Oriented Programming YouTube Tutorial
# https://www.youtube.com/watch?v=ZDa-Z5JzLYM

class Employee:
    # you always need to put self (the instance) as the first argument for every method
    # the instance is always passed automatically

    def __init__(self, first, last, pay): # this is the constructor
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
    
    def fullname(self): # instance method
        return '{} {}'.format(self.first, self.last)

emp1 = Employee('Corey', 'Schafer', 50000)
emp2 = Employee('Test', 'User', 60000)

print(emp1)
print(emp2)

print(emp1.email)
print(emp2.email)

print(emp1.fullname())
print(Employee.fullname(emp1))