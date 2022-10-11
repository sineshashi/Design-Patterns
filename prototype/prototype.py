'''
This pattern follows, "Favor composition over inheritence."

In prototype pattern, we instead of inheriting the class and initializing them we clone the already instantiated object \n
and compose it with other operations, in this pattern, clone.

This can be used if have to use objects with same data over and over and being independent to each other.

Difference between Singleton and Prototype is that, In singleton, we use only one instance to manage \n
dependencies at global level but in prototype, we use objects with same data over and over. In this case\n
instead of initializing again and again, we instantiate one object or same some data and clone it over and over.

"Save the prototype in ram and clone it instead of creating new whenever necessary."
'''

from abc import abstractmethod, ABCMeta
from copy import deepcopy

#Here using abstract class is useless as python follows duck typing. We can work without it too.
class PrototypeAbstract(metaclass=ABCMeta):
    @abstractmethod
    def clone():
        pass

class Prototype(PrototypeAbstract): #This is the prototype which has clone method.
    def clone(self):
        deepcopy(self)

#To apply clone method, inherit this class and apply clone method.