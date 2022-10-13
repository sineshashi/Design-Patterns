'''
When we implement a new data structure and we want to iterate over that, iterator pattern is obvios.
'''

import abc

class Iterator(metaclass = abc.ABCMeta):
    @abc.abstractmethod
    def has_next():
        ...

    @abc.abstractmethod
    def next():
        ...

class Container(metaclass = abc.ABCMeta):
    @abc.abstractmethod
    def getIterator(self):
        ...

'''
Inherit these class and implement, more specifically, conatiner and iterator class should have the give methods.
A small implemention can be found here:
'''

class MyListIterator(Iterator):
    def __init__(self, mylist):
        self.index = 0
        self.my_list = mylist.list

    def has_next(self):
        return self.index < len(self.my_list)

    def next(self):
        self.index += 1
        return self.my_list[self.index-1]


class MyList(Container):
    def __init__(self, *args):
        self.list = list(args)

    def getIterator(self):
        return MyListIterator(self)

mylist = MyList(1, 2, 3, 4)
mylist_iter = mylist.getIterator()

while mylist_iter.has_next():
    print(mylist_iter.next())

'''
Although this works fine, but python has two magic functions __iter__ and __next__.
Implementing them in the container directly allows us to use for loop over the container.
'''

class MyNewList:
    def __init__(self, *args):
        self.index = 0
        self.list = list(args)

    def __iter__(self):
        return self #As list is an iterator.

    def __next__(self):
        try:
            self.index += 1
            return self.list[self.index-1]
        except:
            raise StopIteration()

l = MyNewList(1, 2, 3, 4)
print(l.list)
for i in l:
    print(i)

'''
Although above iterators are useless but give us a good understanding about how iterators are created \n
and implemented in python.
'''