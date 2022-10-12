'''
Whenever you want to send an instruction or set of instructions from one object to 
another, while keeping these objects loosely coupled, it is wise to encapsulate everything 
needed to execute the instructions in some kind of data structure.

The class of objects used to encapsulate 
information needed by some other method in order to execute is called a command.

A simple structure of command pattern is below:
'''

class Command:
    def __init__(self, receiver, text):
        self.reciever = receiver
        self.text = text

    def execute(self):
        self.reciever.print_message(self.text)

class Receiver:
    def print_message(self, text):
        print(text)

class Invoker:
    def __init__(self, commands=[]):
        self.commands = commands
    def add_command(self, command):
        self.commands.append(command)

    def execute(self):
        for command in self.commands:
            command.execute()

invoker = Invoker()
invoker.add_command(Command(Receiver(), "Hii I am msg."))
invoker.add_command(Command(Receiver(), "Hii, who are you?"))
invoker.execute()

#Here invoker will not be able to see the implementation in the Receiver class but will operate through command.