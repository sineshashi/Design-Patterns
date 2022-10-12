'''
When we need to control how the client will see the methods and objects and access them, we can use proxy.
In proxy, client sees what it want to see but that's not the actual thing. Like proxy network, provides \n
internet and everything needed and seems like a regualar network but it's not.

Proxy Pattern has three types:
1) Remote Proxy:
    When we want to abstract the location of resource, we can use it. The resource will seem to be local to \n
    client but will not be local.

2) Virtual Proxy:
    When we want to delay the creation of object untill the completion of process, we can use virtual proxy. \n
    Client will find the object is created already but we will create it later.

3) Protection Proxy:
    When there are multilayered clients and we want to hide them from each other, we can use protection proxy.

Generally proxy patterns has three elements:
client who want to access, object which is to be accessed and proxy which controls how client can access \n
object.

Let's say that we have a memoized function of calculating fibonacci sequence. Now we want to hide the \n
memoization from the client. In this case, we can use proxy pattern.
'''

class Calculator:
    def fib(self, n):
        if n < 2:
            return 1
        return self.fib(n-1)+self.fib(n-2)

def memoize(fn):
    _cache = {}
    def memoized(*args):
        key = (fn.__name__, args)
        if key in _cache:
            return _cache(key)
        fout = fn(*args)
        _cache[key] = fout
        return _cache[key]
    return memoized

class CalculatorProxy: #This hides the logic of fib function.
    def __init__(self, target):
        self.fib = memoize(target.fib)


calculator = CalculatorProxy(Calculator())
print(calculator.fib(5))