'''
Builder pattern can be used if want to regulate the creation of object.
This is an alternative to factory pattern. For simple things, factory pattern is used.
As code grows, we can use, builder, prototype or abstract factory accordingly.

In this pattern we have two types of classes:
    Builder: Builder class is an abstract class which builds the given class.
    Director: It controls how the builder will work.
'''

from abc import ABCMeta, abstractmethod

class Director(metaclass = ABCMeta): #This is an interface to direct the builder interface.
    def __init__(self):
        self._builder = None

    @abstractmethod
    def construct(self):
        pass

    def get_constructed_object(self):
        return self._builder.constructed_object

class Builder(metaclass = ABCMeta): #This is an interface to create the objects of a class.
    def __init__(self, constructed_object):
        self.constructed_object = constructed_object 

class Product:
    def __init__(self):
        pass
        #A class whose objects are to be created.

class ConcreteBuilder(Builder):
    #Implementation of builder interface.
    def __init__(self, constructed_object):
        pass

class ConcreteDirector(Director):
    #Implementation of director interface.
    def __init__(self):
        pass
    
    def construct(self):
        pass

    def get_constructed_object(self):
        pass

#Classis example for the pattern is django form builder and its admin panel autogenerated HTML.