'''
The same problem solved by factory method can be shaped in different form and can be solved by using \n
abstract factory method.

We can create abstract factory to create objects of a specific class and can instantiate a class on \n
conditional basis based on factory used.
'''

from abc import ABCMeta, abstractmethod

class Square:
    def draw(self):
        ...
        #Write the logic.

class Circle:
    def draw(self):
        ...
        #Write logic

class AbstractFactory(metaclass = ABCMeta):
    @abstractmethod #This means, every class will have this method which inherit it. and we can call this for every class inherirting this class.
    def create_object(self):
        pass

class SquareFactory(AbstractFactory):
    def create_object(self):
        #Write logic
        return Square()

class CircleFactory(AbstractFactory):
    def create_object(self):
        #Write logic.
        return Circle()

def draw_something(factory):
    factory.create_object().draw()

square_factory = SquareFactory()
draw_something(square_factory) #In this way we can call a class based on abstract factory.