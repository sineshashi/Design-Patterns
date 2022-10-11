'''
When we have a class with specific fields and method but we want some other fields and methods in the class \n
then we use adaptor method to convert our class approximately to the desired class.

The sample is:
'''


class WhatIHave:
    def fun1(self):
        ...

    def fun2(self):
        ...

class WhatIWant:
    def fun3(self):
        ...

'''
In this scenario, we have two methods to use:
1) Class Adaptor. It simply inherits both the classes and provide the desired functionality.
'''

class ClassAdaptor(WhatIHave, WhatIWant):
    def __init__(self, what_i_have:WhatIHave):
        self.what_i_havce = what_i_have
    def fun1(self):
        return self.what_i_havce.fun1

    def fun2(self):
        return self.what_i_havce.fun2

    def fun3(self):
        self.fun1()
        self.fun2()

class Client:
    def __init__(self, what_i_want):
        self.what_i_want = what_i_want

    def do(self):
        self.what_i_want.fun3()

adaptee = WhatIHave()
adapter = ClassAdaptor(adaptee)
client = Client(adapter)
client.do()

'''
2)Object Adaptor Pattern: Instead of inheriting classes, we use object composition.
'''

class ObjectAdaptor:
    def __init__(self, what_i_have: WhatIHave):
        self.what_i_have = what_i_have

    def fun3(self):
        #This is the desired function.
        self.what_i_have.fun1()
        self.what_i_have.fun2()

    def __getattribute__(self, __name: str):
        #Instead of inheritence, we preserve the properties of WhatIHave class by this function.
        return getattr(self.what_i_have, __name)