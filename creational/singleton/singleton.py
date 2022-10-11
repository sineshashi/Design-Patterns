'''
In Singleton Pattern, Object state is managed at global level. \n
We check if the object is already instantiated and if it is we use that instead of instantiating another.
'''


class SingletonObject:
    class _SingletonObject:  # This is the real object which will be managed at global level.
        def __init__(self) -> None:
            self.val = None

        def __str__(self) -> str:
            return f"{self} {self.val}"

    instance = None

    def __new__(cls):
        if not SingletonObject.instance:  # Cheching if object is not instantiated.
            SingletonObject.instance = SingletonObject._SingletonObject()
        return SingletonObject.instance

    def __getattribute__(self, __name: str):
        return getattr(SingletonObject.instance, __name)

    def __setattr__(self, __name: str, __value) -> None:
        return setattr(SingletonObject.instance, __name, __value)
