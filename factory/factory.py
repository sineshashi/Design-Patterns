'''
If we want to get an object on a conditional basis then we can define a factory method.
i.e. Based on some string, we instantiate specific class.
'''

class Square:
    def draw(self):
        ...
        #Write the logic.

class Circle:
    def draw(self):
        ...
        #Write logic

#If want to instantiate square or circle based on input then we can define factory method.

def factory(shape):
    if shape == "square":
        return Square()

    if shape == "circle":
        return Circle()

    #We can wrtie this method as static method in a class like Shape or the base class inherited by the shapes to encapsulate the logic

'''
The above factory function seems illogical as we can instantiate the Circle and Square respectively whenever needed but that will be tightly coupled with Square and Circle classes.
'''

shape = factory("square")
shape.draw() #In this way, we can dynamically instantiate the classes.