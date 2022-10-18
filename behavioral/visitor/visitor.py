'''
When we want to perform an action in a set of classes, we have good opportunity to use this pattern.
i.e., we have a series of objects of different classes, we want to check the status of each object.
If we have some tools like, printer, electric bulb and some other devices and we want to check whether each of device is connected and ready for use. Or We want to check printer is connected and others are not or printer is not busy while some of them are busy.
Whenever, we want a specific pattern for different classes, we can use it.
'''

import abc
import random

class Visitable:
    def accept(self, visitor):
        visitor.visit(self)

class CompositeVisitable(Visitable):
    def __init__(self, iterable):
        self.iterable = iterable

    def accept(self, visitor):
        for element in self.iterable:
            element.accept(visitor)
        visitor.visit(self)

class AbstractVisitor(metaclass = abc.ABCMeta):
    @abc.abstractmethod
    def visit(self, element):
        ...

class Light(Visitable):
    def __init__(self, name):
        self.name = name
        self.status = self.get_status()

    def get_status(self): #This returns random status. In real life this will be determied by device driver.
        return random.choice(range(-1, 2))

    def is_online(self):
        return self.status != -1

    def boot_up(self):
        self.status = 0

#Let There are two persons living in same home and they have compromised with each other when to turn light on, when to off, when to use more bright color.
class LightStatusUpdateVisitor(AbstractVisitor):
    def __init__(self, person1_home, person2_home):
        self.person1home = person1_home
        self.person2home = person2_home

    def visit(self, element):
        if self.person1home:
            if self.person2home:
                element.status = 1
            else:
                element.status = 2
        elif self.person2home:
            element.status = 1
        else:
            element.status = 0
#Similar case of Thermostat too.
class TempRegulator(Visitable):
    def __init__(self, name):
        self.name = name
        self.status = self.get_status()

    def get_status(self): #This returns random status. In real life this will be determied by device driver.
        return random.choice(['heating', 'cooling', 'on', 'off', 'error'])

    def is_online(self):
        return self.status != 'off'

    def boot_up(self):
        self.status = 'on'

class TempRegulatorStatusUpdateVisitor(AbstractVisitor):
    def __init__(self, person1_home, person2_home):
        self.person1home = person1_home
        self.person2home = person2_home

    def visit(self, element):
        if self.person1home:
            if self.person2home:
                element.status = 'cooling'
            else:
                element.status = 'heating'
        elif self.person2home:
            element.status = 'cooling'
        else:
            element.status = 'off'

#Now here want to regulate light and Temperatur on the basis of which of person1 and person2 is in Home.
class CompositeVisitor(AbstractVisitor):
    def __init__(self, person1home, person2home):
        self.person1home = person1home
        self.person2home = person2home

    def visit(self, element):
        try:
            c = element.__class__.__name__ + "StatusUpdateVisitor"
        except:
            raise ValueError("NO visitor found.")

        visitor = c(self.person1home, self.person2home)
        visitor.visit(element)
#In this way, we can regulate the each and every device connected according to the persons in home.
'''
Whenever such situation arises, we can use visitor pattern. i.e. Given a conditon, if we want to perform a set of actions, we can creater visitor class.
'''