class Receiver:
    def __init__(self, value):
        self._value = value

    def add(self, value):
        self._value += value

    def subtract(self, value):
        self._value -= value

class AddCommand:
    def __init__(self, receiver, value):
        self.receiver = receiver
        self.value = value

    def execute(self):
        return self.receiver.add(self.value)

    def undo(self):
        return self.receiver.subtract(self.value)

class SubtractCommand:
    def __init__(self, receiver, value):
        self.receiver = receiver
        self.value = value

    def execute(self):
        return self.receiver.subtract(self.value)

    def undo(self):
        return self.receiver.add(self.value)

class Invoker:
    def __init__(self, commands = []):
        self.commands = commands
        self.undo_stack = []

    def add_command(self, command):
        self.commands.append(command)

    def undo(self):
        self.undo_stack.pop().undo()

    def execute(self):
        for command in self.commands:
            command.execute()
            self.undo_stack.append(command)

recevier = Receiver(10)
invoker = Invoker()
invoker.add_command(AddCommand(recevier, 5))
invoker.add_command(SubtractCommand(recevier, 2))
invoker.execute()

print(recevier._value)
invoker.undo()
invoker.undo()

print(recevier._value)

'''
In this way, we can seperate our logic from client as well as can group the commands to execute.
'''