'''
In this pattern, we do not need to change the interface but add addtional functionality.
'''

#Class decorators must contain __call__ method.
import time
from functools import wraps

class ClassDecorator: #This decorator prints the current time on start of the function and after its execution.
    def __init__(self, f):
        self.f = f

    def __call__(self, *args):
        print(time.time()) #Prints current time.
        fout = self.f(*args)
        print(time.time())
        return fout

@ClassDecorator #Python provides this @ symbol for decorating some thing otherwise we can pass f as arg in class.
def some_function(*args):
    ...


#Function decorator:

def funtion_decorator(f):
    @wraps(f) #This does not change the __name__ and __doc__ of f function.
    def wrap_f(n):
        print(time.time())
        fout = f(n)
        print(time.time())
        return fout
    return wrap_f

@funtion_decorator
def some_func(n):
    ...

#If we need to decorate every method of a class, we can decorate the whole class instead.
#define a decorator which can decorate the class and use that.