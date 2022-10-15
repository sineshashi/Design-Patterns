'''
State Pattern is used where we need to maintain different states for some objects.
'''

class State:
    pass

class ConcreteState1(State):
    def __init__(self, state_machine):
        self.state_machine = state_machine

    def switch_state(self):
        self.state_machine.state = self.state_machine.state2

class ConcreteState2(State):
    def __init__(self, state_machine):
        self.state_machine = state_machine

    def switch_state(self):
        self.state_machine.state = self.state_machine.state1

class StateMachine:
    def __init__(self):
        self.state1 = ConcreteState1(self)
        self.state2 = ConcreteState2(self)
        self.state = self.state1

    def switch(self):
        self.state.switch_state()

state_machine = StateMachine()
print(state_machine.state)
state_machine.switch()
print(state_machine.state)