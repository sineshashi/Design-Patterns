'''
When we have a sequence of functions to call like sequence of middlewares then instead of calling them all \n
in a single funtion, we can use Chain Of Responsibilty pattern.
'''

def fun1():
    ...

def fun2():
    ...

def fun3():
    ...

def main():
    fun1()
    fun2()
    fun3()

'''
The above main function calls them all which is a vague to do this.
Because if we have many functions this will become a mess of code.
One good way to handle this is to create classes and save which to execute after which one.
'''

class CatchAll():
    def __init__(self):
        self.next = None
    def execute():
        print("executed")

class Fun1:
    def __init__(self):
        self.next = CatchAll()
    def execute(self):
        fun1()
        return self.next.execute()

class Fun2:
    def __init__(self):
        self.next = CatchAll() 
    def execute(self):
        fun2()
        return self.next.execute()

class Fun3:
    def __init__(self, next):
        self.next = CatchAll()
    def execute(self):
        fun3()
        return self.next.execute()

def main_f(head):
    head.execute()

#Below, we will create a sequence in which functions are going to be executed.
hd = Fun1()

current = hd
current.next = Fun2()

current = current.next
current.next = Fun2()

main_f(hd)

#Although above implementation is a bit longer but will avoide the mess of code.
#Let's see another implementation, if output of one is input for another.

class Dispatcher:
    def __init__(self, handlers = []):
        self.handlers = handlers

    def execute(self, request):
        for handler in self.handlers:
            request = handler(request)
        return request

#The above class has capability to execute many handlers in the sequential order.