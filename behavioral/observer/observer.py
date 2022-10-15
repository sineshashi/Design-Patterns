'''
A software design pattern in which an object, called the subject, maintains a list of its 
dependents, called observers, and notifies them automatically of any state changes, usually 
by calling one of their methods. It is mainly used to implement distributed event handling 
systems 
'''

import abc

class Observer(metaclass = abc.ABCMeta):
    @abc.abstractmethod
    def update(self):
        ...

class ConcreteOberver:
    def update(self, observed):
        ...

class Observable:
    def __init__(self):
        self.observers = set()

    def register(self, observer):
        self.observers.add(observer)

    def unregister(self, observer):
        self.observers.remove(observer)

    def update_all(self):
        for observer in self.observers:
            observer.update(self)

##In case we want to call different type of observers, we can store callbacks instead of observer.

class NewObservable:
    def __init__(self):
        self.callbacks = set()

    def register(self, callback):
        self.callbacks.remove(callback)

    def unregister(self, callback):
        self.callbacks.remove(callback)

    def update_all(self):
        for callback in self.callbacks:
            callback(self)