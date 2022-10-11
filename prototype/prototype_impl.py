from copy import deepcopy
from .prototype import Prototype

#Let us say we have three levels defined in the dict.
levels = {
    1: {
        "power": 50,
        "drange": 10,
        "flexibility": 55,
        "speed": 5
    },
    2: {
        "power": 65,
        "drange": 15,
        "flexibility": 70,
        "speed": 10
    },
    3: {
        "power": 80,
        "drange": 20,
        "flexibility": 85,
        "speed": 15
    }
}
#Let us say we are going to design a game which has knights with some properties and are defined as per level.
class Knight:
    def __init__(self, level):
        self.unit_type = "knight" #Saving this if we have more such classes.
        #Interact with db here. Let us consider following fields are from a db.
        self.power = levels[level]["power"]
        self.range = levels[level]["drange"]
        self.flexibility = levels[level]["flexibilty"]
        self.speed = levels[level]["speed"]
   
#If we use the above class and we go with these levels, we will initialize the class every time.

knight1_level1 = Knight(1)
knigh2_level2 = Knight(1)
#In this way it will initialize class for each level and every time player creates a new knight but they all will have same data.
#Now consider we were interacting with db each time, it will kill our application.
#To avoid that, we store these prototypes in the RAM and clone them.

class KnightPPattern(Prototype):
    def __init__(self, level):
        self.unit_type = "knight" #Saving this if we have more such classes.
        #Interact with db here.
        self.power = levels[level]["power"]
        self.range = levels[level]["drange"]
        self.flexibility = levels[level]["flexibilty"]
        self.speed = levels[level]["speed"]

    def clone(self):
        deepcopy(self)

class Baracks:
    def __init__(self):
        self.units = {
            "knight": {
                1: KnightPPattern(1),
                2: KnightPPattern(2),
                3: KnightPPattern(3)
            }
        }

    def create_unit(self, type, level):
        return self.units[type][level].clone()

#Now this will not interact with db every time but clone the instance which is already in RAM.
#We could have directlty used KnightPPattern(1) instead of creating barack but creating Barack gives us power to decouple things more.
#and provides a simple funtion to use instead of using .clone() every time.
barack = Baracks()

knight1_level1 = barack.create_unit("knight", 1)
knight2_level1 = barack.create_unit("knight", 1)