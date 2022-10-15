'''
When we want to choose some strategy or function at runtime e.g. choosing between two functions, we can go for this pattern.

Although we can use if and else like:
'''
def choose(strategy, a, b):
    if strategy == "add":
        return a+b
    if strategy == "subtract":
        return a-b

'''
But this is a vague solution which will be complex for some real world scenerios. Now let us see some simple implementaion of this pattern.
'''

class StrategyExecutor:
    def __init__(self, strategy = None):
        self.strategy = strategy

    def execute(self, arg1, arg2):
        if self.strategy is None:
            raise NotImplementedError("Not implemented")

        else:
            return self.strategy.execute(arg1, arg2)

class AdditionStrategy:
    def execute(self, arg1, arg2):
        return arg1 +  arg2

class SubtractionStrategy:
    def execute(self, arg1, arg2):
        return arg1 - arg2

executor = StrategyExecutor()
executor.strategy = AdditionStrategy()
print(executor.execute(1, 2))
executor.strategy = SubtractionStrategy()
print(executor.execute(2, 1))

'''
Instead of wrapping addition and subtractions in classes, we can directly pass these functions to StrategyExecutor class and modify the execute function to call directly the strategy with given arguments. Even we can remove the Executore class and make it a functions considering other functions as arguments.
'''