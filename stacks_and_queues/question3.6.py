# Valerie Nayak
# 6/18/2020
# Question 3.6

from collections import deque

class Dog:
    def __init__(self, date):
        self.date = date
    
    def display(self):
        print('Dog:', date, end=' ')

class Cat:
    def __init__(self, date):
        self.date = date
    
    def display(self):
        print('Cat', date, end=' ')

class AnimalShelter:
    def __init__(self):
        self.dogs = deque()
        self.cats = deque()

    def enqueue(self, date, dog=True):
        if dog == True:
            self.dogs.append(Dog(date))
        else:
            self.cats.append(Cat(date))
    
    def dequeue_any(self):
        if self.dogs[0].date < self.cats[0].date:
            return self.dogs.popleft()
        else:
            return self.cats.popleft()

    def dequeue_dog(self):
        return self.dogs.popleft()
    
    def dequeue_cat(self):
        return self.cats.popleft()