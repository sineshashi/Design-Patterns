'''
When elements of containes are also containers in that case we can use composite pattern.
Composite pattern is a partitioning design pattern and describes a group of objects that is treated \n
the same way as a single instance of the same type of object. The intent of a composite is to “compose” \n
objects into tree structures to represent part-whole hierarchies. \n
It allows you to have a tree structure and ask each node in the tree structure to perform a task.


In object-oriented programming, a composite is an object designed as a composition of one-or-more similar objects,\n
all exhibiting similar functionality. This is known as a “has-a” relationship between objects.


In a simple way, if want to store a list of class objects, we can define a new class and store all the objects \n
so that we can treat that collect as a class instead a collection of objects.
'''

class Obj:
    def __init__(self):
        ...

class ContainerObj:
    def __init__(self, objects =[]):
        self.objects = objects

    def add(self, obj):
        ...

    def remove(self, obj):
        ...

    def find(self, obj):
        ...

    def lenth(self):
        ...